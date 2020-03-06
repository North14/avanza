import logging
import requests
import pickle
from os import path
from selenium import webdriver

from .constants import constants

BASE_URL = 'https://www.avanza.se'


class Avanza:
    def __init__(self):
        self.session = requests.Session()

    def _request_noauth(self, url):
        """ Returns json of requested url """
        return self.session.get(url).json()

    def _test_auth(self):
        """ Tests authentication by checking response of positions page """
        url = f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}"
        response = self.session.get(url)
        if response.ok:
            return True
        return False

    def _authenticate(self):
        """ Test authentication using cookies """
        if not self._test_auth():
            if path.isfile('.cookies'):  # if not authenticated, load cookies
                with open('.cookies', 'r+b') as f:
                    self.session.cookies.update(pickle.load(f))
            if not self._test_auth():  # if still not authenticated try logging in and saving new cookies
                driver = webdriver.Firefox()
                driver.get(f"{BASE_URL}{constants['paths']['LOGIN']}")
                while True:
                    if driver.current_url == f"{BASE_URL}{constants['paths']['HOME']}":
                        [self.session.cookies.set(c['name'], c['value']) for c in driver.get_cookies()]
                        driver.close()
                        break
                with open('.cookies', 'w+b') as f:
                    pickle.dump(self.session.cookies, f)

    def _request_withauth(self, url):
        """ Authenticates before returning json of requested url """
        self._authenticate()
        return self.session.get(url).json()

    def _request(self, url, auth=False):
        """ Choose with or without account depending on function """
        if auth:
            return self._request_withauth(url)
        else:
            return self._request_noauth(url)

    def stock(self, orderbookId):
        """
        Returns information about stock,
        may be used for funds/certificates too,
        but might return different results
        """
        try:
            int(orderbookId)
            return self._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))
        except ValueError:
            logging.error("orderbookId must be int")

    def fund(self, orderbookId):
        """
        Returns information about fund,
        may be used for funds/certificates too,
        but might return different results
        """
        try:
            int(orderbookId)
            return self._request(f"{BASE_URL}{constants['paths']['FUND_PATH']}".format(orderbookId))
        except ValueError:
            logging.error("orderbookId must be int")

    def certificate(self, orderbookId):
        """
        Returns information about certificate,
        may be used for funds/certificates too,
        but might return different results
        """
        try:
            int(orderbookId)
            return self._request(f"{BASE_URL}{constants['paths']['CERTIFICATE_PATH']}".format(orderbookId))
        except ValueError:
            logging.error("orderbookId must be int")

    def watchlists(self):
        """ Returns information about accounts watchlists """
        return self._request(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}", auth=True)

    def positions(self):
        """ Returns information about accounts positions """
        return self._request(f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}", auth=True)

    def deals_and_orders(self):
        """ Returns deals, orders and accounts """
        return self._request(f"{BASE_URL}{constants['paths']['DEALS_AND_ORDERS_PATH']}", auth=True)

    def search(self, searchQuery):
        """ Returns results of search query """
        return self._request(f"{BASE_URL}{constants['paths']['SEARCH']}".format(searchQuery))

    def overview_chartdata(self, timePeriod):
        """ Returns chartdata from overview page """
        timePeriod = timePeriod.upper()
        for periods in constants['public']['chartdata']:
            if timePeriod == periods:
                break
        else:
            raise Exception("Invalid timeperiod!")
        return self._request(f"{BASE_URL}{constants['paths']['CHARTDATA_OVERVIEW']}".format(timePeriod), auth=True)

    def news(self, index):
        """ Returns x amount of news """
        try:
            int(index)
            return self._request(f"{BASE_URL}{constants['paths']['NEWS']}".format(index))
        except ValueError:
            logging.error("orderbookId must be int")

    def distribution_chartdata(self):
        """ Returns values from account distribution chart """
        return self._request(f"{BASE_URL}{constants['paths']['CHARTDATA_DISTRIBUTION']}", auth=True)

    def feed(self):
        """ Returns feed from Home """
        return self._request(f"{BASE_URL}{constants['paths']['FEED']}", auth=True)

    def accounts(self):
        """ Returns accounts """
        return self._request(f"{BASE_URL}{constants['paths']['ACCOUNTS']}", auth=True)
