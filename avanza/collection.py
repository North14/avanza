from .constants import constants, BASE_URL
from .base import Base


def get_account_overview(account_id):
    """Returns information about accounts watchlists

    Args:
        account_id (int): id of account

    Returns:
        dict:

    Note:
        Authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['ACCOUNT_OVERVIEW_PATH']}".format(account_id), auth=True)


def get_transactions(account_id=None):
    """
    Returns information about accounts watchlists


    Args:
        account_id (int): id of account

    Returns:
        dict:

    Note:
        Authentication neccessary
    """
    url = f"{BASE_URL}{constants['paths']['TRANSACTIONS_PATH']}"
    if account_id:
        return Base()._request(url.format(account_id), auth=True)
    return Base()._request(url.replace('{0:d}', ''), auth=True)


def get_insight(**kwargs):
    """
    Returns accounts

    Args:
        time_period (str): time period

    Returns:
        dict:

    Note:
        Authentication neccessary
    """
    time_period = kwargs.pop('time_period', 'TODAY').upper()
    assert not kwargs
    url = f"{BASE_URL}{constants['paths']['INSIGHT']}".format(time_period)
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
