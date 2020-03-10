import logging

from .constants import constants, BASE_URL
from .base import Base

def get_overview_chartdata(timePeriod='one_month'):
    """
    Returns chartdata from overview page
    .. note:: authentication neccessary
    
    :type timePeriod: string
    :param timePeriod: time period 
    """
    timePeriod = timePeriod.upper()
    url = f"{BASE_URL}{constants['paths']['CHARTDATA_OVERVIEW']}".format(timePeriod)
    if Base()._check_timePeriod(timePeriod):
        return Base()._request(url, auth=True)
    else:
        raise Exception("Invalid timePeriod!")

def get_distribution_chartdata():
    """
    Returns values from account distribution chart
    .. note:: authentication neccessary
    """
    return Base()._request(f"{BASE_URL}{constants['paths']['CHARTDATA_DISTRIBUTION']}", auth=True)

def get_ticker_chartdata(orderbookId, timePeriod='today'):
    """
    Returns chartdata of ticker
    
    :type orderbookId: int
    :param orderbookId: id of instrument
    :type timePeriod: string
    :param timePeriod: time period
    """
    timePeriod = timePeriod.upper()
    url = f"{BASE_URL}{constants['paths']['CHARTDATA_PATH']}".format(orderbookId, timePeriod)
    if Base()._check_timePeriod(timePeriod):
        return Base()._request(url)
    else:
        raise Exception("Invalid timePeriod!")
