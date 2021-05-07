from challenges.array_binary_search.array_binary_search import binary_search

def test_binary_search():
    actual = binary_search([4,8,15,16,23,42], 42)
    expected = 2
    assert actual == expected




def test_binary_search2():
    actual = binary_search([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

