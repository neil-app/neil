import bcrypt
from flask_restful import Resource
from flask import g, jsonify, request, Response
from ..models import User
from ..schemas import UserSchema


class Login(Resource):

    def get(self):
        data = request.get_json()
        user = g.session.query(User).first()
        return jsonify({'users': UserSchema().dump(user).data, 'data': data})

    def post(self):
        data = request.get_json()
        if 'application/json' not in request.headers['Content-Type']:
            return jsonify({'message': 'リクエストが不正です'}), 400
        elif not (data.get('email') and data.get('password')):
            return jsonify({'message': 'dataが不正です'}), 401
        user = g.session.query(User).filter(User.email == data.get('email')).first()
        # [("ny.ldn.tko@gmail.com", "$2a$10$J8iFmKEzC1vrE/MVVKk0BukDNQQKSLo4mve1MtWtBwQnLnxfINpYe"), ("test@gmail.com", "$2a$10$k3YoukIfQ9293FRhlph8Q.i/SWdusQyu9AsR.83aMyue6zqmjAEHS")]
        password = data.get('psaaword')
        hashed_password = user.password
        if not bcrypt.checkpw(password.encode('utf8'), hashed_password.encode('utf8')):
            return jsonify({'mespzsage': 'おらんばい'}), 404
        return jsonify({'token': user.token})

    def put(self):
        return {'hello': 'world by put'}
