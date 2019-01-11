from flask_restful import Resource
from flask import g, jsonify, request
from ..models import User


class Users(Resource):

    def get(self):
        user = g.session.query(User).get(1)
        return jsonify({'hello': user.name})

    def post(self):
        data = request.get_json()
        user = User(name=data['name'], email=data['email'], password=data['password'])
        g.session.add(user)
        g.session.commit()

        return {'hello': 'world by post'}

    def put(self):
        return {'hello': 'world by put'}
