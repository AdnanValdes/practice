import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""

    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "price": float(quote["latestPrice"]),
            "symbol": quote["symbol"]
        }
    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def enforce_tables(database):
    """Ensure all required tables are present in database"""

    database.execute("""
    create table if not exists users (
        id integer,
        username text not null,
        hash text not null,
        cash numeric not null default 10000.00,
        primary key(id)
        )
    """)

    database.execute("""
    create table if not exists transactions (
        user_id integer,
        timestamp text not null,
        symbol text not null,
        operation text not null,
        shares integer not null,
        price real not null,
        foreign key(user_id) references users(id)
        )
    """)

    database.execute("""
    create table if not exists portfolio (
        user_id integer,
        symbol text,
        shares integer,
        foreign key(user_id) references users(id),
        unique (user_id, symbol)
        )
    """)

    database.execute("""
        create unique index if not exists username on users (username)
    """)

    database.execute("""
        create index if not exists user_id on transactions (user_id)
    """)

    database.execute("""
        create index if not exists user_portfolio on portfolio (user_id)
    """)