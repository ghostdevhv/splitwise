from sqlalchemy import Column
from sqlalchemy import String, Float
from database.create_db import Base


class User(Base):
    __tablename__ = "user"

    name = Column("name", String(100), nullable=False)
    phone = Column("phone", String(50), nullable=False, primary_key=True)
    balance = Column("balance", Float)

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.balance = 0

    def __str__(self):
        return "name='%s', phone='%s', balance=%f" % (
            self.name,
            self.phone,
            self.balance,
        )
