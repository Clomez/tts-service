from TTS.api import TTS
from ttsUtils import printToProcessLog as printToLog
import time
from configs import tts_config, config

############################
# Text files from resources/input/ to audio
# Input files larger than 2x char_limiter might destroy perf
###########################

## App
def toFile(txt, fileName, language):
    tts = TTS(model_name = tts_config["model_name"])
    tts.tts_to_file(
        text=txt, 
        # speaker_wav=speaker_wav, # either speaker or speaker_wav, not both
        speaker=tts_config["speaker"],
        language=language, 
        file_path=f"{tts_config['path_to_file']}{fileName}.wav",
        enable_text_splitting = tts_config["split_sentancess"])
    
    printToLog(f"Done generating file {fileName} - thread process shutting down")


def requestService(filename, path_to_input, language):
    time.sleep(5) # ugly hack for ensuring input file has time to write

    printToLog(f"Starting requested job id: {filename} in new thread")
    printToLog(f"System configs: {config}")
    printToLog(f"Job configs: {tts_config}")

    file = f"{path_to_input}/{filename}"

    try:
        with open(f'{file}', 'r') as f:
            chunk = f.read()
            toFile(chunk, filename, language)
            f.close

    except FileNotFoundError as e:
        printToLog(f"ERROR File not found - err: {e}")

    except Exception as e:
        printToLog(f"ERROR Somethings happend ?! err: {e}")

    
