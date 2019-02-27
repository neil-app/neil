import random
from flask_restful import Resource
from flask import g, request, Response
from ..models import Image, User, History, Magazine
from ..schemas import UserSchema, CompantSchema, HistorySchema, MagazineSchema


class Profile(Resource):

    def get(self, user_id):
        response = dict()
        user = g.session.query(User).get(user_id)
        response["user"] = UserSchema().dump(user).data
        response["company"] = CompantSchema().dump(user.companies[0]).data if user.companies else None
        histories = g.session.query(History).filter(History.user_id == user_id).order_by(History.year)
        response["histories"] = HistorySchema().dump(histories, many=True).data
        magazines = g.session.query(Magazine).filter(Magazine.user_id == user_id).order_by(Magazine.rank)
        response["magazines"] = MagazineSchema().dump(magazines, many=True).data
        return {"profile": response}