import pprint

pp = pprint.PrettyPrinter(indent=2)

MINING_REWARD = 10.0

genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Ronny'
participants = set()


def hash_block(block):
    temporary_hash = [block[key] for key in block]
    return hash(str(temporary_hash))


def clear_transactions():
    global open_transactions
    open_transactions = []


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]

    tx_sender.append(open_tx_sender)

    amount_sent = 0
    amount_received = 0

    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent


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

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True

    return False


def mine_block():
    last_block = blockchain[-1]
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)

    block = {
        'previous_hash': hash_block(last_block),
        'index': len(blockchain),
        'transactions': copied_transactions
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
    pp.pprint('-' * 10)
    pp.pprint('Outputting block: ')
    pp.pprint(blockchain)
    pp.pprint('Outputting transactions: ')
    pp.pprint(open_transactions)
    pp.pprint('-' * 10)


def verify_chain():
    """ Verify the current blockchain and
        return a Boolean with the validation status

    Returns:
        [Boolean] -- validation status
    """

    for (index, block) in enumerate(blockchain):
        if index > 0 and block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False

    return True


def verify_transaction(transaction):
    return get_balance(transaction['sender']) >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


def manipulate():
    if len(blockchain) >= 1:
        blockchain[0] = {
            'previous_hash': '',
            'index': 0,
            'transactions': [
                {'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}
            ]
        }


# Test function for module
def _test():
    pass


if __name__ == '__main__':
    _test()
