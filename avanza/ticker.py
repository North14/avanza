#!/usr/bin/env python3

import logging
import pandas
import json

from .constants import constants, BASE_URL
from .base import Base

class Ticker:
    def __init__(self, orderbookId, option=None):
        self.orderbookId = orderbookId
        self.option = option

        if option == 'fund':
            self.data = Base()._request(f"{BASE_URL}{constants['paths']['FUND_PATH']}".format(self.orderbookId))
        elif option == 'certificate':
            self.data = Base()._request(f"{BASE_URL}{constants['paths']['CERTIFICATE_PATH']}".format(self.orderbookId))
        elif option == None:
            self.data = Base()._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(self.orderbookId))
        else:
            raise TypeError("Invalid option!")

    def __str__(self):
        """ Displays data in string format, use function data for dictionary """
        return json.dumps(self.data)

    @property
    def data(self):
        """ Returns full json of ticker call """
        return self.data

    @property
    def pandas(self):
        return pandas.io.json.build_table_schema(self.data)
