#!/usr/bin/env python3

import logging
import json

from .constants import constants, BASE_URL
from .base import Base

class Ticker(Base):
    def __init__(self, orderbookId, instrument='stock', auth=False):
        """
        :type orderbookId: int
        :param orderbookId: id of instrument
        :type instrument: string
        :param instrument: type of instrument
        :type auth: boolean
        :param auth: auth=True for additional information from instrument
        """
        super().__init__()
        if instrument in ['fund', 'certificate', 'stock']:
            if auth:
                self.data = self._request(f"{BASE_URL}{constants['paths']['INSTRUMENT_PATH']}".format(instrument, orderbookId), auth=None)
            else:
                self.data = self._request(f"{BASE_URL}{constants['paths']['INSTRUMENT_PATH']}".format(instrument, orderbookId))
        else:
            raise TypeError("Invalid option!")

    def __str__(self):
        """ dumps data in string format, use function data for dictionary """
        return json.dumps(self.data)

    @property
    def info(self):
        """
        Return full json of ticker call
        
        :rtype: string
        """
        return self.data

    @property
    def buy_price(self):
        """ Return buy price of ticker """
        return self.data['buyPrice']

    @property
    def sell_price(self):
        """ Return sell price of ticker """
        return self.data['sellPrice']

    @property
    def last_price(self):
        """ Return last price of ticker """
        return self.data['lastPrice']

    @property
    def highest_price(self):
        """ Return highest price of ticker """
        return self.data['highestPrice']

    @property
    def lowest_price(self):
        """ Return lowst price of ticker """
        return self.data['lowestPrice']

    @property
    def symbol(self):
        """ Return symbol of ticker """
        return self.data['tickerSymbol']

    @property
    def currency(self):
        """ Return currency of ticker """
        return self.data['currency']

    @property
    def isin(self):
        """ Return isin of ticker """
        return self.data['isin']

    @property
    def marketplace(self):
        """ Return marketplace of ticker """
        return self.data['marketPlace']

    @property
    def name(self):
        """ Return name of ticker """
        return self.data['name']

    @property
    def change(self):
        """ Return chage in currency of ticker """
        return self.data['change']

    @property
    def change_percent(self):
        """ Return change in percent of ticker """
        return self.data['changePercent']

    @property
    def flag_code(self):
        """ Return flag code of ticker """
        return self.data['flagCode']

    @property
    def country(self):
        """ Return country of ticker """
        return self.data['country']

    @property
    def id(self):
        """ Return id of ticker """
        return self.data['id']

    @property
    def quote_updated(self):
        """ Return time of last quote update of ticker """
        return self.data['quoteUpdated']

    @property
    def last_price_updated(self):
        """ Return time of last price update of ticker """
        return self.data['lastPriceUpdated']
