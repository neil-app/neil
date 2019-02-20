import urllib
import requests
from bs4 import BeautifulSoup
from ..database import db
from ..models import Image


class CreateImagesTask:

    def __init__(self, url, tag_name):
        self.session = db.session
        self.url = url
        self.tag_name = self.convert_tag_name(tag_name)
        self.res = requests.get(url)
        self.soup = self.scraping(self.res)

    def create(self):
        title = self.soup.title.string
        image_tags = self.soup.select(self.tag_name)
        if not image_tags:
            print("{0}が存在しない".format(self.tag_name))
            return
        for image_tag in image_tags:
            image_url = self.get_image_url(image_tag)
            if image_url:
                self.session.add(Image(title=title, image_url=image_url, user_id=8))
        self.session.commit()

    @staticmethod
    def get_image_url(image_tag):
        image_tag = image_tag.find("img") if image_tag.find("img") else image_tag
        if not image_tag.get("src"):
            return
        print(image_tag['src'])
        image_url = urllib.parse.unquote(image_tag['src'])
        split_query = urllib.parse.urlparse(image_url).query.split('&')
        if "src" in split_query:
            image_url = split_query.split('=')[1]
        return image_url

    @staticmethod
    def convert_tag_name(tag_name):
        if tag_name[0] != ".":
            return "." + tag_name
        return tag_name

    @staticmethod
    def scraping(res):
        if res.status_code < 300:
            return BeautifulSoup(res.content, "html.parser")