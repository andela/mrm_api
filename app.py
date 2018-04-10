from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#local imports
from config import config

#initializing a db instance
db = SQLAlchemy()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    return app
