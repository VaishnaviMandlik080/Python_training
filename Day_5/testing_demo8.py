from demo8 import calc

def test_calc():
    assert calc(2, 3) == 5
    assert calc(-1, 1) == 0
    assert calc(0, 0) == 0

test_calc()