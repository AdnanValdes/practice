import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        if "delete" in request.form:
            db.execute("delete from birthdays where id = ?", request.form.get("delete"))

        elif "name" in request.form:
            name = request.form.get("name").capitalize()
            birthday = request.form.get("birthday")
            month = birthday[5:7]
            day = birthday[-2:]
            db.execute(
                "insert into birthdays (name, month, day) values (:name, :month, :day)",
                name=name,
                month=month,
                day=day,
            )
        return redirect("/")

    else:
        rows = db.execute("select * from birthdays")
        # TODO: Display the entries in the database on index.html

        return render_template("index.html", rows=rows)
