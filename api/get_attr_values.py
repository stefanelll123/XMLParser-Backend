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
        xml_files = os.listdir(f'{PATH}')
        files_to_return = []

        for file in xml_files:
            if file.endswith('.xml'):
                f = open(f'{PATH}/{file}', "r")
                content = f.read()

                if contains(content, attr, value):
                    file_id = file.replace('.xml', '')
                    info = mongo.meta.find_one({'_id': ObjectId(file_id)}, {'_id': 0, 'content': 0})
                    files_to_return.append({
                        '_id': file_id, 
                        'file_name': info.get('file_name'),
                        'path': f'/highlight?attribute={attr}&value={value}&_id={file_id}'
                    })

        return {'status': 0, 'docs': files_to_return}, 200
    except Exception as e:
        print(e)
        return {'error': 'Could not process files'}, 500
