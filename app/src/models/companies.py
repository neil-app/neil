from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy import Column, BigInteger, String, DateTime, Text, Integer
from ..database import db


class Company(db.Model):

    __tablename__ = 'companies'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    rank = Column(Integer, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    user = relationship('User', backref='companies')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
