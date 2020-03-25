import avanza


def test_news():
    news = avanza.News(3)
    assert news
    assert news.results
    assert isinstance(news.pretty, str)
    assert isinstance(news.info, dict)
