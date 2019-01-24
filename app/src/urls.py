import json
from flask import make_response
from flask_restful import Api
from . import app
from .apis import Health, Users, UsersUserId

api = Api(app)


@api.representation('application/json')
def output_json(data, code, headers):
    resp = make_response(json.dumps(data, ensure_ascii=False), code)
    resp.headers.extend(headers)
    return resp

api.add_resource(Health, '/api/health')
api.add_resource(Users, '/api/users')
api.add_resource(UsersUserId, '/api/users/<int:user_id>')
