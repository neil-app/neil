from flask_restful import Api
from . import app
from .apis import Health, Users, Login

api = Api(app)
api.add_resource(Login, '/api/auth/login')
api.add_resource(Health, '/api/health')
api.add_resource(Users, '/api/users')
