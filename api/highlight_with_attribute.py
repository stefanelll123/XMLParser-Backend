import re
from util.constants import PATH
from bson.objectid import ObjectId


def highlight_doc_with_tag(env, file_id, tag):
    # create the search string [tag] and [/tag]
    search_string = [
        f'&lt;{tag}',
        f'&lt;/{tag}&gt;'
    ]

    # read file
    mongo = env.get('mongo')

    try:
        file = mongo.meta.find_one({'_id': ObjectId(file_id)})
        content = file.get('content')
    except Exception as e:
        print(e)
        return {'status': 0, 'error': 'File not found.'}, 404

    # try:
    #     file = open(f'{PATH}/{file_id}.xml', 'r')
    #     content = file.read()
    # except OSError:
    #     return {'status': 0, 'error': 'File not found.'}, 404

    # replace '<' with &lt; and '>' with '&gt;'
    # so the browser will not interpret as html
    content = content.replace('<', '&lt;')
    content = content.replace('>', '&gt;')

    # if file meets the condition
    if search_string[0] in content:
        # add the highlight as an html styled div
        highlighted = content.replace(search_string[0],
                                      f'<span style=\'color:red; font-weight: bold;\' >{search_string[0]}')
        highlighted = highlighted.replace(search_string[1], f'{search_string[1]}</span>')

        # return result
        return {'status': 0, 'content': highlighted}, 200

        # file found but condition not satisfied
    return {'status': 0}, 204


def highlight_doc_with_attribute(env, file_id, attribute, value):
    # create the search string [attribute="value"]
    search_string = f'{attribute}="{value}"'

    # read file
    mongo = env.get('mongo')

    try:
        file = mongo.meta.find_one({'_id': ObjectId(file_id)})
        content = file.get('content')
    except Exception as e:
        print(e)
        return {'status': 0, 'error': 'File not found.'}, 404
    # try:
    #     file = open(f'{PATH}/{file_id}.xml', 'r')
    #     content = file.read()
    # except OSError:
    #     return {'status': 0, 'error': 'File not found.'}, 404

    # replace '<' with &lt; and '>' with '&gt;'
    # so the browser will not interpret as html
    content = content.replace('<', '&lt;')
    content = content.replace('>', '&gt;')

    # if file meets the condition
    if search_string in content:
        # replace all
        highlighted = content.replace(search_string,
                                      f'<span style=\'color: red; font-weight:bold;\'>{search_string}</span>')

        # return result
        return {'status': 0, 'content': highlighted}, 200

    # file found but condition not satisfied
    return {'status': 0}, 204
