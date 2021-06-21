from challenges.tree_intersection.tree_intersection import *

def test_tree_intersection():

    tree = BinaryTree(42)
    tree.root.left = Node(110)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(170)
    tree.root.left.right.left = Node(130)
    tree.root.left.right.right = Node(180)
    tree.root.right = Node(600)
    tree.root.right.left= Node(210)
    tree.root.right.right = Node(360)
    tree.root.right.right.left = Node(4)
    tree.root.right.right.right = Node(550)

    tree1 = BinaryTree(150)
    tree1.root.left = Node(110)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(170)
    tree1.root.left.right.left = Node(130)
    tree1.root.left.right.right = Node(180)
    tree1.root.right = Node(250)
    tree1.root.right.left= Node(210)
    tree1.root.right.right = Node(360)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(550)

    expected = [110, 170, 130, 180, 210, 360, 550]
    actual = tree_intersection(tree, tree1)
    assert actual == expected