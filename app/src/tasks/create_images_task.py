import urllib
from ..database import db
from ..models import Image
import requests
from bs4 import BeautifulSoup


class CreateImagesTask:

    def __init__(self, url, tag_name):
        self.session = db.session
        self.url = url
        if tag_name[0] == ".":
            self.tag_name = tag_name
        else:
            self.tag_name = "." + tag_name

    def create(self):
        res = requests.get(self.url)
        html = res.content
        soup = BeautifulSoup(html, "html.parser")
        image_tags = soup.select(self.tag_name)
        title_tag = soup.title.string
        if not image_tags:
            print("{0}が存在しない".format(self.tag_name))
            return
        imgs = list()

        for img in image_tags:
            img = img.find("img") if img.find("img") else img
            if img.get("src"):
                src = urllib.parse.unquote(img['src'])
                imgs.append(src)

        image_urls = list()
        for img in imgs:
            for split_query in urllib.parse.urlparse(img).query.split('&'):
                key = split_query.split('=')[0]
                value = split_query.split('=')[1]
                if key == 'src':
                    image_urls.append(value)
            print(imgs)
            print(image_urls)



        for img_url in image_urls:
            image = Image(title="title_tag", image_url=img_url, user_id=8)
            self.session.add(image)
            self.session.commit()
