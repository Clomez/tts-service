from datetime import datetime

def hourStamp():
    current_dateTime = datetime.now()
    return f"{current_dateTime.hour}-{current_dateTime.minute}"

def printToLog(msg):
    with open('log/log.txt', 'a') as f:
        f.write(f"{hourStamp()} -- {msg}\n")