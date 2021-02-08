from model.account import Account
from model.transaction_history import TransactionHistory


def query_to_account(query_array):
    """
    Maps database query to an Account object
    :param query_array: db query to convert
    :return: Account object or None if not found
    """

    return Account(query_array[0], query_array[1], query_array[2]) if len(query_array) > 2 else None


def queries_to_histories(query_array):
    """
    Maps database queries to array of transaction histories
    :param query_array: db query to convert
    :return: array of transaction histories
    """
    result = []
    for tup in query_array:
        listed = list(tup)
        result.append(TransactionHistory(listed[0], listed[1], listed[2], listed[3], listed[4]))

    return result
