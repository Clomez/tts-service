from TTS.api import TTS
from ttsUtils import printToProcessLog as printToLog, printSystemConfigs, cleanup
import time
from configs import tts_config, config

############################
# Text files from resources/input/ to audio
# Input files larger than 2x char_limiter might destroy perf
###########################

def toFile(txt, args):
    tts = TTS(model_name = tts_config["model_name"])
    tts.tts_to_file(
        text=txt, 
        # speaker_wav=speaker_wav, # either speaker or speaker_wav, not both
        speaker=tts_config["speaker"],
        language=args['language'], 
        file_path=f"{tts_config['file_out_path']}{args['filename']}.wav",
        enable_text_splitting = tts_config["split_sentancess"])
    
    printToLog(f"Done generating file {args['filename']} - thread process shutting down")


def requestService(args):
    time.sleep(5) # ugly hack for ensuring input file has time to write

    printToLog(f"Starting requested job id: {args['filename']} in new thread")
    printSystemConfigs()

    file = f"{config['path_to_input']}/{args['filename']}"

    try:
        with open(f'{file}', 'r') as f:
            chunk = f.read()
            toFile(chunk, args)
            f.close

        time.sleep(3)
        cleanup()

    except FileNotFoundError as e:
        printToLog(f"ERROR File not found - err: {e}")

    except Exception as e:
        printToLog(f"ERROR Somethings happend ?! err: {e}")

    
