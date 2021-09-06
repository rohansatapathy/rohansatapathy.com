from flask import Flask
from flask_flatpages import FlatPages

from config import Config


app = Flask(__name__)
app.config.from_object(Config)
pages = FlatPages(app)


from app import routes
