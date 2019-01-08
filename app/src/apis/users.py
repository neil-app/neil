from flask_restful import Resource
from flask import g, jsonify
from ..models import User

class Users(Resource):

    def get(self):
        user = g.session.query(User).get(1)
        return jsonify({'hello': user.name})

    def post(self):
        return {'hello': 'world by post'}

    def put(self):
        return {'hello': 'world by put'}

    def delete(self):
        return {'hello': 'world by delete'}
