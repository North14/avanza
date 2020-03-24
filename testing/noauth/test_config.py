import avanza


def test_config():
    assert avanza.Config.get('cookie_path') == '/tmp/.cookies'
    avanza.Config.set({'cookie_path': '/tmp/.cookies1'})
    assert avanza.Config.get('cookie_path') == '/tmp/.cookies1'
