from model.account import Account
import api
import database

session_end = False
current_account = None
atm_global_amount = 10000.0


def authorize(args, conn):
    global current_account
    if len(args) < 3:
        print('Invalid command. Please provide an account id and a pin.')
        return

    account = api.get_account_by_id(args[1], conn)
    if len(account) < 1:
        print('Authorization failed.')
        return
    # check if pin number is correct
    if account[0].pin == args[2]:
        # set current session
        current_account = account[0]
        print(current_account.account_id, 'successfully authorized.')
        return
    else:
        print('Authorization failed.')
        return


def logout():
    global current_account
    if current_account is None:
        print('No account is currently authorized.')
        return
    else:
        print('Account', current_account.account_id, 'logged out.')
        current_account = None


def process_withdraw(amount, conn):
    global current_account
    global atm_global_amount
    current_account.withdraw(amount)
    api.create_transaction_history(current_account, -amount, conn)
    print('Amount dispensed: $', amount)
    atm_global_amount -= amount

    if (current_account.balance < 0):
        print('You have been charged an overdraft fee of $5. Current balance:', current_account.balance)
        api.create_transaction_history(current_account, -5, conn)
    else:
        print('Current balance:', current_account.balance)


def withdraw(args, conn):
    global current_account
    global atm_global_amount
    if current_account is None:
        print('Authorization is required.')
        return
    if len(args) < 2:
        print('Please provide withdrawal amount.')
        return
    amount = float(args[1])
    if current_account.balance < 0:
        print('Your account is overdrawn! You may not make withdrawals at this time.')
        return
    if atm_global_amount == 0:
        print('Unable to process your withdrawal at this time.')
        return
    if amount > atm_global_amount:
        print('Unable to dispense full amount requested at this time.')
        process_withdraw(atm_global_amount, conn)
    else:
        process_withdraw(amount, conn)


def deposit(args, conn):
    global current_account
    if current_account is None:
        print('Authorization is required.')
        return
    if len(args) < 2:
        print('Invalid command. Please provide a deposit amount.')
        return
    else:
        amount = float(args[1])
        if amount < 0:
            print('Invalid deposit amount. Please provide positive amount.')
            return
        current_account.deposit(amount)
        api.create_transaction_history(current_account, amount, conn)
        print('Current balance:', current_account.balance)


def balance():
    global current_account
    if current_account is None:
        print('Authorization is required.')
        return
    print('Current balance:', current_account.balance)


def history(conn):
    global current_account
    if current_account is None:
        print('Authorization is required.')
        return

    histories = api.get_transaction_histories(current_account.account_id, conn)

    if len(histories) < 1:
        print('No history found')
    else:
        for h in histories:
            print(h.date, h.time, h.amount, h.balance)


# Establish db connection and initialize
conn = database.create_connection()
database.initialize_db(conn)
# Main session
while not session_end:
    command_input = list(input("Type your command: ").split())
    if len(command_input) < 1:
        print('Please provide a command.')
    elif command_input[0] == 'end':
        database.close_connection()
        session_end = True
    elif command_input[0] == 'authorize':
        authorize(command_input, conn)
    elif command_input[0] == 'withdraw':
        withdraw(command_input, conn)
    elif command_input[0] == 'deposit':
        deposit(command_input, conn)
    elif command_input[0] == 'balance':
        balance()
    elif command_input[0] == 'history':
        history(conn)
    elif command_input[0] == 'logout':
        logout()
    elif command_input[0] == 'session':
        print('current account: ', current_account.account_id if current_account else 'None')
        print('current global amount: ', atm_global_amount)
    else:
        print('Unknown Command')

    print('\n')
