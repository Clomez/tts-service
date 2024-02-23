import os
from configs import config, tts_config
from datetime import datetime
import pprint

def findInputFiles(path):
    return os.listdir(path)[1:] # rm .git from arr

def getUuid():
    import uuid
    return str(uuid.uuid4())

def createFileName():
    import uuid
    uuid = str(uuid.uuid4())
    id = uuid[:7]
    return f"{hourStamp()}-{id}"

def shorten(txt):
    if len(txt) > 60:
        return txt[:60]
    else:
        return txt
    
def hourStamp():
    current_dateTime = datetime.now()
    return f"{current_dateTime.hour}-{current_dateTime.minute}"

def printToLog(msg):
    with open('log/log.txt', 'a') as f:
        f.write(f"{hourStamp()} -- {msg}\n")

def printSystemConfigs():
     printToProcessLog(pprint.pformat(config))
     printToProcessLog(pprint.pformat(tts_config))

def printToProcessLog(msg):
    with open('log/process_log.txt', 'a') as f:
        f.write(f"{hourStamp()} -- {msg}\n")

def createInputFile(args):
	try:
		with open(f"{config['path_to_input']}/{args['filename']}", 'w') as f:
			f.write(str(args["dataSet"].decode("utf-8")))
			f.close()

	except FileNotFoundError as e:
		printToLog(f"Error no input file")
          
def cleanup():
    folder = config['path_to_input']
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))