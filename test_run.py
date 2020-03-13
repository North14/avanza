import avanza


def test_buy_price():
    stock = avanza.Ticker(3873).last_price
    cert = avanza.Ticker(966569, instrument='certificate').last_price
    try:
        float(stock)
        float(cert)
        print("test_buy_price: OK")
    except:
        raise Exception("test_buy_price: ERROR")


def test_ticker_chartdata():
    chartdata = avanza.chartdata.get_ticker_chartdata(3873)
    if chartdata:
        print("test_ticker_chartdata: OK")
    else:
        raise Exception("test_ticker_chartdata: ERROR")


def test_search():
    search = avanza.Search("msft").info
    for resultGroup in search['resultGroups']:
        if resultGroup['instrumentType'] == "STOCK":
            for hit in resultGroup['hits']:
                if hit['link']['orderbookId'] == '3873':
                    print("test_search: OK")
                    return
    else:
        raise Exception("test_search: ERROR")
