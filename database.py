import sqlite3
from queryMapper import queries_to_accounts
from model.account import Account


def create_connection():
    conn = sqlite3.connect('atm.db')

    return conn


# initializes account data
def initialize_db(conn):
    c = conn.cursor()
    c.execute("""SELECT name from sqlite_master WHERE type = 'table' AND name = 'account'""")
    # if tables are not initialized, create tables and initialize entries
    if (c.fetchone() == None):
        c.execute("""CREATE TABLE IF NOT EXISTS account(
            account_id TEXT PRIMARY KEY,
            pin TEXT,
            balance FLOAT
        )""")

        c.execute("""INSERT INTO account VALUES('2859459814','7386',10.24)""")
        c.execute("""INSERT INTO account VALUES('1434597300','4557',90000.55)""")
        c.execute("""INSERT INTO account VALUES('7089382418','0075',0.00)""")
        conn.commit()
    else:
        return

