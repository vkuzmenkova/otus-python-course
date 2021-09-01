from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest


MOVIES_LIST = {
    1: "Dune",
    2: "Hunger Games",
    3: "Harry Potter",
    4: "Friends: Reunion"
}

movies_app = Blueprint("movies_app", __name__)


@movies_app.route("/", endpoint='list')
def get_movies():
    return render_template("movies/list.html", movies=MOVIES_LIST)


@movies_app.route('/<int:item_id>', endpoint='about')
def get_item(item_id: int = 1):
    mov_name = MOVIES_LIST.get(item_id)
    if mov_name is None:
        raise NotFound(f"No movie with id={item_id}")
    return render_template("movies/about.html", mov_name=MOVIES_LIST[item_id],
                           mov_id=item_id)


@movies_app.route('/add', endpoint='add', methods=['GET', 'POST'])
def create_movie():
    if request.method == 'GET':
        return render_template('movies/add.html')
    movie_name = request.form.get("movie_name")
    if not movie_name:
        raise BadRequest

    movie_id = len(MOVIES_LIST)+1
    MOVIES_LIST[movie_id] = movie_name
    return redirect(
        url_for("movies_app.about", item_id=movie_id))
