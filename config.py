import os
from sqlalchemy import create_engine
import urllib
class Config(object):
    SECRET_KEY='clave nueva'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:burbu@localhost/bdidgs802'
    SQLALCHEMY_TRACK_MODIFICATIONS = False