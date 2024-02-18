from TTS.api import TTS
from logger import printToLog
from ttsUtils import createFileId, findInputFiles

import os

############################
# Text files from resources/input/ to audio
# Input files larger than 2x char_limiter might destroy perf
###########################

# CONFIGS
# See README for explanations
lang = "en"
speaker_wav = "tts/en_sample.wav"
speaker = "Abrahan Mack"

# Extra args
split_sentancess = True
speed = 1 # Not in use

file_out_path = "audio/"
file_input_path = "./resources/input/"
char_limiter = 500

models = "XTTS-v2/tts_models/multilingual/multi-dataset/xtts_v2"

## App
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

if __name__ == "__main__":
    try:
        inputArr = findInputFiles(file_input_path)
        if len(inputArr) > 0:
            printToLog(f"TTS Service found {len(inputArr)} input files.")

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