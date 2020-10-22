from flask_restful import Resource, reqparse

class SignIn(Resource) :
    def get(self):
        return {'message': 'Server Start'}