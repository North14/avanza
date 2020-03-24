import avanza


def test_search():
    search = avanza.Search("msft")
    for resultGroup in search.info['resultGroups']:
        if resultGroup['instrumentType'] == "STOCK":
            for hit in resultGroup['hits']:
                if hit['link']['orderbookId'] == '3873':
                    break
            else:
                continue
            break
    else:
        raise Exception("test_search: ERROR")
    assert isinstance(search.count, int)
    assert isinstance(search.results, list)
    assert isinstance(search.first, dict)
    assert isinstance(search.by_instrument('stock'), list)
