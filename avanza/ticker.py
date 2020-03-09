#!/usr/bin/env python3

import logging
import json

from .constants import constants, BASE_URL
from .base import Base

class Ticker:
    def __init__(self, orderbookId, option=None):
        self.option = option
        if option == 'fund':
            self.data = Base()._request(f"{BASE_URL}{constants['paths']['FUND_PATH']}".format(orderbookId))
        elif option == 'certificate':
            self.data = Base()._request(f"{BASE_URL}{constants['paths']['CERTIFICATE_PATH']}".format(orderbookId))
        elif not option or option == 'stock':
            self.data = Base()._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))
        else:
            raise TypeError("Invalid option!")

    def __str__(self):
        """ dumps data in string format, use function data for dictionary """
        return json.dumps(self.data)

    @property
    def info(self):
        """ Returns full json of ticker call """
        return self.data

    @property
    def buy_price(self):
        return self.data['buyPrice']

    @property
    def sell_price(self):
        return self.data['sellPrice']

    @property
    def last_price(self):
        return self.data['lastPrice']

    @property
    def highest_price(self):
        return self.data['highestPrice']

    @property
    def lowest_price(self):
        return self.data['lowestPrice']

    @property
    def symbol(self):
        return self.data['tickerSymbol']

    @property
    def currency(self):
        return self.data['currency']

    @property
    def isin(self):
        return self.data['isin']

    @property
    def marketlace(self):
        return self.data['marketPlace']

    @property
    def name(self):
        return self.data['name']

    @property
    def change(self):
        return self.data['change']

    @property
    def change_percent(self):
        return self.data['changePercent']

    @property
    def flag_code(self):
        return self.data['flagCode']

    @property
    def country(self):
        return self.data['country']

    @property
    def id(self):
        return self.data['id']

    @property
    def quote_updated(self):
        return self.data['quoteUpdated']

    @property
    def last_price_updated(self):
        return self.data['lastPriceUpdated']
