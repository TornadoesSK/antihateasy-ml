from flask import Blueprint, request
import json


endpoints=Blueprint('endpoints',__name__)

@endpoints.route('/', methods=['GET'])
def home():
    return "Hello world"

@endpoints.route('/gettextsentiment', methods=['POST'])
def gettextsentiment():
    data = json.loads(request.data)
    if "you are a very bad ugly person" in data["tweet"]:
        return { "hide" : True }
    
    return { "hide" : False }