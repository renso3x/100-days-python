from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "somesecret"

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        if user == 'admin':
            return redirect(url_for("admin"))
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
    if "user" in session:
       return f"<h1>Hello Admin</h1> <a href='/logout' >Logout</a>" 
    #Redirect url to a function name
    # Pass url param when redirecting
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)