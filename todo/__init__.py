import flask
from flask import request, jsonify
from .views import routes

def create_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    app.register_blueprint(routes.bp, url_prefix='/api/v1')
    # initalize data
    routes.todos.append({
        "id": 1,
        "title": "Watch CSSE6400 Lecture",
        "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
        "completed": True,
        "deadline_at": "2026-02-27T18:00:00",
        "created_at": "2026-02-20T14:00:00",
        "updated_at": "2026-02-20T14:00:00"
    })

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()