import logging
import json
import pandas

from .constants import constants, BASE_URL
from .base import Base


class ChartData(Base):
    """Grab json chartdata and output as pandas DataFrame"""
    def get_overview_chartdata(self, time_period='one_month'):
        """Returns chartdata from overview page

        Args:
            time_period (str): time period

        Returns:
            dict:

        Note:
            Authentication necessary
        """
        time_period = time_period.upper()
        url = f"{BASE_URL}{constants['paths']['CHARTDATA_OVERVIEW']}".format(time_period)
        if self._check_time_period(time_period):
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
            raise Exception("Invalid time_period!")

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

#    def get_ticker_chartdata(self, orderbookId, time_period='one_week'):
#        """Returns daily chartdata of ticker
#
#        Args:
#            orderbookId (int): id of instrument
#            time_period (str): time period, default='today'
#
#        Returns:
#            dict:
#        """
#        url = f"{BASE_URL}{constants['paths']['CHARTDATA_PATH']}".format(orderbookId, time_period.lower())
#        if self._check_time_period(time_period.upper()):
#            r = self._request(url)
#            if 'dataSeries' in r:
#                data_series = r['dataSeries']
#            return pandas.read_json(json.dumps(data_series))
#        else:
#            raise Exception("Invalid time_period!")

    def get_ticker_chartdata(self, orderbook_id, time_period="month", chart_type="AREA", chart_resolution="TEN_MINUTES"):
        """Returns chartdata from overview page

        Args:
            orderbook_id (int): 
            time_period (str): time period
            chart_type (str): Type of chart (AREA, CANDLESTICK, OHLC)
            chart_resolution (str): resolution of chart

        Returns:
            dict:

        Note:
            Authentication necessary
        """
        url = f"{BASE_URL}{constants['paths']['CHARTDATA_PATH']}"
        p = {
            "orderbookId": orderbook_id,
            "chartType": chart_type,
            "chartResolution": chart_resolution,
            "timePeriod": time_period
            }
        h = {"Content-Type": "application/json"}
        r = self._request(url, p=p, h=h, method="POST")
        if 'dataPoints' in r:
            data_series = r['dataPoints']
            df = pandas.read_json(json.dumps(data_series))
            df.columns = ['timestamp', 'value']
            return df
        return r
