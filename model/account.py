class Account:
    def __init__(self, account_id, pin, balance):
        self.account_id = account_id
        self.pin = pin
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            self.balance -= amount
            self.balance -= 5.0
        else:
            self.balance -= amount
