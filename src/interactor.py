import inquirer
import pprint

from .blockchain import (get_transaction_value,
                         add_transaction,
                         print_blockchain,
                         owner,
                         participants,
                         manipulate,
                         mine_block,
                         get_balance,
                         verify_chain,
                         open_transactions,
                         verify_transactions,
                         clear_transactions)

pp = pprint.PrettyPrinter(indent=2)

NEW_TRANSACTION = 'Add new transaction value'
MINE_BLOCK = 'Mine a new block'
OUTPUT_BLOCKCHAIN = 'Output the blockchain blocks'
OUTPUT_PARTICIPANTS = 'Output participants'
VALIDATE_TRANSACTIONS = 'Check transaction validity'
CHANGE_CHAIN = 'Manipulate the chain'
QUIT = 'Quit'

choices = [
    NEW_TRANSACTION,
    MINE_BLOCK,
    OUTPUT_BLOCKCHAIN,
    OUTPUT_PARTICIPANTS,
    VALIDATE_TRANSACTIONS,
    CHANGE_CHAIN,
    QUIT
]
questions = [
    inquirer.List('action', message='Please choose: ', choices=choices)
]


def init():
    waiting_for_input = True

    while waiting_for_input:
        action = inquirer.prompt(questions)
        user_choice = action['action']

        if user_choice == NEW_TRANSACTION:
            input_data = get_transaction_value()
            recipient, amount = input_data
            if not add_transaction(owner, recipient, amount):
                pp.pprint('Amount not available')
        elif user_choice == MINE_BLOCK:
            if mine_block():
                clear_transactions()
        elif user_choice == OUTPUT_BLOCKCHAIN:
            print_blockchain()
        elif user_choice == OUTPUT_PARTICIPANTS:
            pp.pprint(participants)
        elif user_choice == VALIDATE_TRANSACTIONS:
            if verify_transactions():
                pp.pprint('All transactions are valid')
            else:
                pp.pprint('There are invalid transactions')
        elif user_choice == CHANGE_CHAIN:
            manipulate()
        elif user_choice == QUIT:
            waiting_for_input = False

        pp.pprint(get_balance('Ronny'))

        if not verify_chain():
            pp.pprint('Blockchain not valid, exiting!')
            waiting_for_input = False
    else:
        pp.pprint('Done!')
