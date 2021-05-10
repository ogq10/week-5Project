import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager


from .site.routes import site
from .authentication.routes import auth




def create_app(config_class=Config):
    db = SQLAlchemy(app)
    login_manager = LoginManager(app)
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(site)
    app.register_blueprint(auth)

    root_db.init_app(app)
    migrate = Migrate(app, root_db)
    login_manager.init_app(app)

    return app

from may_blog import routes