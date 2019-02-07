from flask_restful import Resource
from flask import g, request, Response
from ..models import User
from ..schemas import UserSchema


class Users(Resource):

    def get(self):
        users = g.session.query(User).filter(
            User.disabled.is_(False)
        ).all()
        return {'users': UserSchema().dump(users, many=True).data}


    def post(self):
        data = request.get_json()
        if 'application/json' not in request.headers['Content-Type']:
            return {'message': 'リクエストが不正です'}, 400
        elif not (data.get('name') and data.get('email') and data.get('password')):
            return {'message': 'dataが不正です'}, 401
        user = User.register(data.get('name'), data.get('email'), data.get('password'))
        g.session.add(user)
        g.session.commit()
        return Response()


class UsersUserId(Resource):

    def get(self, user_id):
        user = g.session.query(User).get(user_id)
        if not user:
            return {'message': 'user not found'}, 404
        return {'user': UserSchema().dump(user).data}

    def put(self, user_id):
        user = g.session.query(User).get(user_id)
        data = request.get_json()
        if 'application/json' not in request.headers['Content-Type']:
            return {'message': 'リクエストが不正です'}, 400
        elif not user:
            return {'message': 'user not found'}, 404
        elif not (data.get('name') and data.get('email')):
            return {'message': 'dataが不正です'}, 401
        user.name = data['name']
        user.email = data['email']
        return Response()

    def delete(self, user_id):
        user = g.session.query(User).get(user_id)
        if not user:
            return {'message': 'user not found'}, 404
        user.disabled = True
        return Response()
