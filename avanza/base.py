import logging
logger = logging.getLogger(__name__)
import requests

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
            import pickle
            from os import path
            if path.isfile('.cookies'):
                with open('.cookies', 'r+b') as f:
                    self.session.cookies.update(pickle.load(f))
                if self._test_auth():
                    return
            if not self._test_auth():
                from selenium import webdriver
                from selenium.webdriver.support.ui import WebDriverWait
                from selenium.webdriver.support import expected_conditions

                with webdriver.Firefox() as driver:
                    wait = WebDriverWait(driver, 1200)
                    driver.get(f"{BASE_URL}{constants['paths']['LOGIN']}")
                    wait.until(expected_conditions.title_is("Hem"))
                    [self.session.cookies.set(c['name'], c['value']) for c in driver.get_cookies()]
                with open('.cookies', 'w+b') as f:
                    pickle.dump(self.session.cookies, f)
        if not self._test_auth():
            raise Exception("Authentication error")

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
                logger.debug("Valid time period")
                return True
        else:
            logger.debug("Invalid time period")
            return False
