import xml.etree.ElementTree as ET
from util.utils import *


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

        info = mongo.meta.insert_one(meta)
        file_id = info.inserted_id

        print(file_id)
        mongo.text.insert_one(text_info)
    except Exception as e:
        return {'error': 'Could not insert XML data'}, 500

    return {'status': 0}, 200
