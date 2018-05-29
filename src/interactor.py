import inquirer
import pprint

from .blockchain import get_transaction_value, add_transaction, print_blockchain, owner, participants, manipulate, mine_block, get_balance, verify_chain, open_transactions

pp = pprint.PrettyPrinter(indent=2)

choices = [
    'Add new transaction value',
    'Output the blockchain blocks',
    'Output participants',
    'Mine block',
    'Manipulate the chain',
    'Quit'
]
questions = [
    inquirer.List('action', message='Please choose: ', choices=choices)
]


def init():
    waiting_for_input = True

    while waiting_for_input:
        action = inquirer.prompt(questions)
        user_choice = action['action']

        if user_choice == 'Add new transaction value':
            input_data = get_transaction_value()
            recipient, amount = input_data
            if not add_transaction(owner, recipient, amount):
                print('Amount not available')
        elif user_choice == 'Output the blockchain blocks':
            print_blockchain()
        elif user_choice == 'Output participants':
            pp.pprint(participants)
        elif user_choice == 'Mine block':
            if mine_block():
                open_transactions = []
        elif user_choice == 'Manipulate the chain':
            manipulate()
        elif user_choice == 'Quit':
            waiting_for_input = False
        else:
            print('Input was invalid, please pick a value from the options!')
            continue

        pp.pprint(get_balance('Ronny'))

        if not verify_chain():
            print('Blockchain not valid, exiting!')
            waiting_for_input = False
    else:
        print('Done!')
