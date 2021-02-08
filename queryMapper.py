from model.account import Account

def queries_to_accounts(query_array):
    result = []
    for tup in query_array:
        listed = list(tup)
        if len(listed) < 3:
            raise ValueError("Not enough values in the tuple!", tup)
        else:
            result.append(Account(listed[0], listed[1], listed[2]))

    return result
