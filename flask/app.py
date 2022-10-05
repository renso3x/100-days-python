from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "somesecret"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        if user == 'admin':
            session["admin"] = user
            return redirect(url_for("admin"))

        session["user"] = user
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")
    
# Accept url parameters in the link
@app.route('/<name>')
def user(name):
    if "user" in session:
        return f"hello {name} <a href='/logout' >Logout</a>"

    return redirect(url_for("login"))

@app.route('/admin')
def admin():
    if "admin" in session:
       return f"<h1>Hello Admin</h1> <a href='/logout' >Logout</a>" 
    elif "user" in session:
        return redirect(url_for("user", name=session["user"]))
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)