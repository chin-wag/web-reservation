from flask import Flask
from mongoengine import connect


connect('restaurant')
app = Flask(__name__, static_url_path='/app/static')

from app import routes
