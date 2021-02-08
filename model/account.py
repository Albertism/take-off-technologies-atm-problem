class Account:
    def __init__(self, account_id, pin, balance):
        self.account_id = account_id
        self.pin = pin
        self.balance = float(balance)

    def deposit(self, amount):
        """
        Sets new balance after depositing amount
        :param amount: amount to be deposited
        :return:
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Sets new balance after withdrawing amount.
        :param amount: amount to be withdrawn
        :return:
        """
        self.balance -= amount
