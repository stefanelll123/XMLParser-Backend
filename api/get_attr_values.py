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
                    info = mongo.meta.find_one({'_id': ObjectId("5e1e300c3f31de83e5ed8bfa")}, {'_id': 0, 'content': 0})
                    files_to_return.append({'_id': file.replace('.xml', ''), 'file_name': info.get('file_name')})

        return {'status': 0, 'docs': files_to_return}, 200
    except Exception as e:
        print(e)
        return {'error': 'Could not process files'}, 500
