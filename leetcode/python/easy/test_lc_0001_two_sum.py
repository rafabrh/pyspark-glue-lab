from lc_0001_two_sum import solve

def test_basic():
    assert solve([2, 7, 11, 15], 9) == [0, 1]

def test_duplicates():
    assert solve([3, 3], 6) == [0, 1]

def test_negative():
    assert solve([-1, -2, -3, -4, -5], -8) == [2, 4]
