import os
from flask import Flask
from .config import config_by_name
def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)

    # Load config
    cfg = config_name or os.getenv("FLASK_ENV", "development")
    app.config.from_object(config_by_name[cfg])
    app.config.from_pyfile("../.env", silent=True)