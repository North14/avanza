import avanza


def test_inspiration_list():
    inspiration = avanza.Collection.get_inspiration_list()
    q = type(inspiration)
    assert q is dict or q is list
