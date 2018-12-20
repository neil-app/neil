from flask_script import Manager
from src.app import app
from src.models import *

manager = Manager(app)


if __name__ == "__main__":
    manager.run()