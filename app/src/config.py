import os


class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mysecretpassword1234@localhost/neil"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig