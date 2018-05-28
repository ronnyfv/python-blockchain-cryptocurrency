block_chain = []
waiting_for_input = True

def get_last_block_chain_value():
    if len(block_chain) < 1:
        return None
    return block_chain[-1]


def add_value(transaction_amount, last_transaction=[0]):
    if last_transaction == None:
        last_transaction = [0]
    block_chain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount: '))


def get_user_choice():
    return input('Your choice: ')


def print_block_chain():
    print('-' * 10)

    for block in block_chain:
        print('Outputting block: ')
        print(block)
    else:
        print('-' * 10)


def verify_chain():
    is_valid = True

    for block_index in range(len(block_chain)):
        if block_index > 0 and block_chain[block_index][0] != block_chain[block_index - 1]:
            is_valid = False
            break

    return is_valid


while waiting_for_input:
    print('-' * 30)
    print('Please choose:')
    print('A: Add new transaction value')
    print('O: Output the blockchain blocks')
    print('H: Manipulate the chain')
    print('Q: Quit')
    print('')

    user_choice = get_user_choice()

    if user_choice == 'a' or user_choice == 'A':
        add_value(get_transaction_value(), get_last_block_chain_value())
    elif user_choice == 'o' or user_choice == 'O':
        print_block_chain()
    elif user_choice == 'h' or user_choice == 'H':
        if len(block_chain) >= 1:
            block_chain[0] = [2]
    elif user_choice == 'q' or user_choice == 'Q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
        continue
    
    if not verify_chain():
        print('Blockchain not valid, exiting!')
        waiting_for_input = False
else:
    print('Done!')
