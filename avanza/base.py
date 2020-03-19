import requests
import logging
logger = logging.getLogger(__name__)

from .constants import constants, BASE_URL


class Base:
    def __init__(self):
        """Base class which other classes/function uses

        Attributes:
            session: initiates request session
        """
        self.session = requests.Session()

    @property
    def _auth_ok(self):
        """Tests authentication by checking response of positions page"""
        url = f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}"
        response = self.session.get(url)
        if response.ok:
            logger.debug("Authentication OK")
            return True
        return False

    def _authenticate(self):
        """Tests authentication using cookies"""
        logger.debug("Try authenticate using cookies")
        import pickle
        from os import path
        if path.isfile('.cookies'):
            with open('.cookies', 'r+b') as f:
                self.session.cookies.update(pickle.load(f))
            if self._auth_ok:
                return
            logger.debug("Authentication using cookies unsuccessful")
        else:
            logger.debug("No cookies found")

        logger.debug("Try authenticate using selenium")
        from selenium import webdriver
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions
        with webdriver.Firefox() as driver:
            wait = WebDriverWait(driver, 1200)
            driver.get(f"{BASE_URL}{constants['paths']['LOGIN']}")
            wait.until(expected_conditions.title_is("Hem"))
            [self.session.cookies.set(c['name'], c['value']) for c in driver.get_cookies()]
        if self._auth_ok:
            try:
                with open('.cookies', 'w+b') as f:
                    pickle.dump(self.session.cookies, f)
            except Exception as error:
                logging.debug(f"Error while saving cookies: {error}")
            return
        else:
            logger.debug("Authentication using selenium unsuccessful")
        assert self._auth_ok

    def _request(self, url, p={}, h={}, method="GET", auth=False):
        """Download json of url with python request session

        Args:
            url (str): link to be requested
            auth (bool): auth=True if request need authentication

        Returns:
            dict: json python dict of url
        """
        if auth and not self._auth_ok:
            self._authenticate()
        if method == "POST":
            import json
            r = self.session.post(url, data=json.dumps(p), headers=h).json()
        elif method == "GET":
            r = self.session.get(url, params=p, headers=h).json()
        else:
            raise Exception("error invalid method for _request")
        if 'statusCode' in r:
            logger.debug(f"Error while retrieving json {r['time']}: {r['statusCode']} - {r['message']}")
            if r['errors']:
                logger.debug(f"Error while retrieving json {r['time']}: {r['errors']}")
            if r['additional']:
                logger.debug(f"Error while retrieving json {r['time']}: {r['additional']}")
            raise Exception("Error while retrieving json")
        return r

    def _check_timePeriod(self, time_period):
        """Checks if arg timePeriod is a valid time period

        Args:
            timePeriod (str): time period

        Returns:
            bool
        """
        for period in constants['public']['chartdata']:
            if time_period == constants['public']['chartdata'][period]:
                return True
        else:
            logger.debug(f"Invalid time period: {time_period}")
            return False
