import unittest
import queryMapper
from model.account import Account
from model.transaction_history import TransactionHistory


class TestAccountMethods(unittest.TestCase):
    def testQueryToAccount(self):
        mock_query_array = [12345678, 3333, 0.0]
        expected = Account(12345678, 3333, 0.0)
        account = queryMapper.query_to_account(mock_query_array)

        assert isinstance(account, Account)
        self.assertEqual(account.account_id, expected.account_id)
        self.assertEqual(account.pin, expected.pin)
        self.assertEqual(account.balance, expected.balance)

    def testQueryToAccountIfInvalid(self):
        mock_query_array = [12345678, 3333]
        account = queryMapper.query_to_account(mock_query_array)

        self.assertEqual(account, None)

    def testQueriesToTransactionHistory(self):
        mock_query_array = [('00123456', '2021-02-08', '03:03:03', '20.0', '30.0')]
        expected = TransactionHistory('00123456', '2021-02-08', '03:03:03', '20.0', '30.0')
        histories = queryMapper.queries_to_histories(mock_query_array)

        self.assertEqual(len(histories), 1)
        assert isinstance(histories[0], TransactionHistory)
        self.assertEqual(histories[0].account_id, expected.account_id)
        self.assertEqual(histories[0].date, expected.date)
        self.assertEqual(histories[0].time, expected.time)
        self.assertEqual(histories[0].balance, expected.balance)
        self.assertEqual(histories[0].amount, expected.amount)

    def testQueriesToTransactionHistoryIfEmptyArray(self):
        mock_query_array = []
        histories = queryMapper.queries_to_histories(mock_query_array)

        self.assertEqual(len(histories), 0)