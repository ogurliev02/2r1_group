from flask_mail import Message
from app import app, mail
from threading import Thread
from flask import render_template

def async_mail(f):
    def wrapper(*args, **kwargs):
        t = Thread(target=f, args=args, kwargs=kwargs)
        t.start()
    return wrapper

@async_mail
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)

def send_simple_mail(subject, sender, to_who, text_body="", html_body=""):
    msg = Message(subject=subject, sender=sender, recipients=to_who)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_simple_mail('Reset your password!',
                    sender=app.config['ADMINS'][0],
                    to_who=[user.email],
                    text_body=render_template('email/reset_password.txt', user=user, token=token),
                    html_body=render_template('email/reset_password.html', user=user, token=token))