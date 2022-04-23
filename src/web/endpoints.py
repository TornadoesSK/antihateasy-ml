from flask import Blueprint, request, abort
import json


endpoints=Blueprint('endpoints',__name__)

@endpoints.route('/', methods=['GET'])
def home():
    return "Hello world"

@endpoints.route('/gettextsentiment', methods=['POST'])
def gettextsentiment():
    data = json.loads(request.data)
    # if a username isn't supplied in the request, return a 400 bad request
    if "tweet" not in data.keys():
        abort(400)
        
    if "you are a very bad ugly person" in data["tweet"]:
        return { "hide" : True }
    
    return { "hide" : False }