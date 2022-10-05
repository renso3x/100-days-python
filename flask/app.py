from distutils.debug import DEBUG
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content=['Romeo', "Joy", "Bob"])

# Accept url parameters in the link
@app.route('/<name>')
def user(name):
    return f"hello {name}"

@app.route('/admin')
def admin():
    #Redirect url to a function name
    # Pass url param when redirecting
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run(DEBUG=True)