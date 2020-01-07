from flask import Flask, request
from modules.init import init_modules

from api.process_xml import *

app = Flask(__name__)
env = init_modules()


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if not request.json or not ('file_name' in request.json and 'content' in request.json):
        return {'error': 'Invalid request body'}, 400

    return process_xml(env, request.json['content'], request.json['file_name'])


# Get document by tag
@app.route('/tags/<tag_name>', methods=['GET'])
def get_by_tag():
    tag_name = request.query_string.tag_named

    return 200


if __name__ == '__main__':
    app.run(debug=True)
