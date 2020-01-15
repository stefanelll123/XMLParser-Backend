def get_docs_by_size(env, size):
    try:
        mongo = env.get('mongo')
        docs = mongo.meta.find({"size": int(size)}, {"file_name": 1, "_id": 1})
        new_docs = list()
        for doc in docs:
            file_id = str(doc.get("_id"))
            new_docs.append({
                "_id": file_id, 
                "file_name": doc.get("file_name"),
                'path': f'/files?file_id={file_id}'
            })
    except:
        return {'error': 'Could not query'}, 500

    return {'docs': new_docs}, 200