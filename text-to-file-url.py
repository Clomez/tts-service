from TTS.api import TTS
import socket
from datetime import datetime

############################
# Text to audio using sockets
# TODO: character encoding
###########################

# CONFIG
# See README for explanations
lang = "en"
speaker_wav = "tts/en_sample.wav"
speaker = "Abrahan Mack"

# Extra args
split_sentancess = True
speed = 1 # Not in use

file_out_path = "audio/"
models = "XTTS-v2/tts_models/multilingual/multi-dataset/xtts_v2"

## App
def hourStamp():
    current_dateTime = datetime.now()
    return f"{current_dateTime.hour}-{current_dateTime.minute}"

def createFileId():
    import uuid
    uuid = str(uuid.uuid4())
    id = uuid[:7]
    return f"{hourStamp()}-{id}"

def shorten(txt):
    if len(txt) > 60:
        return txt[:60]
    else:
        return txt

def printToLog(msg):
    with open('log/log.txt', 'a') as f:
        f.write(f"{hourStamp()} -- {msg}\n")

def toFile(txt):
    tts = TTS(model_name = models)
    id = createFileId()
    tts.tts_to_file(
        text=txt, 
        # speaker_wav=speaker_wav, # either speaker or speaker_wav, not both
        speaker=speaker,
        language=lang, 
        file_path=f"{file_out_path}{createFileId()}.wav",
        enable_text_splitting = split_sentancess
        )
    
    printToLog(f"Done generating file {id}")

def startServer():
    try:
        # Create socket server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 6060))
        server.listen(1)
        printToLog("Server started")
        return server
    except Exception as e:
        print(e)
        printToLog(f"SERVER ERROR: {e}")
    
if __name__ == "__main__":
    try:
        while True:
            connection, client_address = startServer().accept()
            data = connection.recv(64768)
            connection.send("job accepted".encode())
            connection.close()
            msg = data.decode()
            printToLog(f"Text input: {shorten(msg)}")
            toFile(msg)

    except Exception as e:
        print(e)
        printToLog(f"ERROR: {e}")
        connection.close()