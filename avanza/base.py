import logging
import requests
import pickle
from os import path
from selenium import webdriver

from .constants import constants, BASE_URL

class Base:
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

    def _check_timePeriod(self, timePeriod):
        for periods in constants['public']['chartdata']:
            if timePeriod == periods:
                return True
        else:
            return False
