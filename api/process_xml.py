import xml.etree.ElementTree as ET

from util.utils import *
from util.constants import *


def process_xml(env, xml_string, file_name):
    # Parse the xml string
    root = ET.fromstring(xml_string)

    # Get XML file info
    info = get_info(root, xml_string, file_name)

    meta = info['meta']
    text_info = info['dictt']

    meta['content'] = xml_string

    # Insert data into the database
    try:
        mongo = env.get('mongo')

        mongo.meta.insert(meta)
        mongo.text.insert(text_info)

        with open(f'{PATH}/{file_name}', 'x') as xml_file:
            xml_file.write(xml_string)
    except OSError:
        return {'error": f"{file_name} already exists'}, 500
    except Exception as e:
        print(e)
        return {'error': 'Could not insert XML data'}, 500

    return {'status': 0}, 200

