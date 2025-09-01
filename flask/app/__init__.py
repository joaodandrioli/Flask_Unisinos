from flask import Flask
from .Hello.routes import hello_bp
from .Name.routes import nome_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)

    app.register_blueprint(nome_bp)

    return app




