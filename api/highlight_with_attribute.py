import re
from util.constants import PATH


def highlight_doc_with_tag(file_id, tag):
    # create the search string [tag] and [/tag]
    search_string = [
        f'&lt;{tag}',
        f'&lt;/{tag}&gt;'
    ]

    # read file
    try:
        file = open(f'{PATH}/{file_id}.xml', 'r')
        content = file.read()
    except OSError:
        return {'status': 0, 'error': 'File not found.'}, 404

    # replace '<' with &lt; and '>' with '&gt;'
    # so the browser will not interpret as html
    content = content.replace('<', '&lt;')
    content = content.replace('>', '&gt;')

    # if file meets the condition
    if search_string[0] in content:
        # add the highlight as an html styled div
        highlighted = content.replace(search_string[0], f'<div style=\'background-color: yellow\' >{search_string[0]}')
        highlighted = highlighted.replace(search_string[1], f'{search_string[1]}</div>')

        # return result
        return {'status': 0, 'content': highlighted}, 200

        # file found but condition not satisfied
    return {'status': 0}, 204


def highlight_doc_with_attribute(file_id, attribute, value):
    # create the search string [attribute="value"]
    search_string = f'{attribute}="{value}"'

    # read file
    try:
        file = open(f'{PATH}/{file_id}.xml', 'r')
        content = file.read()
    except OSError:
        return {'status': 0, 'error': 'File not found.'}, 404

    # replace '<' with &lt; and '>' with '&gt;'
    # so the browser will not interpret as html
    content = content.replace('<', '&lt;')
    content = content.replace('>', '&gt;')

    # if file meets the condition
    if search_string in content:
        # replace all
        highlighted = content.replace(search_string, f'{search_string} style="background-color: yellow;" ')

        # return result
        return {'status': 0, 'content': highlighted}, 200

    # file found but condition not satisfied
    return {'status': 0}, 204
