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

def test_append(list_test):
    list_test.append(88)
    excpected = "{8} -> {Yahya} -> {Zakaria} -> {88} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_append2(list_test):
    list_test.append(22)
    list_test.append(20)
    list_test.append(1)
    excpected = "{8} -> {Yahya} -> {Zakaria} -> {22} -> {20} -> {1} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_insert_after(list_test):
    list_test.insert_after("Yahya", 88)
    excpected = "{8} -> {Yahya} -> {88} -> {Zakaria} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_insert_after2(list_test):
    list_test.insert_after("Yahya", 88)
    list_test.insert_after(88, "hello")
    list_test.insert_after("hello", 'world')
    excpected = "{8} -> {Yahya} -> {88} -> {hello} -> {world} -> {Zakaria} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_insert_before(list_test):
    list_test.insert_before("Yahya", 88)
    excpected = "{8} -> {88} -> {Yahya} -> {Zakaria} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual

def test_insert_before2(list_test):
    list_test.insert_before("Yahya", 88)
    list_test.insert_before(88, "hello")
    list_test.insert_before("hello", 'world')
    excpected = "{8} -> {world} -> {hello} -> {88} -> {Yahya} -> {Zakaria} -> NULL"
    actual = f"{list_test}"
    assert excpected == actual



@pytest.fixture
def list_test():
    linked = Linking()
    linked.insert("Zakaria")
    linked.insert("Yahya")
    linked.insert(8)
    return linked