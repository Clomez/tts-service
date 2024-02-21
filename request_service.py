from TTS.api import TTS
from ttsUtils import printToLog
import time

############################
# Text files from resources/input/ to audio
# Input files larger than 2x char_limiter might destroy perf
###########################

# CONFIGS
# See README for explanations
lang = "en"
speaker_wav = "tts/fi_sample3.wav" # Custom wav voice
speaker = "Andrew Chipper"
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

# Extra args
split_sentancess = True
speed = 1 # Not in use

file_out_path = "audio/"
char_limiter = 20000

## App
def toFile(txt, fileName):
    tts = TTS(model_name = model_name)
    tts.tts_to_file(
        text=txt, 
        # speaker_wav=speaker_wav, # either speaker or speaker_wav, not both
        speaker=speaker,
        language=lang, 
        file_path=f"{file_out_path}{fileName}.wav",
        enable_text_splitting = split_sentancess)
    
    printToLog(f"Done generating file {fileName}")


def requestService(filename, path_to_input):
    printToLog(f"Starting requested job id: {filename} waiting for file")
    time.sleep(2)

    file = f"{path_to_input}/{filename}"

    try:
        with open(f'{file}', 'r') as f:
            chunk = f.read()
            toFile(chunk, filename)
            f.close

    except FileNotFoundError as e:
        printToLog(f"ERROR File not found - err: {e}")

    except Exception as e:
        printToLog(f"ERROR Somethings happend ?! err: {e}")

    
