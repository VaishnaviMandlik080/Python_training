
'''
Demonstrate pytest assertions.
Five tests pass and one fails.
'''

def test_f1():
    port = 3000
    assert port == 3000


def test_f2():
    port = 3000
    assert port > 3000


def test_f3():
    app = "grafana"
    assert app == "grafana"


def test_f4():
    n = 100
    assert n < 200


def test_sample():
    status_code = 200
    assert status_code == 200


def test_sample_url():
    url = "api.com"
    assert url == "api.com"