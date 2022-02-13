from flask import session

def buy_stock(database, cash, symbol, shares):
	""" Execute SQL statements to add stock into user's portfolio"""

	database.execute("""
        update users
            set cash = :cash
            where id = :user_id
    """,
    cash=cash,
    user_id=session['user_id']
    )

    # Add to portfolio
    # Uses SQLite3 "UPSERT"
    # https://www.sqlite.org/draft/lang_UPSERT.html
	database.execute("""
        insert into portfolio
            (user_id, symbol, shares)
            values
                (:user_id, :symbol, :shares)
            on conflict (user_id, symbol)
                do update set shares=shares+:shares
        """,
        user_id = session['user_id'],
        symbol=symbol['symbol'],
        shares=shares
    )

def create_transaction(database, operation, symbol, shares):
    database.execute("""
    insert into transactions
        (user_id, timestamp, symbol, operation, shares, price)
        values
            (:user_id, datetime('now'), :symbol, :operation, :shares, :price)""",
     symbol=symbol['symbol'],
     operation=operation,
     shares=shares,
     price=symbol['price'],
     user_id=session['user_id']
)

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

def sell_stock(database, symbol, shares):
	"""Execute SQL statements to remove stock from user's portfolio"""

	# Add cash to user's account
	database.execute("""
        update users
            set cash = cash + :cash
            where id = :user_id
    """,
    cash =(symbol['price'] * int(shares)),
    user_id=session['user_id']
    )
    # Remove stock from user's portfolio
	database.execute("""
        update portfolio
            set shares = shares - :shares
            where user_id = :user_id
            and symbol = :symbol
    """,
    shares=shares,
    user_id=session['user_id'],
    symbol=symbol['symbol'])
    # If user owns 0 stock, remove from stock from table
	database.execute("""
        delete from portfolio
            where user_id = :user_id
            and symbol = :symbol
            and shares = 0
    """,
    user_id=session['user_id'],
    symbol=symbol['symbol'])