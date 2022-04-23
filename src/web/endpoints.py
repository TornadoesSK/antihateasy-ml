from flask import Blueprint, request

endpoints=Blueprint('endpoints',__name__)

@endpoints.route('/', methods=['GET'])
def home():
    return "Hello world"
