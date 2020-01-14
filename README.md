XML-Parser
===========

Requirements
------------

- Flask (`pip install flask`).
- Dotenv (`pip install python-dotenv`).
- Dotenv-CLI (`pip install dotenv-cli`).
- Mongo Client (`pip install pymongo`).
- DNS (`pip install dnspython`).


Installation
------------

You should create a new file `.env` which contains the following

    $ MONGO_URI="{mongo_connection_string}"

Running the Server
--------------------
    (cmd) dotenv run py app.py
    

API Helper
===========

    # Upload File
    -------------
    POST /upload_file 
    {
        content: [content],
        file_name: [file_name]
    }
    
    
    # Get document by tag
    ---------------------
    GET /tags?tag_name=[tag]
    
    
    # Get document by depth (doc>=depth)
    ------------------------------------
    GET /depths?depth=[depth]
    
    
    # Get documents by tag size
    GET /elements?size=[size]
    
    
    # Get document with <word> below <tag>
    GET /search?tag_name=[tag]&word=[word]
    