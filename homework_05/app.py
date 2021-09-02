from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', endpoint='index')
def intro_func():
    return render_template('index.html')


@app.route('/about/', endpoint='about')
def get_details():
    return render_template('about.html')
