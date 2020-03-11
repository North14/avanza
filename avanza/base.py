import logging
import requests
import pickle
from os import path
from selenium import webdriver

from .constants import constants, BASE_URL

class Base:
    def __init__(self):
        """Base class which other classes/function uses

        Attributes:
            session: initiates request session
        """
        self.session = requests.Session()

    def _test_auth(self):
        """Tests authentication by checking response of positions page"""
        url = f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}"
        response = self.session.get(url)
        if response.ok:
            return True
        return False

    def _authenticate(self):
        """Tests authentication using cookies"""
        if not self._test_auth():
            if path.isfile('.cookies'):
                with open('.cookies', 'r+b') as f:
                    self.session.cookies.update(pickle.load(f))
            if not self._test_auth():
                driver = webdriver.Firefox()
                driver.get(f"{BASE_URL}{constants['paths']['LOGIN']}")
                while True:
                    if driver.current_url == f"{BASE_URL}{constants['paths']['HOME']}":
                        [self.session.cookies.set(c['name'], c['value']) for c in driver.get_cookies()]
                        driver.close()
                        break
                with open('.cookies', 'w+b') as f:
                    pickle.dump(self.session.cookies, f)

    def _request(self, url, auth=False):
        """Download json of url with python request session

        Args:
            url (str): link to be requested
            auth (bool): auth=True if request need authentication

        Returns:
            dict: json python dict of url
        """
        if auth:
            self._authenticate()
        return self.session.get(url).json()

    def _check_timePeriod(self, timePeriod):
        """Checks if arg timePeriod is a valid time period

        Args:
            timePeriod (str): time period

        Returns:
            bool
        """
        for period in constants['public']['chartdata']:
            if timePeriod == constants['public']['chartdata'][period]:
                return True
        else:
            return False
