import json
from flask import Flask, session, g, request, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    return app

app = create_app()

@app.before_request
def before_request():
    from . import db  # 循環importが起きるため一旦関数内でimport
    g.session = db.session
    token = request.headers.get('Authorization', None)
    if token:
        token = token.replace('Bearer ', '')
        from .models import User  # 循環importが起きるため一旦関数内でimport
        g.user = g.session.query(User).filter(User.token == token).one_or_none()
    else:
        g.user = None
    print("##### REQUEST #####")
    print(request)
    print(request.headers)
    if request.data != b'':
        print(json.dumps(json.loads(request.data.decode("utf-8")), ensure_ascii=False))
    print("####################")


@app.after_request
def after_request(response):
    g.session.commit()
    g.session.close()
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = -1
    print("##### RESPONSE #####")
    print(request)
    print(response)
    if response.headers['Content-Type'] == 'application/json' and response.data != b'':
        print(json.dumps(json.loads(response.data.decode("utf-8")), ensure_ascii=False))
    print("####################")
    return response