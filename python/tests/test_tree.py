from challenges.tree.tree import *
import pytest

@pytest.fixture
def tree_test():
    node1 = TNode(11)
    node1.left = TNode(12)
    node1.right = TNode(13)
    node1.right.left = TNode(14)
    node1.right.right = TNode(15)
    return node1

def test_init_empty():
    binary_tree_test = BinaryTree()
    actual = binary_tree_test.__str__()
    expected = 'None'
    assert actual == expected

def test_init_one():
    node1 = TNode(11)
    binary_tree_test = BinaryTree(node1) 
    actual = binary_tree_test.__str__()
    expected = '11'
    assert actual == expected


def test_init_right_and_left():
    node1 = TNode(11)
    node1.left = TNode(12)
    node1.right = TNode(13)
    binary_tree_test = BinaryTree(node1) 
    actual = binary_tree_test.root.data , binary_tree_test.root.left.data , binary_tree_test.root.right.data
    # print(actual)
    expected = 11,12,13
    assert actual == expected 

def test_pre_order(tree_test):
    binary_tree_test = BinaryTree(tree_test) 
    actual = binary_tree_test.pre_order()
    # print(actual)
    expected = '[11, 12, 13, 14, 15]'
    assert actual == expected 

def test_in_order(tree_test):
    binary_tree_test = BinaryTree(tree_test) 
    actual = binary_tree_test.in_order()
    # print(actual)
    expected = '[12, 11, 14, 13, 15]'
    assert actual == expected 

def test_post_order(tree_test):
    binary_tree_test = BinaryTree(tree_test) 
    actual = binary_tree_test.post_order()
    expected = '[12, 14, 15, 13, 11]'
    assert actual == expected 


