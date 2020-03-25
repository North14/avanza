import avanza


def test_inspiration_list():
    inspiration = avanza.collection.get_inspiration_list()
    q = type(inspiration)
    assert q is dict or q is list
