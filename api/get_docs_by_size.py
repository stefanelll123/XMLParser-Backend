def get_docs_by_size(env, size):
    try:
        mongo = env.get('mongo')
        docs = mongo.meta.find({"size": int(size)}, {"file_name": 1, "_id": 0, "content": 1})
    except:
        return {'error': 'Could not query'}, 500

    return {'docs ': list(docs)}, 200
