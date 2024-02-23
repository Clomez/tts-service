import os

from datetime import datetime

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

def printToProcessLog(msg):
    with open('log/process_log.txt', 'a') as f:
        f.write(f"{hourStamp()} -- {msg}\n")