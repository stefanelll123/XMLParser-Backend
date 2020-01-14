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

    # check if file meets the condition
    if search_string in content:
        # get the position of the string
        position = content.find(search_string)

        # highlight the content in new var
        highlighted = content[:position] + ' style="background-color: yellow;" ' + content[position:]

        # return result
        return {'status': 0, 'content': highlighted}, 200

    # File found but condition was not satisfied
    return {'status': 0}, 204
