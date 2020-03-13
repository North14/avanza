import logging

from .constants import constants, BASE_URL
from .base import Base


def get_account_overview(accountId):
    """Returns information about accounts watchlists
    
    Args:
        accountId (int): id of account
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['ACCOUNT_OVERVIEW_PATH']}".format(accountId), auth=True)


def get_transactions(accountId=None):
    """
    Returns information about accounts watchlists


    Args:
        accountId (int, optional): id of account
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    url = f"{BASE_URL}{constants['paths']['TRANSACTIONS_PATH']}"
    if accountId:
        return Base()._request(url.format(accountId), auth=True)
    return Base()._request(url.replace('{0:d}', ''), auth=True)


def get_insight(timePeriod="today"):
    """
    Returns accounts

    Args:
        timePeriod (str): time period
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    timePeriod = timePeriod.upper()
    url = f"{BASE_URL}{constants['paths']['INSIGHT']}".format(timePeriod)
    if Base()._check_timePeriod(timePeriod):
        return Base()._request(url, auth=True)
    else:
        raise Exception("Invalid timePeriod!")


def get_watchlists():
    """Returns information about accounts watchlists
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['WATCHLISTS_PATH']}", auth=True)


def get_positions():
    """Returns information about accounts positions
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}", auth=True)


def get_deals_and_orders():
    """Returns deals, orders and accounts
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['DEALS_AND_ORDERS_PATH']}", auth=True)


def get_feed():
    """Returns feed from Home
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['FEED']}", auth=True)


def get_accounts():
    """Returns accounts
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['ACCOUNTS']}", auth=True)


def get_inspiration_list():
    """Returns inspiration list
    
    Returns:
        dict:
    
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['INSPIRATION_LIST_PATH']}")


def get_account_summary():
    """Returns account summary
    
    Returns:
        dict:
    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['CATEGORIZED_ACCOUNTS']}", auth=True)
