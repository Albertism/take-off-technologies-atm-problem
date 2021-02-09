import queryMapper
import database


def get_account_by_id(account_id):
    """
    Fetches account that has matching account id
    :param account_id: requested account id
    :return: requested account if found
    """
    conn = database.get_connection()
    c = conn.cursor()
    c.execute("""SELECT * FROM account WHERE account_id = :id""", {'id': account_id})

    query_array = list(c.fetchone())
    account = queryMapper.query_to_account(query_array)

    return account


def create_transaction_history(account, amount):
    """
    Creates transaction history of requested account
    :param account: account requested
    :param amount: amount of transaction requested
    :return:
    """
    conn = database.get_connection()
    c = conn.cursor()
    c.execute("""INSERT INTO transaction_history VALUES(
        :account_id,
        DATE('now', 'localtime'),
        TIME('now', 'localtime'),
        :amount,
        :balance
    )""", {'account_id': account.account_id,
           'amount': amount,
           'balance': account.balance})
    conn.commit()


def update_account_balance(account):
    """
    Updates account with the new balance
    :param account: account to be updated
    :return:
    """
    conn = database.get_connection()
    c = conn.cursor()
    c.execute("""UPDATE account
        SET balance = :balance
        WHERE account_id = :account_id
    """, {'balance': account.balance, 'account_id': account.account_id})

    conn.commit()


def get_transaction_histories(account_id):
    """
    Get transaction histories of requested account
    :param account_id:
    :return: list of transaction histories
    """
    conn = database.get_connection()
    c = conn.cursor()
    c.execute("""SELECT * FROM transaction_history WHERE account_id = :id
    ORDER BY date DESC, time DESC""", {'id': account_id})

    histories = queryMapper.queries_to_histories(c.fetchall())
    return histories


def initialize_db():
    """
    Initializes tables and default entries in the database if it doesn't already exist.
    :return:
    """
    database.initialize_db()


def close_db_connection():
    """
    Closes current database connection
    :return:
    """
    database.close_connection()
