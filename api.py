import queryMapper
import database


def get_account_by_id(account_id):
    conn = database.get_connection()
    c = conn.cursor()
    c.execute("""SELECT * FROM account WHERE account_id = :id""", {'id': account_id})

    accounts = queryMapper.queries_to_accounts(c.fetchall())
    print(' accounts are here:', accounts)

    return accounts


def create_transaction_history(account, amount):
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



def get_transaction_histories(account_id):
    conn = database.get_connection()
    c = conn.cursor()
    c.execute("""SELECT * FROM transaction_history WHERE account_id = :id
    ORDER BY date DESC, time DESC""", {'id': account_id})

    histories = queryMapper.queries_to_histories(c.fetchall())
    return histories


def initialize_db():
    database.initialize_db()


def close_db_connection():
    database.close_connection()
