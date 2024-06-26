import os
from flask import Flask
from dotenv import load_dotenv
from . import home, signin, login, userMenu

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_mapping(
        SECRET_KEY = os.getenv('SECRET_KEY'),
        DATABASE_HOST = os.getenv('DATABASE_HOST'),
        DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD'),
        DATABASE_USER = os.getenv('DATABASE_USER'),
        DATABASE = os.getenv('BATABASE')
    )
    app.register_blueprint(home.bp)
    app.register_blueprint(signin.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(userMenu.bp)
    return app
