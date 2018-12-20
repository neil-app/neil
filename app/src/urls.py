from flask_restful import Api
from . import app
from .apis import Health

api = Api(app)
api.add_resource(Health, '/health')
