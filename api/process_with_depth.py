from util.utils import *


def get_docs_with_depth(env, depth):
    # Find docs in the database
    try:
        mongo = env.get('mongo')

        # searching by tag_name and converting cursor to list
        docs = list(mongo.meta.find({'max_depth': {'$gte': int(depth)}}, {'file_name': 1, '_id': 1}))

        new_docs = list()
        for doc in docs:
            new_docs.append({"_id": str(doc.get("_id")), "file_name": doc.get("file_name")})

        return {'status': 0, 'docs': new_docs}, 200
    except:
        return {'error': 'Database connection failed!'}, 500
