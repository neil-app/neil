import os


class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres-user:password@localhost/local"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig