from TTS.api import TTS
from ttsUtils import createFileName, findInputFiles, printToLog
import os

############################
# Text files from resources/input/ to audio
# Input files larger than 2x char_limiter might destroy perf
###########################

# CONFIGS
# See README for explanations
lang = "pl"
speaker_wav = "tts/fi_sample3.wav" # Custom wav voice
speaker = "Tanja Adelina"
model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

# Extra args
split_sentancess = True
speed = 1 # Not in use

file_out_path = "audio/"
file_input_path = "./resources/input/"
char_limiter = 20000

## App
def toFile(txt):
    tts = TTS(model_name = model_name)
    id = createFileName()
    tts.tts_to_file(
        text=txt, 
        speaker_wav=speaker_wav, # either speaker or speaker_wav, not both
        # speaker=speaker,
        language=lang, 
        file_path=f"{file_out_path}{createFileName()}.wav",
        enable_text_splitting = split_sentancess)
    
    printToLog(f"Done generating file {id}")

if __name__ == "__main__":
    try:
        inputArr = findInputFiles(file_input_path)
        if len(inputArr) > 0:
            printToLog(f"TTS Service found {len(inputArr)} input files.")
        else:
            printToLog("ERROR: No Input files found")

        # FILE INPUT LOOP
        for input in inputArr:
            with open(f'{file_input_path}{input}', 'r') as f:
                chunk = f.read()
                if len(chunk) > char_limiter:
                    chunk01 = chunk[:char_limiter]
                    chunk02 = chunk[:char_limiter + 1]
                    toFile(chunk01)
                    toFile(chunk02)
                else:
                    toFile(chunk)

    except Exception as e:
        print(e)
        printToLog(f"ERROR: {e}")