import unittest
from model.account import Account


class TestAccountMethods(unittest.TestCase):
    def testWithdraw(self):
        testAccount = Account(123456789, 1234, 0)
        testAccount.withdraw(10)
        self.assertEqual(testAccount.balance, -10)

    def testWithdraw2(self):
        testAccount = Account(123455555, 3434, 30)
        testAccount.withdraw(30)
        self.assertEqual(testAccount.balance, 0)

    def testDeposit(self):
        testAccount = Account(123456489, 1234, -10)
        testAccount.deposit(30)
        self.assertEqual(testAccount.balance, 20)
