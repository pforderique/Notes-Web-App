from flask import Flask
from .config import MY_SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = MY_SECRET_KEY

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")

    return app