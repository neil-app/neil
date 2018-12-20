FROM python:3.6

RUN pip install uwsgi

COPY uwsgi.ini /etc/uwsgi/

# copy files
RUN mkdir /app
COPY requirements.txt /app/
COPY src /app/src
COPY manage.py /app/
WORKDIR /app
RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD tail -f /dev/null

ENV UWSGI_AUTORELOAD 0

EXPOSE 5000

CMD ["uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
