from flask_restful import Resource
from flask import g, jsonify, request, Response
from ..models import User


class Users(Resource):

    def get(self):
        user = g.session.query(User).get(1)
        return jsonify({'hello': user.name})

    def post(self):
        data = request.get_json()
        if 'application/json' not in request.headers['Content-Type']:
            return jsonify({'message': 'リクエストが不正です'}), 400
        elif not (data.get('name') and data.get('email') and data.get('password')):
            return jsonify({'message': 'dataが不正です'}), 401
        user = User.register(data.get('name'), data.get('email'), data.get('password'))
        g.session.add(user)
        g.session.commit()
        return Response()

    def put(self):
        return {'hello': 'world by put'}
