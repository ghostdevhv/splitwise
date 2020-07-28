from database.create_db import session_factory
from database.manager.user import User
from database.manager.transaction import Transaction
from database.manager.balance import Balance
from sqlalchemy import or_, and_


def add_transaction(payee_id, payer_ids, total_amount, split_type, split_amount_list=None):
    actual_amount_list = []
    if split_type == "Equal":
        actual_amount_list = [total_amount / (len(payer_ids))] * len(payer_ids)

    elif split_type == "Absolute":
        actual_amount_list = split_amount_list[:]

    elif split_type == "Percentage":
        for i in range(len(payer_ids)):
            actual_amount_list.append(split_amount_list[i] * total_amount / 100)

    session = session_factory()
    payee_amount = 0

    for index, payer_id in enumerate(payer_ids):
        if payer_id != payee_id:
            payee_amount += actual_amount_list[index]
            session.add(Transaction(payer_id, payee_id, actual_amount_list[index]))
            payer = session.query(User).filter(User.phone == payer_id).first()
            payer.balance -= actual_amount_list[index]

            balance_row = session.query(Balance).filter(
                and_(Balance.payer_id == payer_id, Balance.payee_id == payee_id)).first()
            if balance_row is None:
                new_row = Balance(payer_id, payee_id, actual_amount_list[index])
                session.add(new_row)
            else:
                balance_row.amount += actual_amount_list[index]

    payer = session.query(User).filter(User.phone == payee_id).first()
    payer.balance += payee_amount
    session.commit()


def get_all_transactions():
    session = session_factory()
    transactions = session.query(Transaction).all()
    return transactions


def get_user_transaction(user_id):
    session = session_factory()
    transactions = session.query(Transaction).filter(
        or_(Transaction.payer_id == user_id, Transaction.payee_id == user_id)).all()

    return transactions
