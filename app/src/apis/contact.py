from flask_restful import Resource
from flask import request

class Contact(Resource):
    def get(self):
        return {'hello': 'world by get'}

    def post(self):
        data = request.get_json()
        print(data)
        return {'hello': 'world by post'}

    def put(self):
        return {'hello': 'world by put'}

    def delete(self):
        return {'hello': 'world by delete'}