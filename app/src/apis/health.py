from flask_restful import Resource

class Health(Resource):
    def get(self):
        return {'hello': 'world by get'}

    def post(self):
        return {'hello': 'world by post'}

    def put(self):
        return {'hello': 'world by put'}

    def delete(self):
        return {'hello': 'world by delete'}