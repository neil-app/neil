from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from sqlalchemy import Column, BigInteger, String, DateTime, Text
from ..database import db


class Image(db.Model):

    __tablename__ = 'images'

    id = Column(BigInteger, primary_key=True)
    title = Column(String(255), nullable=False)
    image_url = Column(Text, nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id'))
    user = relationship('User', backref='images')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
