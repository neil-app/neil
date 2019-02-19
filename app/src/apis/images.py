import random
from flask_restful import Resource
from flask import g, request, Response
from ..models import Image
from ..schemas import ImageSchema


class Images(Resource):

    def get(self):
        images = g.session.query(Image).all()
        images = random.sample(images, 10)
        return {'images': ImageSchema().dump(images, many=True).data}
