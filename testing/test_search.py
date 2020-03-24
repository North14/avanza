import avanza


def test_search():
    search = avanza.Search("msft").info
    for resultGroup in search['resultGroups']:
        if resultGroup['instrumentType'] == "STOCK":
            for hit in resultGroup['hits']:
                if hit['link']['orderbookId'] == '3873':
                    return
    else:
        raise Exception("test_search: ERROR")
