"""Entry point to evolving the neural network. Start here."""
from __future__ import print_function
import falcon
from falcon_cors import CORS

cors = CORS(allow_all_origins= True,allow_credentials_all_origins=True,allow_all_headers=True,allow_all_methods=True,allow_origins_list=['http://localhost:63342','http://localhost:5000', 'http://210.107.233.174:5000'])

class Main():
    def __init__(self):
        pass

    def on_get(self, req, resp):
            resp.body="Hello"

api = falcon.API(middleware=[cors.middleware])
api.add_route('/', Main())

