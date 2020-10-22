#from com_cheese_api.ext.db import config
from flask_restful import Resource, reqparse

class Recommend(Resource):
    def get(self):
        return {'message': 'Server Statrt'}
