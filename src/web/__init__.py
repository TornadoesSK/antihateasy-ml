from flask import Flask

def create_app( config: dict = None):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config['SECRET_KEY']

    from .endpoints import endpoints

    app.register_blueprint(endpoints, url_prefix='/')
    return app
