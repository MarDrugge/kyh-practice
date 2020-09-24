from Uppgift36.pwstrength import compute_strength


def test_pw_length11():
    pw = "1" * 11
    assert compute_strength(pw) == 1


def test_pw_length5():
    pw = "1" * 5
    assert compute_strength(pw) == 0


def test_lett_and_num():
    pw = "abc123"
    assert compute_strength(pw) == 1


def test_only_num():
    pw = "123"
    assert compute_strength(pw) == 0


def test_only_lett():
    pw = "abc"
    assert compute_strength(pw) == 0


def test_spec_char():
    pw = "##"
    assert compute_strength(pw) == 1


def test_wrong_spec_char():
    pw = "!!"
    assert compute_strength(pw) == 0


def test_all():
    pw = "abc123##" * 2
    assert compute_strength(pw) == 3