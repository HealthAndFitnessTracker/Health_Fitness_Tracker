from flask import Flask
from views import views
from configs import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
