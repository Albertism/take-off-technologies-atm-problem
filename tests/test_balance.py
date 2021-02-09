import unittest
from unittest import mock
from unittest.mock import patch
from main import balance


class TestAccountMethods(unittest.TestCase):
    @patch('builtins.print')
    def testBalance(self, mocked_print):
        with mock.patch('main.current_account', None):
            balance()
        print('mock calls')
        print(mocked_print.mock_calls)