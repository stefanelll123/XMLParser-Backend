from util.utils import *


def get_docs_with_word_and_tag(env, word, tag_name):
    # Find docs in the database
    try:
        mongo = env.get('mongo')

        # query = dict()
        # query.add(tag_name, {'$exists': True})

        # searching word in tag
        cursor = mongo.text.find({tag_name: {'$exists': True}})

        docs = list(cursor)
        new_docs = list()

        if word:
            for doc in docs:
                for property in doc:
                    for text in doc[property]:
                        if word in text:
                            new_docs.append({"file_name": doc.filename})

            return {'status': 0, 'docs': new_docs}, 200
        else:
            return {'status': 0, 'docs': docs}, 200
    except:
        return {'error': 'Database connection failed!'}, 500
