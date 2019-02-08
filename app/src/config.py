import os


class BaseConfig:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mysecretpassword1234@localhost:5432/neil"


class LocalDockerConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mysecretpassword1234@postgres-neil-db/neil"

config = {
    "local": "src.config.LocalConfig",
    "local-docker": "src.config.LocalDockerConfig",
}


def configure_app(application):
    config_name = os.getenv('FLASK_CONFIGURATION', 'local')
    application.config.from_object(config[config_name])
    application.config.from_pyfile('config.cfg', silent=True)
