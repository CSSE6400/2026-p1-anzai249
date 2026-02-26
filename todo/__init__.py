import flask
from flask import request, jsonify
from .views import routes

def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    app.register_blueprint(routes.bp, url_prefix='/api/v1')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()