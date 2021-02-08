from model.account import Account
import api
import database

session_end = False
global current_account
current_account = None


def authorize(args, conn):
    global current_account
    if len(args) < 3:
        print('Not enough argument. Please provide account id and pin')
        return

    account = api.get_account_by_id(args[1], conn)
    if len(account) < 1:
        print('Authorization failed')
        return
    # check if pin number is correct
    if account[0].pin == args[2]:
        # set current session
        current_account = account[0]
        print(current_account.account_id, 'successfully authorized.')
        return
    else:
        print('Authorization failed')
        return


def logout(conn):
    global current_account
    if current_account is None:
        print('No account is currently authorized')
        return
    else:
        print('Account', current_account.account_id, 'logged out.')
        current_account = None


def withdraw(amount, conn):
    global current_account
    if current_account is None:
        print('Authorization is required')
        return


# Establish db connection and initialize
conn = database.create_connection()
database.initialize_db(conn)
# Main session
while not session_end:
    command_input = list(input("Type your command: ").split())
    if command_input[0] == 'end':
        session_end = True
    elif command_input[0] == 'authorize':
        authorize(command_input, conn)
    elif command_input[0] == 'withdraw':
        session_end = False
    elif command_input[0] == 'deposit':
        session_end = False
    elif command_input[0] == 'balance':
        session_end = False
    elif command_input[0] == 'history':
        session_end = False
    elif command_input[0] == 'logout':
        logout(conn)
    elif command_input[0] == 'session':
        print('current account: ', current_account.account_id if current_account else 'None')
    else:
        print('Unknown Command')
