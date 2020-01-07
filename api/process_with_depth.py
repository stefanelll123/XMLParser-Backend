from util.utils import *


def get_docs_with_depth(env, depth):
    # Find docs in the database
    try:
        mongo = env.get('mongo')

        # searching by tag_name and converting cursor to list
        docs = list(mongo.meta.find({'max_depth': {'$gte': int(depth)}}, {'content': 1, 'file_name': 1, '_id': 0}))

        print(docs)

        return {'status': 0, 'docs': docs}, 200
    except:
        return {'error': 'Database connection failed!'}, 500
