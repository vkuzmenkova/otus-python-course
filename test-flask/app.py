from flask import Flask, request, redirect
# from werkzeug.debug import DebuggedApplication

from views.movies import movies_app

flask_app = Flask(__name__)
# flask_app.wsgi_app = DebuggedApplication(flask_app.wsgi_app, evalex=True)

flask_app.register_blueprint(movies_app, url_prefix='/movies')


@flask_app.route('/')
def hello_func():
    name = request.args.get("name", "friend!")
    print(flask_app)
    return f"Hello, {name}"

