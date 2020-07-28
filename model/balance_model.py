from database.create_db import session_factory
from database.manager.user import User
from database.manager.balance import Balance
from database.manager.transaction import Transaction
from sqlalchemy import and_


def settle_balance(payer_id, payee_id):
    session = session_factory()
    balance = session.query(Balance).filter(
        and_(Balance.payer_id == payee_id, Balance.payee_id == payer_id)).first()

    payee = session.query(User).filter(User.phone == payee_id).first()
    payee.balance += balance.amount
    payer = session.query(User).filter(User.phone == payer_id).first()
    payer.balance -= balance.amount

    new_transaction = Transaction(payer_id, payee_id, balance.amount)
    session.add(new_transaction)
    balance.amount = 0
    session.commit()


def get_balance_list():
    session = session_factory()
    balance_list = session.query(Balance).all()
    return balance_list
