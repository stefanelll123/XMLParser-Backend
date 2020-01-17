import os
import xml.etree.ElementTree as ET

from util.constants import *
from bson.objectid import ObjectId

def contains(content, attr, value):
    root = ET.fromstring(content)
    result = root.findall(f".//*[@{attr}='{value}']")

    if result:
        return True

    return False


def get_attr_values(env, attr, value):
    try:
        mongo = env.get('mongo')
        xml_files = mongo.meta.find()
        files_to_return = []

        for file in xml_files:
            content = file.get('content')

            if contains(content, attr, value):
                file_id = str(file.get('_id'))
                files_to_return.append({
                    '_id': file_id, 
                    'file_name': file.get('file_name'),
                    'path': f'/highlight?_id={file_id}&attribute={attr}&value={value}'
                })

        return {'status': 0, 'docs': files_to_return}, 200
    except Exception as e:
        print(e)
        return {'error': 'Could not process files'}, 500
