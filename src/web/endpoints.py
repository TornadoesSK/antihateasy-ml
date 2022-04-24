from flask import Blueprint, request, abort
import json
from ..ml import Net

endpoints=Blueprint('endpoints', __name__)
model = Net.load_from_checkpoint("src/ml/checkpoints/50epochs.ckpt")

@endpoints.route('/', methods=['GET'])
def home():
    return "Hello world"

@endpoints.route('/gettextsentiment', methods=['POST'])
def gettextsentiment():
    data = json.loads(request.data)
    # if a username isn't supplied in the request, return a 400 bad request
    if "tweet" not in data.keys():
        abort(400)

    pred = model.predict_sentence(data["tweet"])

    is_bad = pred["class"] != 2
    
    return { "hide" : is_bad }
    