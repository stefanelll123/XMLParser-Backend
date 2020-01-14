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