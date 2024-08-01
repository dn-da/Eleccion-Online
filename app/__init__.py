import logging

from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 

import logging
from app.config import Config

from dotenv import load_dotenv
import os


load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config.from_object(Config)
    ma.init_app(app)
    logging.basicConfig(level=logging.INFO)

    db.init_app(app)

    from app.routes.routes import home_bp
    app.register_blueprint(home_bp)

    return app