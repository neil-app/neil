import uuid
import bcrypt
from enum import Enum
from datetime import datetime
from sqlalchemy_utils import ChoiceType
from sqlalchemy import Column, Integer, String, DateTime
from ..database import db
from .types.user_type import UserType


class User(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    token = Column(String(255), nullable=False)
    user_type = Column(ChoiceType(UserType, impl=Integer()), default=0, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    @classmethod
    def register(cls, name, email, password):
        salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
        hashpw = bcrypt.hashpw(
            str(password).encode('utf-8'), salt
        ).decode('utf-8')
        return cls(
            name=name,
            email=email,
            password=hashpw,
            token=str(uuid.uuid4()),
        )
