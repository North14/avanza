import avanza


def test_ticker():
    msft = avanza.Ticker(3873)
    assert isinstance(msft.info, dict)
    assert isinstance(msft.buy_price, float)
    assert isinstance(msft.sell_price, float)
    assert isinstance(msft.last_price, float)
    assert isinstance(msft.symbol, str)
    assert isinstance(msft.currency, str)
    assert isinstance(msft.isin, str)
    assert isinstance(msft.marketplace, str)
    assert isinstance(msft.name, str)
    assert isinstance(msft.change, float)
    assert isinstance(msft.change_percent, float)
    assert isinstance(msft.flag_code, str)
    assert isinstance(msft.country, str)
    assert isinstance(msft.id, int)
    assert isinstance(msft.quote_updated, str)
    assert isinstance(msft.last_price_updated, str)
