from ttsUtils import createFileName, getUuid
from configs import config

def getArgs(name, request):
    return {
        "filename" : f"{name}-{createFileName()}",
        "dataSet" : request.get_data(),
        "theme" : request.args.get('theme'),
        "user" : request.args.get('user'),
        "title" : request.args.get('title'),
        "language" : request.args.get('language'),
        "id" : getUuid()
}

def return404():
    return "Resource nowhere to be seen."

def futureResourceLocation(args):
    return f"Link: {config['host']}/{args['filename']}.wav/get"

def getResourceLocation(id):
    return f"{config['path_to_file']}/{id}"