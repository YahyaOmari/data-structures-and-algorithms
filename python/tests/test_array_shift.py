from code_challenges.array_shift.array_shift import insertShiftArray


def test_insertShiftArray():
    actual = insertShiftArray([2,4,6,2,0,77,88,99,14,10,112,8], -555)
    expected = [-555, 0, 2, 2, 4, 6, 8, 10, 14, 77, 88, 99, 112]
    assert actual == expected

def test_insertShiftArray2():
    actual = insertShiftArray([3,2,1,0,4,58,55,10], 7)
    expected = [0, 1, 2, 3, 4, 7, 10, 55, 58]
    assert actual == expected
