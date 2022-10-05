from datetime import timedelta
import os
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = "somesecret"
app.permanent_session_lifetime = timedelta(minutes=5)

#DB
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'users.sqlite3')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

db.init_app(app)
# Model
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        flash(f"Login successful.")

        # Match if the user exist
        found_user = users.query.filter_by(name=user).first() 

        if found_user:
            session["email"] = found_user.email
            session["user_id"] = found_user._id
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        if user == 'admin':
            session["admin"] = user
            return redirect(url_for("admin"))

        session["user"] = user
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")
    
# Accept url parameters in the link
@app.route('/<name>', methods=["POST", "GET"])
def user(name):
    email = None
    user_id = None
    if "user" in session:
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=name).first() 
            found_user.email = email
            session["user"] = found_user.name
            session["user_id"] = found_user._id

            email = session["email"]
            user_id = session["user_id"]
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session and "user_id" in session:
                email = session["email"]
                user_id = session["user_id"]
                
        return render_template("user.html", user=name, email=email, user_id=user_id)
        
    return redirect(url_for("login"))

@app.route('/admin')
def admin():
    if "admin" in session:
       return f"<h1>Hello Admin</h1> <a href='/logout' >Logout</a>" 
    elif "user" in session:
        return redirect(url_for("user", name=session["user"]))
    return redirect(url_for("login"))

@app.route('/user/<id>')
def view(id):
    if "user_id" in session:
        user = users.query.filter_by(_id=id).first()
        return f"User: {user.name}. Email: {user.email}"

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    flash("You have been logout.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)