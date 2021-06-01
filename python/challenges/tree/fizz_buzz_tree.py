from .tree import *


def matching(num):
    if num % 3 == 0 and num % 5 == 0: 
        return "FizzBuzz"
    
    elif num % 3 == 0: 
        return "Fizz"
    
    elif num % 5 == 0: 
        return "Buzz"
    
    elif num % 3 != 0 and num % 5 != 0: 
        return num
    
    else: 
        return str(num)


def fizz_buzz_tree(tree_data):
    tree = BinaryTree()
    if not tree_data.root: 
        return tree

    def walk(current):
        node = TNode(matching(current.data))

        if current.left: 
            node.left = walk(current.left)
        
        if current.right: 
            node.right = walk(current.right)
        return node

    tree.root = walk(tree_data.root)
    return tree



if __name__ == "__main__":
    fizz = BinaryTree()
    fizz.root = TNode(1)
    fizz.root.left = TNode(10)
    fizz.root.right = TNode(12)
    fizz.root.left.left = TNode(2)
    fizz.root.left.right = TNode(18)
    fizz.root.right.right = TNode(15)
    print(fizz_buzz_tree(fizz).pre_order())


