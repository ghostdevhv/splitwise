from sqlalchemy import Column
from sqlalchemy import Integer, String, Float
from database.create_db import Base


class Balance(Base):
    __tablename__ = "balance"

    id = Column(Integer, primary_key=True)
    payer_id = Column("id_1", String(50))
    payee_id = Column("id_2", String(50))
    amount = Column("amount", Float)

    def __init__(self, payer_id, payee_id, amount):
        self.payer_id = payer_id
        self.payee_id = payee_id
        self.amount = amount

    def __str__(self):
        return "%s owes %s %f amount of money" % (
            self.payer_id,
            self.payee_id,
            self.amount
        )
