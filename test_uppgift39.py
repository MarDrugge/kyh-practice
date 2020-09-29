from uppgift39 import maximum, total, produkt


def test_maximum():
    expected = 3
    got = maximum(1, 2, 3)
    assert expected == got


def test_maximum1():
    expected = 6
    got = maximum(4, 6, 5)
    assert expected == got


def test_maximum2():
    expected = 9
    got = maximum(9, 7, 3)
    assert expected == got


def test_total():
    expected = 6
    got = total([1, 2, 3])
    assert expected == got


def test_total1():
    expected = 15
    got = total([4, 5, 6])
    assert expected == got


def test_total2():
    expected = 7
    got = total([2, 2, 3])
    assert expected == got


def test_produkt():
    expected = 24
    got = produkt([2, 3, 4])
    assert expected == got

def test_produkt1():
    expected = 8
    got = produkt([2, 2, 2])
    assert expected == got


def test_produkt2():
    expected = 120
    got = produkt([4, 5, 6])
    assert expected == got