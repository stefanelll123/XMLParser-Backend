from flask import Flask, request
from modules.init import init_modules

from api.process_xml import *
from util.utils import *

app = Flask(__name__)
env = init_modules()

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if not request.json or not ('file_name' in request.json and 'content' in request.json):
        return {'error': 'Invalid request body'}, 400

    return process_xml(env, request.json['content'], request.json['file_name'])

if __name__ == '__main__':
    app.run(debug=True)