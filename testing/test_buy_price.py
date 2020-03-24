import avanza


def test_buy_price():
    stock = avanza.Ticker(3873).last_price
    cert = avanza.Ticker(966569, instrument='certificate').last_price
    assert isinstance(stock, float)
    assert isinstance(cert, float)
