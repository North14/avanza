import requests
import logging

from dataclasses import dataclass

from .constants import constants

BASE_URL = 'http://www.avanza.se'

@dataclass
class Authenticate:
    username: str
    password: str
    totp_secret: str

class Avanza:
    def __init__(self, username, password, totp_secret):
        self.username = username
        self.password = password
        self.totp_secret = totp_secret
        self.session = requests.Session()
    
    def check_login_data(self):
        for x in [self.username, self.password, self.totp_secret]:
            if not x:
                return False
        else:
            return True

    def _request(self, url):
        return self.session.get(url).json()

    def _request_with_auth(self, url):
        # TODO: authenticate before returning json
        return self.session.get(url).json()

    def _authenticate(self, credentials):
        pass

    def stock_path(self, orderbookId):
        if self.check_login_data():
            return self._request_with_auth(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))
        else:
            logging.info("Additional data can be found if login data is set")
            return self._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))

    def fund_path(self, orderbookId):
        if self.check_login_data():
            return self._request_with_auth(f"{BASE_URL}{constants['paths']['FUND_PATH']}".format(orderbookId))
        else:
            logging.info("Additional data can be found if login data is set")
            return self._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))

    def certificate_path(self, orderbookId):
        if self.check_login_data():
            return self._request_with_auth(f"{BASE_URL}{constants['paths']['CERTIFICATE_PATH']}".format(orderbookId))
        else:
            logging.info("Additional data can be found if login data is set")
            return self._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId))

    def watchlists_path(self):
        if self.check_login_data():
            return self._request_with_auth(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}")
        else:
            logging.error("This function needs login data")

