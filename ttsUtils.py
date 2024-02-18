from logger import hourStamp
import os

def findInputFiles(path):
    return os.listdir(path)[1:] # rm .git from arr

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