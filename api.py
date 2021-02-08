import queryMapper


def get_account_by_id(account_id, conn):
    c = conn.cursor()
    c.execute("""SELECT * FROM account WHERE account_id = :id""", {'id': account_id})

    return queryMapper.queries_to_accounts(c.fetchall())
