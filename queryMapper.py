from model.account import Account
from model.transaction_history import TransactionHistory


def queries_to_accounts(query_array):
    result = []
    for tup in query_array:
        listed = list(tup)
        if len(listed) < 3:
            raise ValueError("Not enough values in the tuple!", tup)
        else:
            result.append(Account(listed[0], listed[1], listed[2]))

    return result


def queries_to_histories(query_array):
    result = []
    for tup in query_array:
        listed = list(tup)
        result.append(TransactionHistory(listed[0], listed[1], listed[2], listed[3], listed[4]))

    return result
