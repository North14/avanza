#!/usr/bin/env python3

import logging
import json

from .constants import constants, BASE_URL
from .base import Base

class Ticker:
    def __init__(self, orderbookId, option=None):
        self.option = option
        self.data = Base()._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))

    def __str__(self):
        """ Displays data in string format, use function data for dictionary """
        return json.dumps(self.data)

    @property
    def info(self):
        """ Returns full json of ticker call """
        return self.data
