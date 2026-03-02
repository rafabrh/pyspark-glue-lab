from lc_0242_valid_anagram import solve


def test_true():
    assert solve("anagram", "nagaram") 


def test_false():
    assert not solve("rat", "car")

def test_diff_len():
    assert not solve("a", "ab") 


def test_repeated_chars():
    assert not solve("aacc", "ccac") 