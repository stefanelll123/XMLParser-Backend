import glob
from util.constants import PATH


def highlight_doc_with_attribute(attribute, value):
    # get all xml files from PATH
    files = [f for f in glob.glob(PATH + "**/*.xml")]

    search_string = f'{attribute}="{value}"'
    print(search_string)

    for file in files:
        # read file
        file = open(file, 'r')
        content = file.read()

        # check if file meets the condition
        if search_string in content:
            # get the position of the string
            position = content.find(search_string)

            #
            highlighted = hash[:position] + ' style="background-color: yellow;" ' + hash[position:]

            return {'status': 0, 'file_name': str(file), content: highlighted}, 200

    return {'status': 0}, 204
