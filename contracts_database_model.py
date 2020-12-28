# encoding:utf-8
# database model for contracts application

from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime


from datetime import datetime


from aux import str_to_date
from aux import str_to_num
from aux import number_setter


metadata = MetaData()


contracts = Table('contracts', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('date', DateTime, nullable=False),
                   Column('transaction_number', Integer, unique=True, nullable=False),
                   Column('order_number', Integer, nullable=False),
                   Column('instrument', String, nullable=False),
                   Column('direction', String, nullable=False),
                   Column('quantity', Integer, nullable=False),
                   Column('price', Float, nullable=False),
                   Column('commission', Float, nullable=False),
                   )


class Contract():

    def __init__(self, transaction):
        self.date = transaction.date
        self.transaction_number = transaction.transaction_number
        self.order_number = transaction.order_number
        self.instrument = transaction.instrument
        self.direction = transaction.direction
        self.quantity = transaction.quantity
        self.price = transaction.price
        self.commission = transaction.commission


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, datetime):
            self._date = value
        elif isinstance(value, str):
            self._date = str_to_date(value)
        else:
            raise TypeError('Wrong type of date!')

    @property
    def transaction_number(self):
        return self._transaction_number

    @transaction_number.setter
    def transaction_number(self, value):
        if isinstance(value, int):
            self._transaction_number = value
        elif isinstance(value, str):
            self._transaction_number = int(value)
        else:
            raise TypeError('Wrong type of transaction number!')

    @property
    def order_number(self):
        return self._order_number

    @order_number.setter
    def order_number(self, value):
        if isinstance(value, int):
            self._order_number = value
        elif isinstance(value, str):
            self._order_number = int(value)
        else:
            raise TypeError('Wrong type of order number!')

    @property
    def instrument(self):
        return self._instrument

    @instrument.setter
    def instrument(self, value):
        if isinstance(value, str):
            self._instrument = value
        else:
            raise TypeError('Wrong type of instrument!')

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if value in ('Buy', 'Sell'):
            self._direction = value
        else:
            raise TypeError('Wrong direction!')

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, str):
            quantity = int(value)
            if quantity > 0:
                self._quantity = quantity
            else:
                raise ValueError('Non-positive quantity!')
        else:
            raise TypeError('Wrong quantity type!')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = number_setter(value)

    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value):
        self._commission = number_setter(value)

    def __repr__(self):
        return f'<Contract (Date: {self.date}, transaction: {self.transaction_number:>20}, {self.instrument:>5}, {self.direction:>4}, qty: {self.quantity:>2}, price: {self.price:>10})>'
