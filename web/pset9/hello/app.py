from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name") # Allows us to access key:values from URI
    return render_template("index.html", name=name) # The kwarg must be the same as the variable in the HTML document

@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.args.get("name", "world") # Second value is default parameter when no arguments are passed in URI
    name = request.form['name'] # Syntax for getting values from POST requests.
    return render_template("greet.html", name=name)