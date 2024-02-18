from multiprocessing import Process
from multiprocessing import Pipe

import subprocess
import socket
from TTS.tts import ttsToFile


import queue
import sys

import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

############################
# Unsorted code examples for using TTS
###########################

socket_path = 'tmp/say_socket'
use_cuda = False
q = queue.Queue()


# Inferencer subprocess
def brain(brainIn, stopIn, mouthOut):
    process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out)

    # Load TTS model
    print("--- Loading model...")
    from TTS.tts.configs.xtts_config import XttsConfig
    from TTS.tts.models.xtts import Xtts
    config = XttsConfig()
    config.load_json("XTTS-v2/config.json")
    model = Xtts.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="XTTS-v2")
    model.tts_to_file()
    print("--- Loading model Done...")

    if use_cuda:
        model.cuda()

    # Compute speaker latents
    print("--- Computing speaker latents...")
    gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=["tts/fr_sample.wav"])

    # Brain main loop
    while True:
        print("Ready")
        text = brainIn.recv()
        chunks = model.inference_stream(
            text,
            "en",
            gpt_cond_latent,
            speaker_embedding,
            enable_text_splitting = True
        )

        for i, chunk in enumerate(chunks):
            if stopIn.poll():
                stopIn.recv()
                break
            mouthOut.send(chunk.detach().cpu())

        
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

# Audio player subprocess
def mouth(mouthIn, stopIn, pauseIn):
    import sounddevice as sd
    device="Speakers (High Definition Audio, MME"
    stream = sd.OutputStream(device=device, samplerate=24000, channels=1)
    stream.start()

    # Mouth main loop
    while True:
        if pauseIn.poll():
            pauseIn.recv()
            print("--- Pausing")
            pauseIn.recv()
            print("--- Pause released")

        if stopIn.poll():
            stopIn.recv()
            while mouthIn.poll(): # clear the que
                mouthIn.recv()
            continue
        data = mouthIn.recv()
        stream.write(data)

        TTS.tts.toFile


# Create subprocesses
if __name__ == "__main__":

    mouthOut, mouthIn = Pipe()
    mouthStopOut, mouthStopIn = Pipe()
    mouthPauseOut, mouthPauseIn = Pipe()
    mouth_process = Process(target=mouth, args=(mouthIn, mouthStopIn, mouthPauseIn))
    mouth_process.start()

    brainOut, brainIn = Pipe()
    brainStopOut, brainStopIn = Pipe()

    brain_process = Process(target=brain, args=(brainIn, brainStopIn, mouthOut))
    brain_process.start()

    # Remove the socket if exists
    # Not needed in windows

    # Create the Unix socket server for recieving text
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 6060))
    server.listen(1)

    # Main loop
    try:
        while True:
            print("--- Listening for incoming connections...")
            connection, client_address = server.accept()
            data = connection.recv(64768)
            connection.close()

            if not data:
                print("!!! NO DATA/EMPTY BINARY ???")
                continue

            msg = data.decode()

            if msg.isspace():
                print("!!! Skipping whitespace msg")
                continue

            if msg == "!Stop":
                print("--- Stop called")
                brainStopOut.send(1)
                mouthStopOut.send(1)
                continue

            if msg == "!Pause":
                mouthPauseOut.send(1)
                continue

            print(msg)
            brainOut.send(msg)
            

    except:
        connection.close()
        # os.unlink(socket_path)
        mouth_process.kill()
        brain_process.kill()