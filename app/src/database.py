from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import app

db = SQLAlchemy(app)
Migrate(app, db)
