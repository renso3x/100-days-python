from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
@views.route("/<name>")
def home(name):
    print(name)
    return render_template("home.html", name=name)