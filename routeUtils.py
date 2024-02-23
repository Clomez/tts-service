from ttsUtils import createFileName, getUuid
from configs import config

def getArgs(request):
    return {
        "filename" : f"{request.args.get('user')}-{createFileName()}",
        "dataSet" : request.get_data(),
        "theme" : request.args.get('theme'),
        "user" : request.args.get('user'),
        "title" : request.args.get('title'),
        "language" : request.args.get('language'),
        "id" : getUuid()
}

def validateRequestArgs(request):
    if (request.args.get('user') is None):
        raise Exception(f"Incorrect user arg: {request.args.get('user')}")
    if (request.get_data() is None):
        raise Exception(f"Incorrect input data")


def return404():
    return "Resource nowhere to be seen."

def futureResourceLocation(args):
    return f"Link: {config['host']}/{args['filename']}.wav/get"

def getResourceLocation(id):
    return f"{config['path_to_file']}/{id}"