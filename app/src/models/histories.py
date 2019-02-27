from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy import Column, BigInteger, String, DateTime, Text, Integer
from ..database import db


class History(db.Model):

    __tablename__ = 'histories'

    id = Column(BigInteger, primary_key=True)
    year = Column(Integer, nullable=False)
    discription = Column(Text, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    user = relationship('User', backref='histories')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)