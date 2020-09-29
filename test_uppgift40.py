from uppgift40 import rev_string, stor_bokstav, in_range


def test_rev_string():
    expected = "test sträng"[::-1]
    got = rev_string("test sträng")
    assert expected == got


def test_rev_string1():
    expected = "jag är hungrig"[::-1]
    got = rev_string("jag är hungrig")
    assert expected == got


def test_rev_string2():
    expected = "abcdef"[::-1]
    got = rev_string("abcdef")
    assert expected == got


def test_stor_bokstav():
    expected = 3
    got = stor_bokstav("ABC")
    assert expected == got


def test_stor_bokstav1():
    expected = 4
    got = stor_bokstav("TesT StränG")
    assert expected == got


def test_stor_bokstav2():
    expected = 0
    got = stor_bokstav("abcdef")
    assert expected == got


def test_stor_bokstav3():
    expected = 0
    got = stor_bokstav("")
    assert expected == got



def test_in_range():
    expected = True
    got = in_range(2, 1, 3)
    assert expected == got


def test_in_range1():
    expected = False
    got = in_range(0, 1, 3)
    assert expected == got


def test_in_range2():
    expected = True
    got = in_range(50, 10, 100)
    assert expected == got
