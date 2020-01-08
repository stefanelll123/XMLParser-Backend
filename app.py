from flask import Flask, request
from modules.init import init_modules
from api.process_xml import *
from api.process_with_tags import get_docs_with_tag_name
from api.process_with_depth import get_docs_with_depth
from api.process_with_word_and_tag import get_docs_with_word_and_tag

app = Flask(__name__)
env = init_modules()


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if not request.json or not ('file_name' in request.json and 'content' in request.json):
        return {'error': 'Invalid request body'}, 400

    return process_xml(env, request.json['content'], request.json['file_name'])


# Get document by tag
@app.route('/tags', methods=['GET'])
def get_by_tag():
    tag_name = request.args.get('tag_name')
    return get_docs_with_tag_name(env, tag_name)


# Get document by depth (doc>=depth)
@app.route('/depths', methods=['GET'])
def get_by_depth():
    depth = request.args.get('depth')
    return get_docs_with_depth(env, depth)


# Get document with <word> below <tag>
@app.route('/search', methods=['GET'])
def get_by_word_in_tag():
    tag_name = request.args.get('tag_name')
    word = request.args.get('word')

    # validate
    if not tag_name:
        return {'status': 0}, 400

    # search?tag_name=x&word=z
    return get_docs_with_word_and_tag(env, word, tag_name)


if __name__ == '__main__':
    app.run(debug=True)
