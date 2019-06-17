"""Entry point to evolving the neural network. Start here."""
from __future__ import print_function
import falcon
from falcon_cors import CORS
import pymongo
import json

cors = CORS(allow_all_origins= True,allow_credentials_all_origins=True,allow_all_headers=True,allow_all_methods=True,allow_origins_list=['http://localhost:63342','http://localhost:5000', 'http://210.107.233.174:5000'])

client = pymongo.MongoClient('mongodb://www.shehzikhan.ml:27017')
db=client['datavis']
collection=db['cellphone-specs']

class Distribution():
    def __init__(self):
        self.name='Data Field Distribution API'

    def on_get(self, req, resp):
        try:
            data = []
            if 'field' in req.params:
                field=req.params['field']
                for i, x in enumerate(collection.find().distinct(field)):
                    data.append({"name":x, "count":collection.find({field: x}).count()})
            else:
                data.append({"name": "Total", "count": collection.find().count()})

            result={
                'status': 'success',
                'data': data,
                'count':len(data),
                'message': "data object contains a list of JSON objects containing data field's name and count of matching records"
            }

            resp.body=json.dumps(result)

        except Exception as e:
            resp.body = json.dumps({'status': 'Error', 'message': e.message, 'details': str(e)})


class Query():
    def __init__(self):
        self.name = 'Query API'

    def on_get(self, req, resp):
        try:
            data = []
            query={}

            for param in req.params:
                query[param]=req.params[param]

            for x in collection.find(query):

                data.append(dict(x))

            result = {
                'status': 'success',
                'data': data,
                'count':len(data),
                'message': "data object contains a list of JSON objects containing data field's name and count of matching records"
            }

            resp.body = json.dumps(result)

        except Exception as e:
            resp.body = json.dumps({'status': 'Error', 'message': e.message, 'details': str(e)})






api = falcon.API(middleware=[cors.middleware])
api.add_route('/distribution', Distribution())
api.add_route('/query', Query())


