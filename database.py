import sqlite3
from queryMapper import query_to_account
from model.account import Account

connection = None


# creates connection to the database
def get_connection():
    """
    Fetches current database connection. If there isn't one, create one
    :return: Currently open database connection
    """
    global connection
    if connection is None:
        connection = sqlite3.connect('atm.db')

    return connection


# closes connection to the database
def close_connection():
    """
    Closes currently open database connection
    :return:
    """
    connection.close()


# initializes account data
def initialize_db():
    """
    Initializes tables and default entries in the database if it doesn't already exist.
    :return:
    """
    conn = get_connection()
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


