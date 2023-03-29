import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/generate', methods=['GET'])
@app.route('/', methods=['GET'])

def home():
    return 'Welcome to WooAI API'

def generate():
    req = []
    args = request.args['type', 'title', 'description', 'description_lenght', 'excerpt', 'slug', 'meta_description', 'og_schema', 'image_alt', 'hints']
    for arg in args:
        req.append(arg)
    return req