from database.create_db import session_factory
from database.manager.user import User


def get_users_list():
    session = session_factory()
    users = session.query(User).all()
    return users


def add_user(name, phone):
    session = session_factory()
    new_user = User(name, phone)
    session.add(new_user)
    session.commit()
