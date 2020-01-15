from util.utils import *


def get_docs_with_tag_name(env, tag_name):
    # Find docs in the database
    try:
        mongo = env.get('mongo')

        # searching by tag_name and converting cursor to list
        docs = list(mongo.meta.find({'attributes': {'$eq': tag_name}}, {'file_name': 1, '_id': 1}))
        new_docs = list()
        for doc in docs:
            file_id = str(doc.get("_id"))
            new_docs.append({
                "_id": file_id, 
                "file_name": doc.get("file_name"),
                'path': f'/files?file_id={file_id}'
            })

        return {'status': 0, 'docs': new_docs}, 200
    except:
        return {'error': 'Database connection failed!'}, 500
