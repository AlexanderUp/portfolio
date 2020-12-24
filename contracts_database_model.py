# encoding:utf-8
# database model for contracts application


from sqlalchemy import Metadata
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

metadata = Metadata()

contracts = Table('contracts', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('transaction_number', Integer, unique=True, nullable=False),
                   Column('order_number', Integer, unique=True, nullable=False),
                   Column('instrument', String, nullable=False),
                   Column('direction', String, nullable=False),
                   Column('quantity', Integer, nullable=False),
                   Column('price', Float, nullable=False),
                   Column('commission', Float, nullable=False),
                   )

class Contracts():

    def __init__(selfj, transaction):
        self.transaction_number = transaction.transaction_number
        self.order_number = transaction.order_number
        self.instrument = transaction.instument
        self.direction = transaction.direction
        self.quantity = transaction.quantity
        self.price = transaction.price
        self.commission = transaction.commission

    @property
    def transaction_number(self):
        return self.__transaction_number

    @transaction_number.setter
    def transaction_number(self, value):
        if isinstance(value, int):
            self.__transaction_number = value
        elif isinstance(value, str):
            self.__transaction_numbe = int(value)
        else:
            raise TypeError('Wrong type of transaction number!')

    @property
    def order_number(self):
        return self.__order_number

    @order_number.setter
    def order_number(self, value):
        if isinstance(value, int):
            self.__order_number = value
        elif isinstance(value, str):
            self.__order_number = int(value)
        else:
            raise TypeError('Wrong type of order number!')


    def __repr__(self):
        return f'<Contract ({self.transaction_number},\
                            {self.instrument},\
                            {self.direction},\
                            {self.quantity},\
                            {self.price})>'
