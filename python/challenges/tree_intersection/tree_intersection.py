class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = Node(root)

    def contains(self, value):
        self.flag = False
        def walk(current):
            if current:
                if current.data == value:
                   self.flag = True
                if current.left:
                    walk(current.left)
                if current.right:
                    walk(current.right)
        walk(self.root)
        return self.flag

def tree_intersection(tree_one,tree_two):
    result = []
    def walk(current_one, current_two):
        if current_one and current_two.root:
            if current_two.contains(current_one.data):
                result.append(current_one.data)
            if current_one.left:
                walk(current_one.left, current_two)
            if current_one.right:
                walk(current_one.right, current_two)

    walk(tree_one.root, tree_two)
    return result