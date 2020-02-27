import requests
import logging

from dataclasses import dataclass

from .constants import constants

BASE_URL = 'http://www.avanza.se'

class Avanza:
    def __init__(self, login_data, login_method):
        self.login_data = login_data
        self.login_method = login_method
        # self.username = username
        # self.password = password
        # self.totp_secret = totp_secret
        self.session = requests.Session()

    def _request_noauth(self, url):
        return self.session.get(url, cookies={'from-my': 'browser'}).json()

    def _request_totp(self, url):
        # TODO: authenticate before returning json
        response = self.session.post(
                f"constants['paths']['AUTHENTICATION_PATH']",
                json=self.login_data
                )
        if self.login_data['totp_secret']:
            pass
        return self.session.get(url).json()

    def _request_bankid(self, url):
        response = self.session.post(
                f"{BASE_URL}{constants['paths']['BANKID_PATH']}",
                json=self.login_data,
                )
        logging.info(response)
        return self.session.get(url).json()


    def check_login_data(self):
        if self.login_method:
            if (self.login_method == 'totp') and \
                    self.login_data['username'] and \
                    self.login_data['password'] and \
                    self.login_data['totp_secret']:
                return True
            elif (self.login_method == 'bankid') and \
                    self.login_data['identificationNumber']:
                return True
        else:
            return False

    def _request(self, url, auth):
        if auth == 'required':
            if self.check_login_data():
                self._request_totp(url)
            else:
                raise Exception("Login data neccessary")
        elif auth == 'optional':
            if self.check_login_data():
                if self.login_method == 'totp':
                    return self._request_totp(url)
                if self.login_method == 'bankid':
                    return self._request_bankid(url)
            else:
                logging.info("Additional data can be found if login data is set")
                return self._request_noauth(url)
        elif auth == 'unneccessary':
            return self._request_noauth(url)

    def stock_path(self, orderbookId):
        return self._request(f"{BASE_URL}{constants['paths']['STOCK_PATH']}".format(orderbookId), 'optional')

    def fund_path(self, orderbookId):
        return self._request(f"{BASE_URL}{constants['paths']['FUND_PATH']}".format(orderbookId), 'optional')

    def certificate_path(self, orderbookId):
        return self._request(f"{BASE_URL}{constants['paths']['CERTIFICATE_PATH']}".format(orderbookId), 'optional')

    def watchlists_path(self):
        return self._request(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}",  'required')

    def search(self, searchQuery):
        return self._request(f"{BASE_URL}{constants['paths']['SEARCH']}".format(searchQuery), 'unneccessary')
