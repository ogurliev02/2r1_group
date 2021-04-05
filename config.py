import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'superSecretKey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or \
        'smtp.googlemail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or \
        587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or \
        1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or \
        'rflask9@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or \
        'password!234'
    ADMINS = ['rflask9@gmail.com']