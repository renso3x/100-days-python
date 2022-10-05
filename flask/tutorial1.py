from re import I
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

# Accept url parameters in the link
@app.route('/<name>')
def user(name):
    return f"hello {name}"

@app.route('/admin')
def admin():
    #Redirect url to a function name
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()