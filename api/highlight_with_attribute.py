from util.constants import PATH


def highlight_doc_with_attribute(file_id, attribute, value):
    # create the search string [attribute="value"]
    search_string = f'{attribute}="{value}"'

    # read file
    try:
        file = open(f'{PATH}/{file_id}.xml', 'r')
        content = file.read()
    except OSError:
        return {'status': 0, 'error': 'File not found.'}, 404

    # if file meets the condition
    if search_string in content:
        # replace all
        highlighted = content.replace(search_string, f'style="background-color: yellow;" {search_string}')

        # return result
        return {'status': 0, 'content': highlighted}, 200

    # file found but condition not satisfied
    return {'status': 0}, 204


