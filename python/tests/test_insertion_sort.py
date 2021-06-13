import pytest
from challenges.insertion_sort.insertion_sort import insertion_sort

def test_insertion_sort():
    actual = insertion_sort([5,2,6,0])
    excpected = [0, 2, 5, 6]
    assert excpected == actual

def test_insertion_sort2():
    actual = insertion_sort([20,18,12,8,5,-2])
    excpected = [-2, 5, 8, 12, 18, 20]
    assert excpected == actual

def test_insertion_sort3():
    actual = insertion_sort([5,12,7,5,5,7])
    excpected = [5, 5, 5, 7, 7, 12]
    assert excpected == actual

def test_insertion_sort4():
    actual = insertion_sort([2,3,5,7,13,11])
    excpected = [2, 3, 5, 7, 11, 13]
    assert excpected == actual