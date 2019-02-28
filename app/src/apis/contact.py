import sendgrid
from flask_restful import Resource
from flask import request, current_app
from sendgrid.helpers.mail import *

class Contact(Resource):
    def get(self):
        return {'hello': 'world by get'}

    def post(self):
        data = request.get_json()
        sg = sendgrid.SendGridAPIClient(apikey="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")
        from_email = Email("ny.ldn.tko@gmail.com")
        subject = "Hello World from the SendGrid Python Library!"
        to_email = Email("ny.ldn.tko@gmail.com")
        content = Content("text/plain", "Hello, Email!")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return {'hello': 'world by post'}

    def put(self):
        return {'hello': 'world by put'}

    def delete(self):
        return {'hello': 'world by delete'}
