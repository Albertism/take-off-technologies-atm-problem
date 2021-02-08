import sqlite3
from queryMapper import queries_to_accounts
from model.account import Account


# creates connection to the database
def create_connection():
    conn = sqlite3.connect('atm.db')

    return conn


# closes connection to the database
def close_connection(conn):
    conn.close()


# initializes account data
def initialize_db(conn):
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS account")
    c.execute("DROP TABLE IF EXISTS transaction_history")
    c.execute("""SELECT name from sqlite_master WHERE type = 'table' AND name = 'account'""")
    # if tables are not initialized, create tables and initialize entries
    if (c.fetchone() == None):
        c.execute("""CREATE TABLE IF NOT EXISTS account(
            account_id TEXT PRIMARY KEY,
            pin TEXT,
            balance FLOAT
        )""")

        c.execute("""CREATE TABLE IF NOT EXISTS transaction_history(
            account_id TEXT,
            date TEXT,
            time TEXT,
            amount FLOAT,
            balance FLOAT,
            FOREIGN KEY(account_id) REFERENCES account(account_id)
        )""")

        c.execute("""INSERT INTO account VALUES('2859459814','7386',10.24)""")
        c.execute("""INSERT INTO account VALUES('1434597300','4557',90000.55)""")
        c.execute("""INSERT INTO account VALUES('7089382418','0075',0.00)""")
    else:
        return

