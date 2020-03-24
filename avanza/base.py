import requests
import logging
logger = logging.getLogger(__name__)

from .constants import constants, BASE_URL


class Config:
    """Config class for setting and retrieving settings

    Attributes:
        settings:
            cookie_path
                path to file which should be used when loading/storing cookies
    """
    _settings = {
            "cookie_path": "/tmp/.cookies",
            }

    @classmethod
    def get(cls, name):
        """Retrieves the value of setting

        Args:
            name (str): The key which value should be returned
        """
        return cls._settings[name]

    @classmethod
    def set(cls, name):
        """Change settings using dict

        Examples:
            >>> avanza.Config.set({'cookie_path': '/path/to/file'})

        Args:
            name (dict): The new values to set
        """
        if isinstance(name, dict):
            for key, val in name.items():
                if key in cls._settings:
                    cls._settings[key] = val
                else:
                    raise NameError("Tried setting name which do not exist")
        else:
            logging.debug(f"Expected dict, retrieved {type(name)}")
            raise TypeError(f"Expected dict, retrieved {type(name)}")


class Base(Config):
    """Base class which other classes/function uses

    Attributes:
        session: initiates request session
    """
    def __init__(self):
        super().__init__()
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
        cookies = self.get('cookie_path')
        if path.isfile(cookies):
            try:
                logging.debug(f"Try loading cookies at: {cookies}")
                with open(cookies, 'r+b') as f:
                    self.session.cookies.update(pickle.load(f))
            except Exception as error:
                logging.debug(f"Error while loading cookies: {error}")
            finally:
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
            for c in driver.get_cookies():
                self.session.cookies.set(c['name'], c['value'])
        if self._auth_ok:
            try:
                logging.debug(f"Try saving cookies at: {cookies}")
                with open(cookies, 'w+b') as f:
                    pickle.dump(self.session.cookies, f)
            except Exception as error:
                logging.debug(f"Error while saving cookies: {error}")
            return
        else:
            logger.debug("Authentication using selenium unsuccessful")
        assert self._auth_ok

    def _request(self, url, **kwargs):
        """Download json of url with python request session

        Args:
            url (str): link to be requested
            auth (bool): auth=True if request need authentication
            params (dict): data for POST requests or params for GET request
            headers (dict): headers for POST and GET request
            method (str): Method of request (GET or POST)

        Returns:
            dict: json python dict of url
        """
        p = kwargs.pop('params', {})
        h = kwargs.pop('headers', {})
        method = kwargs.pop('method', 'GET').upper()
        assert method in ['GET', 'POST']
        auth = kwargs.pop('auth', False)
        assert not kwargs

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
            logger.debug(f"Error while retrieving json {r['time']}: "
                         f"{r['statusCode']} - {r['message']}")
            if r['errors']:
                logger.debug(f"Error while retrieving json {r['time']}: "
                             f"{r['errors']}")
            if r['additional']:
                logger.debug(f"Error while retrieving json {r['time']}: "
                             f"{r['additional']}")
            raise Exception("Error while retrieving json")
        return r

    def _check_time_period(self, time_period):
        """Checks if arg time_period is a valid time period

        Args:
            time_period (str): time period

        Returns:
            bool
        """
        for period in constants['public']['chartdata']:
            if time_period == constants['public']['chartdata'][period]:
                return True
        else:
            logger.debug(f"Invalid time period: {time_period}")
            return False
