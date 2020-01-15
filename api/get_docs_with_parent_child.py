import xml.etree.ElementTree as ET

def get_docs_with_parent_child(env, parent, child):
    mongo = env.get('mongo')

    try:
        resulted_docs = list()

        cursor = mongo.meta.find()
        docs = list(cursor)

        for doc in docs:
            root = ET.fromstring(doc.get("content"))
            elements = root.findall(f".//{parent}/{child}")

            if len(elements):
                resulted_docs.append({
                    "_id": str(doc.get('_id')),
                    "file_name": doc.get('file_name'),
                    "path": f"/files?file_id={doc.get('_id')}"
                })

    except:
        return {"error": "An error ocurred"}, 500

    return {"docs": resulted_docs}, 200
