from util.constants import *
from bson.objectid import ObjectId

def get_file_by_id(env, file_id):
    try:
        mongo = env.get('mongo')

        file = mongo.meta.find_one({'_id': ObjectId(file_id)})
    
        content = file.get('content')
        content = content.replace('<', '&lt;')
        content = content.replace('>', '&gt;')  

        return {
            "_id": file_id, 
            "content": content
        }, 200
    except Exception as e:
        print(e)
        return {"error": "An error ocurred"}, 500
