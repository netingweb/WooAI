import flask
from flask import request

app = flask.Flask(__name__)

@app.route('/generate', methods=['GET'])
@app.route('/', methods=['GET'])

def home():
    return 'Welcome to WooAI API'
