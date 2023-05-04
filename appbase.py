# The appbase is used to store a persons login to a database that the site will create to the persons folder. entire page was done by noah.
from os import path
from flask import Flask
from configs import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from views import views

    app.register_blueprint(views, url_prefix='/')    

    from src.User import User

    create_database(app)

    return app

# note. the "website/" is the name of the primary folder this file is in. rename it to whatever folder name its in. Do this for all "website/" instances
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")