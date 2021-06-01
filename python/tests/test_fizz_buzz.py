from challenges.tree.tree import *
from challenges.tree.fizz_buzz_tree import *

def test_fizz_buzz():
    fizz = BinaryTree()
    fizz.root = TNode(1)
    fizz.root.left = TNode(10)
    fizz.root.right = TNode(12)
    fizz.root.left.left = TNode(2)
    fizz.root.left.right = TNode(18)
    fizz.root.right.right = TNode(15)
    actual = fizz_buzz_tree(fizz).pre_order()
    print(actual)
    expected = "[1, 'Buzz', 2, 'Fizz', 'Fizz', 'FizzBuzz']"
    assert actual == expected

def test_fizz_buzz_second():
    fizz = BinaryTree()
    fizz.root = TNode(1)
    fizz.root.left = TNode(3)
    fizz.root.right = TNode(9)
    fizz.root.left.left = TNode(12)
    fizz.root.left.right = TNode(15)
    fizz.root.right.right = TNode(18)
    fizz.root.right.right.right = TNode(30)
    actual = fizz_buzz_tree(fizz).pre_order()
    print(actual)
    expected = "[1, 'Fizz', 'Fizz', 'FizzBuzz', 'Fizz', 'Fizz', 'FizzBuzz']"
    assert actual == expected

def test_fizz_buzz_second():
    fizz = BinaryTree()
    fizz.root = TNode(2)
    fizz.root.left = TNode(4)
    fizz.root.right = TNode(8)
    fizz.root.left.left = TNode(13)
    fizz.root.left.right = TNode(19)
    fizz.root.right.right = TNode(22)
    fizz.root.right.right.right = TNode(26)
    actual = fizz_buzz_tree(fizz).pre_order()
    print(actual)
    expected = "[2, 4, 13, 19, 8, 22, 26]"
    assert actual == expected

