from challenges.array_binary_search.array_binary_search import BinarySearch

def test_binary_search():
    actual = BinarySearch([4,8,15,16,23,42], 42)
    expected = 2
    assert actual == expected




def test_binary_search2():
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

