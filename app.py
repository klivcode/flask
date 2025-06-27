# This is a simple Flask application that provides an API endpoint to get the current server time.
from flask import Flask,request

app = Flask(__name__)


# Routes
@app.route("/")
def home():
    return "<h1> This is a KlivCCode</h1>"

@app.route("/contact")
def contact():
    return "<h1>This is a contact Page</h1>"

@app.route("/about")
def about():
    return "<h1>This is an about Page</h1>"


@app.route("/Services")
def services():
    return "<h1>This is a Services Page</h1>"


@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "You send a data"
    else:
        return "Your are only viewing a form"



if __name__ == "__main__":
    app.run(debug=True)