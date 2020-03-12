#!/usr/bin/env python3
import logging
import json

from .constants import constants, BASE_URL
from .base import Base


class Ticker(Base):
    def __init__(self, orderbookId, instrument='stock', auth=False):
        """Request information about stock/certificate/fund/etc

        Args:
            orderbookId (int): id of instrument
            instrument (str): Type of instrument, Defaults to 'stock'
            auth (bool): Set true for additional information, Defaults to False

        Note:
            Additional information if authenticated
        """
        super().__init__()
        if instrument in ['fund', 'certificate', 'stock']:
            url = f"{BASE_URL}{constants['paths']['INSTRUMENT_PATH']}".format(instrument, orderbookId)
            self.data = self._request(url, auth=auth)
        else:
            raise TypeError("Invalid option!")

    def __str__(self):
        return json.dumps(self.data)

    @property
    def info(self):
        """Grabs full json of ticker call
        
        Returns:
            dict:
        """
        return self.data

    @property
    def buy_price(self):
        """Grabs buy price of ticker
        
        Returns:
            float:
        """
        return self.data['buyPrice']

    @property
    def sell_price(self):
        """Grabs buy sell of ticker
        
        Returns:
            float:
        """
        return self.data['sellPrice']

    @property
    def last_price(self):
        """Grabs last price of ticker
        
        Returns:
            float:
        """
        return self.data['lastPrice']

    @property
    def highest_price(self):
        """Grabs highest price of ticker
        
        Returns:
            float:
        """
        return self.data['highestPrice']

    @property
    def lowest_price(self):
        """Grabs lowest price of ticker
        
        Returns:
            float:
        """
        return self.data['lowestPrice']

    @property
    def symbol(self):
        """Grabs symbol of ticker
        
        Returns:
            str:
        """
        return self.data['tickerSymbol']

    @property
    def currency(self):
        """Grabs currency of ticker
        
        Returns:
            str:
        """
        return self.data['currency']

    @property
    def isin(self):
        """Grabs ISIN of ticker
        
        Returns:
            str:
        """
        return self.data['isin']

    @property
    def marketplace(self):
        """Grabs marketplace of ticker
        
        Returns:
            str:
        """
        return self.data['marketPlace']

    @property
    def name(self):
        """Grabs full name of ticker
        
        Returns:
            str:
        """
        return self.data['name']

    @property
    def change(self):
        """Grabs change price of ticker
        
        Returns:
            int:
        """
        return self.data['change']

    @property
    def change_percent(self):
        """Grabs change price of ticker in percent
        
        Returns:
            int:
        """
        return self.data['changePercent']

    @property
    def flag_code(self):
        """Grabs flag code of ticker
        
        Returns:
            str:
        """
        return self.data['flagCode']

    @property
    def country(self):
        """Grabs the country of ticker
        
        Returns:
            str:
        """
        return self.data['country']

    @property
    def id(self):
        """Grabs the id of ticker
        
        Returns:
            int:
        """
        return self.data['id']

    @property
    def quote_updated(self):
        """Grabs last time quote was updated
        
        Returns:
            str: ISO 8601
        """
        return self.data['quoteUpdated']

    @property
    def last_price_updated(self):
        """Grabs last time price was updated
        
        Returns:
            str: ISO 8601
        """
        return self.data['lastPriceUpdated']
