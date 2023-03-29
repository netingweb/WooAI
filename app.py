import openai
import simplejson
import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to WooAI API'


@app.route('/generate', methods=['GET'])
def generate():

    if not request.args.get('type', ''):
        return 'ko'

    prompt='Generate the following elements for a web page according to the following data.\n'

    if request.args.get('current_url', ''):
        prompt += 'The current URL of the web page is ' + request.args.get('current_url', '') + '.\n'
    if request.args.get('current_title', ''):
        prompt += 'The current title of the web page is ' + request.args.get('current_title', '') + '.\n'
    if request.args.get('current_description', ''):
        prompt += 'The current description for this ' + type + ' is ' + request.args.get('current_description', '') + '.\n'

    if request.args.get('type', ''):
        prompt += 'This web page is about a ' + request.args.get('type', '') + '.\n'

    if request.args.get('keywords', ''):
        prompt += 'All the SEO elements must be optimized for the following keywords: ' + request.args.get('keywords', '') + '.\n'

    if request.args.get('title', ''):
        prompt += 'Generate the best possible SEO title for this page.\n'
    if request.args.get('description', ''):
        prompt += 'Generate the best possible SEO description for this page.\n'

    prompt += " I would like you to generate a JSON formatted response to this request"

    return getCompletion(prompt)


def getCompletion(prompt):
    openai.api_key = "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"
    context = 'You are a SEO expert and you need to help me to support and optmize all the SEO aspect of specific web page. Please respond as accurate and professional as you can to the following query'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system","content": context},
                  {"role": "user", "content":  prompt}]
        )
    # print(completion)
    return response.choices[0].message.content