import pytest
from challenges.linked_list.linked_list import *


# def test_import():
#     assert Linking


def test_insert(list_test):
    excpected = "{8} -> {Yahya} -> {Zakaria} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_includes(list_test):
    actual = [list_test.includes("Zakaria"),list_test.includes("Yahya"),list_test.includes(18)]
    excpected = [True, True , False]
    assert excpected == actual


@pytest.fixture
def list_test():
    linked = Linking()
    linked.insert("Zakaria")
    linked.insert("Yahya")
    linked.insert(8)
    return linked