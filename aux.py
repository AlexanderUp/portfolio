# encoding:utf-8
# auxiliary functions for portfolio analyser application


import os


from datetime import datetime
from collections import namedtuple
from bs4 import BeautifulSoup


Transaction = namedtuple('Transaction', 'date transaction_number order_number instrument direction quantity price commission')


def re_encode_file(file, _initial_encoding='windows-1251', _result_encoding='utf-8'):
    path = os.path.dirname(file)
    file_name, file_ext = os.path.splitext(os.path.basename(file))
    out_file = file_name + '_re_encoded' + file_ext
    out_path = os.path.join(path, out_file)
    with open(file, 'r', encoding=_initial_encoding) as f_in:
        with open(out_path, 'w') as f_out:
            content = f_in.read()
            content.encode(_result_encoding)
            f_out.write(content)
    print('done')

def get_transactions(file):
    transactions = []
    with open(file, 'r') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')

        for row in soup.find_all('tr')[2:]:
            res = []
            for cell in row.find_all('td'):
                res.append(cell.get_text())
            if res[6] == 'Купля':
                res[6] = 'Buy'
            if res[6] == 'Продажа':
                res[6] = 'Sell'
            transaction = Transaction(date=res[0],
                                      transaction_number=res[1],
                                      order_number=res[2],
                                      instrument=res[3],
                                      direction=res[6],
                                      quantity=res[7],
                                      price=res[8],
                                      commission=res[15])
            transactions.append(transaction)
    return transactions

def str_to_date(str):
    d, t = str.split()
    day, month, year = d.split('.')
    hour, minute, second = t.split(':')
    date = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
    return date

def str_to_num(str):
    s = str.split(' ')
    return float(''.join(s))

def number_setter(value):
    price_ = 0
    if isinstance(value, str):
        price_ = str_to_num(value)
    elif isinstance(value, int):
        price_ = float(value)
    elif isinstance(value, float):
        price_ = value
    else:
        raise TypeError('Wrong type of price!')
    if price_ <= 0:
        raise ValueError('Price should be more than zero!')
    return price_


if __name__ == '__main__':
    print('*'*125)

    date = '17.12.2020 22:55:54'
    converted_date = str_to_date(date)
    print(converted_date)
    print(type(converted_date))

    price = '73 725.65'
    p = str_to_num(price)
    print(p)
    print(type(p))
