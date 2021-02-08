import sys
import api
from threading import Thread
from time import sleep


session_end = False
current_account = None
atm_global_amount = 10000.0
clock_running = False
timer = 120
timer_thread = None


def count_down():
    global timer
    global clock_running
    while clock_running and timer > 0:
        timer -= 1
        sleep(1)
    if clock_running:
        print('\nLogged out due to inactivity.')
        logout()
        print('Type your command: ')
    else:
        sys.exit()


def reset_timer():
    global timer
    timer = 120


def start_timer():
    global clock_running
    global timer_thread
    reset_timer()
    clock_running = True
    timer_thread = Thread(target=count_down)
    timer_thread.start()


def stop_timer():
    global clock_running
    clock_running = False
    sleep(1)


def authorize(args):
    global current_account
    global clock_running
    if len(args) < 3:
        print('Invalid command. Please provide an account id and a pin.')
        return

    account = api.get_account_by_id(args[1])
    if len(account) < 1:
        print('Authorization failed.')
        return
    # check if pin number is correct
    if account[0].pin == args[2]:
        # set current session
        current_account = account[0]
        print(current_account.account_id, 'successfully authorized.')
        if clock_running:
            stop_timer()
        start_timer()
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
        stop_timer()


def process_withdraw(amount):
    global current_account
    global atm_global_amount
    current_account.withdraw(amount)
    api.create_transaction_history(current_account, -amount)
    print('Amount dispensed: $', amount)
    atm_global_amount -= amount

    if (current_account.balance < 0):
        print('You have been charged an overdraft fee of $5. Current balance:', current_account.balance)
        api.create_transaction_history(current_account, -5)
    else:
        print('Current balance:', current_account.balance)


def withdraw(args):
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
        process_withdraw(atm_global_amount)
    else:
        process_withdraw(amount)


def deposit(args):
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
        api.create_transaction_history(current_account, amount)
        print('Current balance:', current_account.balance)


def balance():
    global current_account
    if current_account is None:
        print('Authorization is required.')
        return
    print('Current balance:', current_account.balance)


def history():
    '''
    :return:
    '''
    global current_account
    if current_account is None:
        print('Authorization is required.')
        return

    histories = api.get_transaction_histories(current_account.account_id)

    if len(histories) < 1:
        print('No history found')
    else:
        for h in histories:
            print(h.date, h.time, h.amount, h.balance)


def atm():
    global session_end
    global current_account
    global timer
    # Initializes database
    api.initialize_db()
    # Main session
    while not session_end:
        command_input = list(input("Type your command: \n").split())
        if len(command_input) < 1:
            print('Please provide a command.')
        elif command_input[0] == 'end':
            api.close_db_connection()
            session_end = True
        elif command_input[0] == 'authorize':
            authorize(command_input)
        elif command_input[0] == 'withdraw':
            withdraw(command_input)
        elif command_input[0] == 'deposit':
            deposit(command_input)
        elif command_input[0] == 'balance':
            balance()
        elif command_input[0] == 'history':
            history()
        elif command_input[0] == 'logout':
            logout()
        elif command_input[0] == 'session':
            print('current account: ', current_account.account_id if current_account else 'None')
            print('current global amount: ', atm_global_amount)
            print('timer: ', timer)
        else:
            print('Unknown Command')

        reset_timer()
        print('\n')


# start the main thread
main_thread = Thread(target=atm)
main_thread.start()
