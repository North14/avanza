import logging

from .constants import constants, BASE_URL
from .base import Base

def watchlists():
    """ Returns information about accounts watchlists """
    return Base()._request(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}", auth=True)

def positions():
    """ Returns information about accounts positions """
    return Base()._request(f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}", auth=True)

def deals_and_orders():
    """ Returns deals, orders and accounts """
    return Base()._request(f"{BASE_URL}{constants['paths']['DEALS_AND_ORDERS_PATH']}", auth=True)

def search(searchQuery):
    """ Returns results of search query """
    return Base()._request(f"{BASE_URL}{constants['paths']['SEARCH']}".format(searchQuery))

def news(index=5):
    """ Returns x amount of news """
    try:
        int(index)
        return Base()._request(f"{BASE_URL}{constants['paths']['NEWS']}".format(index))
    except ValueError:
        logging.error("orderbookId must be int")

def feed():
    """ Returns feed from Home """
    return Base()._request(f"{BASE_URL}{constants['paths']['FEED']}", auth=True)

def accounts():
    """ Returns accounts """
    return Base()._request(f"{BASE_URL}{constants['paths']['ACCOUNTS']}", auth=True)
