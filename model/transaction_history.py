class TransactionHistory:
    def __init__(self, account_id, date, time, amount, balance):
        self.account_id = account_id
        self.date = date
        self.time = time
        self.amount = float(amount)
        self.balance = float(balance)

