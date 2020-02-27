import requests
import logging
import pickle
from os import path
from selenium import webdriver

from dataclasses import dataclass

from .constants import constants

BASE_URL = 'http://www.avanza.se'

class Avanza:
    def __init__(self):
        self.session = requests.Session()

    def _request_noauth(self, url):
        print("qwe")
        return self.session.get(url).json()

    def _test_auth(self):
        url = f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}"
        response = self.session.get(url)
        if response.ok:
            return True
        return False

    def _authenticate(self):
        if not self._test_auth():
            if path.isfile('.cookies'):
                with open('.cookies', 'r+b')  as f:
                    self.session.cookies.update(pickle.load(f))
            if not self._test_auth():
                driver = webdriver.Firefox()
                driver.get("https://www.avanza.se/start(right-overlay:login/login-overlay)")
                while True:
                    if driver.current_url == "https://www.avanza.se/hem/senaste.html":
                        [self.session.cookies.set(c['name'], c['value']) for c in driver.get_cookies()]
                        driver.close()
                        break
                with open('.cookies', 'w+b') as f:
                    pickle.dump(self.session.cookies, f)

    def _request_withauth(self, url):
        self._authenticate()
        return self.session.get(url).json()

    def _request(self, url, auth=False):
        if auth:
            return self._request_withauth(url)
        else:
            return self._request_noauth(url)

    def stock_path(self, orderbookId):
        return self._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId), auth=True)

    def fund_path(self, orderbookId):
        return self._request(f"{BASE_URL}{constants['paths']['FUND_PATH']}".format(orderbookId), auth=True)

    def certificate_path(self, orderbookId):
        return self._request(f"{BASE_URL}{constants['paths']['CERTIFICATE_PATH']}".format(orderbookId), auth=True)

    def watchlists_path(self):
        return self._request(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}",  auth=True)

    def search(self, searchQuery):
        return self._request(f"{BASE_URL}{constants['paths']['SEARCH']}".format(searchQuery))
