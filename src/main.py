import inquirer
import pprint

import src.blockchain

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
            input_data = blockchain.get_transaction_value()
            recipient, amount = input_data
            if not blockchain.add_transaction(blockchain.owner, recipient, amount):
                print('Amount not available')
        elif user_choice == 'Output the blockchain blocks':
            blockchain.print_blockchain()
        elif user_choice == 'Output participants':
            pp.pprint(blockchain.participants)
        elif user_choice == 'Mine block':
            if blockchain.mine_block():
                open_transactions = []
        elif user_choice == 'Manipulate the chain':
            blockchain.manipulate()
        elif user_choice == 'Quit':
            waiting_for_input = False
        else:
            print('Input was invalid, please pick a value from the options!')
            continue

        pp.pprint(blockchain.get_balance('Ronny'))

        if not blockchain.verify_chain():
            print('Blockchain not valid, exiting!')
            waiting_for_input = False
    else:
        print('Done!')


# content of test_sample.py
def adsadasdas(x):
    return x + 1


# init()
