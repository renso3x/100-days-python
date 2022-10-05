from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")
    
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
    app.run(debug=True)