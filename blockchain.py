genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
waiting_for_input = True
open_transactions = []
owner = 'Ronny'
participants = set()


def hash_block(block):
    temporary_hash = [block[key] for key in block]
    return '-'.join(str(temporary_hash))


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(sender, recipient, amount=0.0):
    """ Append a new value as well

    Arguments:
        sender {string} -- the sender of the coins
        recipient {string} -- the receiver of the coins

    Keyword Arguments:
        amount {float} -- the amount of coins sent with transaction (default: {0.0})
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    last_block = blockchain[-1]

    block = {
        'previous_hash': hash_block(last_block),
        'index': len(blockchain),
        'transactions': open_transactions
    }

    blockchain.append(block)
    return True


def get_transaction_value():
    """[summary]

    Returns:
        [type] -- [description]
    """
    input_recipient = input('Enter the recipient of the transaction: ')
    input_amount = float(input('Your transaction amount: '))
    return (input_recipient, input_amount)


def get_user_choice():
    return input('Your choice: ')


def print_blockchain():
    print('-' * 10)
    print('Outputting block: ' + str(blockchain))
    print('Outputting transactions: ' + str(open_transactions))
    print('-' * 10)


def verify_chain():
    """ Verify the current blockchain and return a Boolean with the validation status

    Returns:
        [Boolean] -- validation status
    """

    for (index, block) in enumerate(blockchain):
        if index > 0 and block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False

    return True


while waiting_for_input:
    print('-' * 30)
    print('Please choose:')
    print('A: Add new transaction value')
    print('O: Output the blockchain blocks')
    print('P: Output participants')
    print('M: Mine block')
    print('H: Manipulate the chain')
    print('Q: Quit')
    print('')

    user_choice = get_user_choice()

    if user_choice == 'a' or user_choice == 'A':
        input_data = get_transaction_value()
        recipient, amount = input_data
        add_transaction(owner, recipient, amount)
    elif user_choice == 'o' or user_choice == 'O':
        print_blockchain()
    elif user_choice == 'p' or user_choice == 'P':
        print(participants)
    elif user_choice == 'm' or user_choice == 'M':
        if mine_block():
            open_transactions = []
    elif user_choice == 'h' or user_choice == 'H':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'q' or user_choice == 'Q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the options!')
        continue

    if not verify_chain():
        print('Blockchain not valid, exiting!')
        waiting_for_input = False
else:
    print('Done!')
