from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {'username':'Bruno'}
    posts = [
        {'autor': {'username':'Maria'}, 'body': 'Olá da Maria'},
        {'autor': {'username':'Bruno'}, 'body': 'Olá!'}
    ]
    return render_template("index.html", user=user, posts=posts)