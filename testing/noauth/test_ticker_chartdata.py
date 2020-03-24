import avanza


def test_ticker_chartdata():
    chartdata = avanza.ChartData().get_ticker_chartdata(3873)
    assert not chartdata.empty
    chartdata = avanza.ChartData().get_ticker_chartdata(3873, chart_type='OHLC')
    assert not chartdata.empty
