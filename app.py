from flask import Flask, request
from modules.init import init_modules
from api.get_docs_by_size import *

from api.process_xml import *
from api.process_with_tags import get_docs_with_tag_name
from api.process_with_depth import get_docs_with_depth
from api.process_with_word_and_tag import get_docs_with_word_and_tag
from api.highlight_with_attribute import highlight_doc_with_attribute, highlight_doc_with_tag
from api.get_attr_values import get_attr_values
from api.get_file_by_id import *

app = Flask(__name__)
env = init_modules()


# File processing
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


# Get documents by number of nodes
@app.route('/elements', methods=['GET'])
def get_by_size():
    size = request.args.get("size")
    return get_docs_by_size(env, size)


# Get documents by number of nodes
@app.route('/docs', methods=['GET'])
def get_by_attr_values():
    attr = request.args.get("attribute")
    value = request.args.get("value")

    return get_attr_values(env, attr, value)


# Highlight an existent XML file that contains a given attribute X with a given value Y
@app.route('/highlight', methods=['GET'])
def highlight_with_attribute():
    # load id and tag
    tag = request.args.get('tag')
    file_id = request.args.get('_id')

    # if tag is set
    if tag:
        return highlight_doc_with_tag(file_id, tag)

    # if tag is not set
    attribute = request.args.get('attribute')
    value = request.args.get('value')

    return highlight_doc_with_attribute(file_id, attribute, value)

@app.route('/files', methods=['GET'])
def get_file():
    file_id = request.args.get("file_id")

    return get_file_by_id(env, file_id)

# Run
if __name__ == '__main__':
    app.run(debug=True)
