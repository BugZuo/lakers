from pymongo import Connection

from lakers import app

host = app.config.get('MONGO_HOST', 'localhost')
port = app.config.get('MONGO_PORT', 27017)

try:
    conn = Connection(host=host, port=port)
except:
    pass

test = conn['test']['test']