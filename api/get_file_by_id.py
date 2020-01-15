from util.constants import *

def get_file_by_id(env, file_id):
    try:
        with open(f"{PATH}/{file_id}.xml") as file:
            file_content = file.read()
    except OSError:
        return {'status': 0, 'error': 'File not found.'}, 404
    except:
        return {"error": "An error ocurred"}, 500
    return {"_id": file_id, "content": file_content}, 200
