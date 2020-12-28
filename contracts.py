# encoding:utf-8
# portfolio efficiency assessment


import os
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

import contracts_database_model as dbm
import config

from aux import get_transactions


mapper(dbm.Contract, dbm.contracts, column_prefix='_')


class PortfolioAnalyser():

    def __init__(self, path):
        self.db_path = os.path.join(path, 'portfolio_db.sqlite3')
        self.engine = create_engine('sqlite:///' + self.db_path)
        dbm.metadata.create_all(bind=self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def update(self, file):
        transactions = get_transactions(file)
        existed_contracts = self.session.query(dbm.Contract).all()
        print(f'existed_contracts: {len(existed_contracts)}')
        for contract in existed_contracts:
            print(contract)

        existed_transaction_numbers = [contract.transaction_number for contract in existed_contracts]

        for transaction in transactions:
            if transaction.transaction_number not in existed_transaction_numbers:
                contract = dbm.Contract(transaction)
                print(contract)
                self.session.add(contract)

        try:
            self.session.commit()
        except sqlalchemy.exc.SQLAlchemyError as err:
            print(err)
            self.session.rollback()
            print('Rolled back!')
        else:
            print('<<< Database updated! >>>')
        return None

    def __repr__(self):
        return f'Portfolio <({self.db_path})>'


if __name__ == '__main__':
    print('*'*125)

    config = config.Config()
    db_path = config.PORTFOLIO_DB_BASEDIR
    source_data_path = config.HTM_FILE_PATH

    analyser = PortfolioAnalyser(db_path)
    print(analyser)
    print('Updating...')
    analyser.update(source_data_path)
    print('Done!')
