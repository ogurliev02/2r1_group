from flask import render_template, current_app
from app.email import send_simple_mail

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_simple_mail('Reset your password!',
                    sender=current_app.config['ADMINS'][0],
                    to_who=[user.email],
                    text_body=render_template('email/reset_password.txt', user=user, token=token),
                    html_body=render_template('email/reset_password.html', user=user, token=token))