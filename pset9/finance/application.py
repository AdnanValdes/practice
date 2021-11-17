import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from sql_helpers import buy_stock, create_transaction, enforce_tables, sell_stock

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure all tables exist at start up
enforce_tables(db)

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    _portfolio = db.execute("select symbol, shares from portfolio where user_id = :user_id", user_id=session['user_id'])

    cash = db.execute("select cash from users where id = :user_id", user_id=session['user_id'])[0]['cash']


    portfolio = []
    total = cash
    for stock in _portfolio:
        stock_data = lookup(stock['symbol'])

        data = {"symbol": stock_data['symbol'],
                        "name": stock_data["name"],
                        "shares":stock["shares"],
                        "price": stock_data["price"],
                        "total": stock_data["price"] * stock["shares"]
        }
        portfolio.append(data)
        total += data['total']
    return render_template("index.html", portfolio=portfolio, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = lookup(request.form.get("symbol"))
        shares = request.form.get("shares")

        # Check that symbol and shares are not empty
        if not symbol:
            return apology("must select a valid ticker!", 400)

        if not shares or not shares.isdigit() or int(shares) < 1:
            return apology("must select number of shares!", 400)

        # Confirm user has enough cash for transaction
        cash_available = db.execute("select cash from users where id = ?", session['user_id'])[0]['cash'] - (symbol['price'] * int(shares))

        if cash_available < 0:
            return apology("you don't have enough cash for that!", 400)

        create_transaction(db, "buy", symbol, shares)
        buy_stock(db, cash_available, symbol, shares)

        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    transactions = db.execute("""
        select symbol, operation, shares, price, timestamp from transactions
            where user_id = :user_id order by timestamp desc
    """,
    user_id=session['user_id'])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        ticker = request.form.get("symbol")
        price = lookup(ticker)

        if price == None or not ticker:
            return apology("invalid symbol", 400)

        return render_template("quote.html", price=price)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Arrive here by posting on registration page
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        # Check that username and password fields are submitted
        if not username or not password or not confirm:
            return apology("Invalid username or password", 400)

        # Check that password confirmation matches
        if password != confirm:
            return apology("Passwords do not match", 400)

        # Check that username is not already in database
        if len(db.execute("select username from users where username = ?", username)) == 1:
            return apology("Username taken", 400)

        # Insert user into database
        db.execute("insert into users (username, hash) values (:username, :hash )", username=username, hash=generate_password_hash(password))

        # Login the user and direct to index
        user_id = db.execute("select id from users where username = ?", username)
        session["user_id"] = user_id[0]["id"]

        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get('symbol')
        shares = request.form.get('shares')

        if not symbol:
            return apology("Select a valid symbol", 403)

        if not shares:
            return apology("Select valid number of stock to sell", 403)

        # Check that the user has stock
        # Placed here to run query only if basic form validation succeeds
        user_stock = db.execute("""
            select shares from portfolio
                where user_id = :user_id
                and symbol = :symbol
        """,
        user_id=session['user_id'],
        symbol=symbol)

        if not user_stock:
            return apology(f"You don't have any {symbol} stock available", 403)

        symbol = lookup(symbol)
        create_transaction(db, "sell", symbol, shares)
        sell_stock(db, symbol, shares)

        return redirect("/")

    # Show sell landing page for GET arrivals
    portfolio = db.execute("""
        select symbol from portfolio
            where user_id = :user_id
            """,
            user_id=session['user_id']
    )
    return render_template("sell.html", portfolio=portfolio)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
