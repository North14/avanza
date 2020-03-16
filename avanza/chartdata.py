import logging
import json
import pandas

from .constants import constants, BASE_URL
from .base import Base


class ChartData(Base):
    """Grab json chartdata and output as pandas DataFrame"""
    def get_overview_chartdata(self, timePeriod='one_month'):
        """Returns chartdata from overview page

        Args:
            timePeriod (str): time period

        Returns:
            dict:

        Note:
            Authentication necessary
        """
        timePeriod = timePeriod.upper()
        url = f"{BASE_URL}{constants['paths']['CHARTDATA_OVERVIEW']}".format(timePeriod)
        if self._check_timePeriod(timePeriod):
            r = self._request(url, auth=True)
            if 'absoluteSeries' in r:
                data_series = []
                for serie in r['absoluteSeries']:
                    point = {'timestamp': serie['timestamp']}
                    point.update(serie['performance'])
                    point.pop('decimalPrecision')
                    data_series.append(point)
            return pandas.read_json(json.dumps(data_series))
        else:
            raise Exception("Invalid timePeriod!")

    def get_distribution_chartdata(self):
        """Returns values from account distribution pie chart

        Returns:
            dict:

        Note:
            Authentication necessary\n
            Will not keep original drilldown
        """
        url = f"{BASE_URL}{constants['paths']['CHARTDATA_DISTRIBUTION']}"
        r = self._request(url, auth=True)
        pie_dict_list = []
        for x in r:
            if x['drilldownSeries']:
                for drilldown in x['drilldownSeries']:
                    pie_dict_list.append(drilldown)
            else:
                x.pop('drilldownSeries', None)
                pie_dict_list.append(x)
        return pandas.read_json(json.dumps(pie_dict_list))

    def get_ticker_chartdata(self, orderbookId, timePeriod='one_week'):
        """Returns daily chartdata of ticker

        Args:
            orderbookId (int): id of instrument
            timePeriod (str): time period, default='today'

        Returns:
            dict:
        """
        url = f"{BASE_URL}{constants['paths']['CHARTDATA_PATH']}".format(orderbookId, timePeriod.lower())
        if self._check_timePeriod(timePeriod.upper()):
            r = self._request(url)
            if 'dataSeries' in r:
                data_series = r['dataSeries']
            return pandas.read_json(json.dumps(data_series))
        else:
            raise Exception("Invalid timePeriod!")
