# encoding:utf-8
# portfolio efficiency assessment


import os

from collections import namedtuple
from bs4 import BeautifulSoup

FILE = os.path.expanduser('~/Downloads/report.htm')

Transaction = namedtuple('Transaction', 'date_time transaction_number order_number instrument direction quantity price commission')

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


if __name__ == '__main__':
    print('*'*125)

    with open(FILE, 'r') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'lxml')

        for row in soup.find_all('tr')[2:]:
            # print('='*125)
            # print(f'Length: {len(row)}')
            res = []
            for cell in row.find_all('td'):
                res.append(cell.get_text())
            # print(f'Length: {len(res)}', res)
            transaction = Transaction(date_time=res[0],
                                      transaction_number=res[1],
                                      order_number=res[2],
                                      instrument=res[3],
                                      direction=res[6],
                                      quantity=res[7],
                                      price=res[8],
                                      commission=res[15])
            print(transaction)
    # re_encode_file(FILE)
