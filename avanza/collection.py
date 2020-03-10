import logging

from .constants import constants, BASE_URL
from .base import Base

def search(searchQuery):
    """
    Returns results of search query

    :type searchQuery: string
    :param searchQuery: string to be searched at Avanza
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['SEARCH']}".format(searchQuery))

def get_news(index=5):
    """
    Returns x amount of news

    :type index: int
    :param index: amount of news to be returned
    """
    try:
        int(index)
        return Base()._request(f"{BASE_URL}{constants['paths']['NEWS']}".format(index))
    except ValueError:
        logging.error("index must be int")

def get_account_overview(accountId):
    """
    Returns information about accounts watchlists
    .. note:: authentication neccessary

    :type accountId: int
    :param accountId: id of account
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['ACCOUNT_OVERVIEW_PATH']}".format(accountId), auth=True)

def get_transactions(accountId=None):
    """
    Returns information about accounts watchlists
    .. note:: authentication neccessary

    :type accountId: int
    :param accountId: id of account, not neccessary
    """
    url = f"{BASE_URL}{constants['paths']['TRANSACTIONS_PATH']}"
    if accountId:
        return Base()._request(url.format(accountId), auth=True)
    return Base()._request(url.replace('{0:d}', ''), auth=True)

def get_insight(timePeriod="today"):
    """
    Returns accounts
    .. note:: authentication neccessary

    :type timePeriod: string
    :param timePeriod: time period
    """
    timePeriod = timePeriod.upper()
    url = f"{BASE_URL}{constants['paths']['INSIGHT']}".format(timePeriod)
    if Base()._check_timePeriod(timePeriod):
        return Base()._request(url, auth=True)
    else:
        raise Exception("Invalid timePeriod!")

def get_watchlists():
    """
    Returns information about accounts watchlists
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}", auth=True)

def get_positions():
    """
    Returns information about accounts positions
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}", auth=True)

def get_deals_and_orders():
    """
    Returns deals, orders and accounts
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['DEALS_AND_ORDERS_PATH']}", auth=True)

def get_feed():
    """
    Returns feed from Home
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['FEED']}", auth=True)

def get_accounts():
    """
    Returns accounts
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['ACCOUNTS']}", auth=True)

def get_inspiration_list():
    """
    Returns inspiration list
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['INSPIRATION_LIST_PATH']}")

def get_account_summary():
    """
    Returns account summary
    .. note :: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['CATEGORIZED_ACCOUNTS']}", auth=True)
