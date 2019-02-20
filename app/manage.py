from flask_script import Manager
from src.app import app
from src.tasks import CreateImagesTask
from src.models import *


manager = Manager(app)


@manager.command
def create_images():
    url = input("urlを入力してください >> ")
    tag_name = input("imageのtagのclass名を入力してください >> ")
    create_image_task = CreateImagesTask(url, tag_name)
    create_image_task.create()

if __name__ == "__main__":
    manager.run()
