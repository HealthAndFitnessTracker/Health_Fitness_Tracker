from flask import Flask
from views import views
from configs import Config
from flask_sqlalchemy import SQLAlchemy
from appbase import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)