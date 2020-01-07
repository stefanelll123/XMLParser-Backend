from util.utils import *


def get_docs_with_tag_name(env, tag_name):
    # Find docs in the database
    try:
        mongo = env.get('mongo')

        # searching by tag_name and converting cursor to list
        docs = list(mongo.meta.find({'attributes': {'$eq': tag_name}}, {'_id': 0}))

        print(docs)

        return {'status': 0, 'docs': docs}, 200
    except FileNotFoundError:
        return {'error': 'Not found'}, 404
