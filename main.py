import argparse
from model import transaction_model, user_model, balance_model


def get_balance_list():
    balance_list = balance_model.get_balance_list()
    for balance in balance_list:
        print(balance)


def settle_balance():
    user_ids_input = input("Enter comma separated payee_id and payer_id:  ")
    payee_id, payer_id = user_ids_input.split(",")

    balance_model.settle_balance(payer_id, payee_id)


def get_all_transactions():
    transactions = transaction_model.get_all_transactions()
    for transaction in transactions:
        print(transaction)


def get_user_transaction():
    user_id = input("Enter user id: ")

    transactions = transaction_model.get_user_transaction(user_id)
    for transaction in transactions:
        print(transaction)


def add_transaction():
    payee_id = input("Enter payee id: ")
    amount_input = input("Enter amount: ")
    amount = float(amount_input)

    payer_ids_input = input("Enter comma separated payer ids: ")
    payer_ids = [i for i in payer_ids_input.split(",")]

    split_type = input("Enter split type (Equal|Absolute|Percentage): ")

    if split_type != "Equal":
        split_amount_input = input("Enter comma separated split amount detail: ")
        split_amount_list = [float(i) for i in split_amount_input.split(",")]
        transaction_model.add_transaction(payee_id, payer_ids, amount, split_type, split_amount_list)

    else:
        transaction_model.add_transaction(payee_id, payer_ids, amount, split_type)


def get_users_list():
    users_list = user_model.get_users_list()
    for user in users_list:
        print(user)


def add_user():
    user_name = input("Enter name of the user: ")
    user_phone = input("Enter phone number of the user: ")
    user_model.add_user(user_name, user_phone)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Splitwise Project')
    parser.add_argument('--choice', help='Feature', choices=['add_user', 'get_users_list', 'add_transaction',
                                                             'get_user_transaction', 'get_all_transactions',
                                                             'settle_balance', 'get_balance_list'], required=True)

    args = parser.parse_args()
    choice = args.choice

    if choice == "add_user":
        add_user()
    elif choice == "get_users_list":
        get_users_list()
    elif choice == "add_transaction":
        add_transaction()
    elif choice == "get_user_transaction":
        get_user_transaction()
    elif choice == "get_all_transactions":
        get_all_transactions()
    elif choice == "settle_balance":
        settle_balance()
    elif choice == "get_balance_list":
        get_balance_list()
    else:
        print("Invalid choice!!")
