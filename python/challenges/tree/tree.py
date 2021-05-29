class TNode:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self, root=None):
    self.root = root
  def __str__(self):
      if self.root is None:
         return f"{self.root}"
      return f"{self.root.data}"

# ////////////////////////////////////
# /////////////pre_order//////////////
# ////////////////////////////////////

  def pre_order(self):
    pre_order_list = []
    """ Pre-order traversal of our tree """
    def walk(root):
      if root is  None:
          raise Exception("the tree is empty") 
      pre_order_list.append(root.data)

      if root.left:
        walk(root.left)
      
      if root.right:
        walk(root.right)
         
    walk(self.root)
    return ''.join(f"{pre_order_list}")

# ////////////////////////////////////
# //////////////in_order//////////////
# # ////////////////////////////////////

  def in_order(self):
    in_order_list = []
    """ Pre-order traversal of our tree """
    def walk(root):
      if root is  None:
          raise Exception("the tree is empty") 

      if root.left:
        walk(root.left)

      in_order_list.append(root.data)

      if root.right:
        walk(root.right)
         
    walk(self.root)
    return ''.join(f"{in_order_list}")

# ////////////////////////////////////
# //////////////post_order////////////
# ////////////////////////////////////
  
  def post_order(self):
    """ Pre-order traversal of our tree """
    post_order_list = []
    def walk(root):
      if root is None:
          raise Exception("the tree is empty") 

      if root.left:
        walk(root.left)

      if root.right:
        walk(root.right)

      post_order_list.append(root.data)
   
    walk(self.root)
    return ''.join(f"{post_order_list}")

# class BinarySearchTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def add (self, data):
        if self.key is None:
            self.key = data
            return

        if self.key > data:
            if self.left:
                self.left.add(data) # Using recursion
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = BinarySearchTreeNode(data)





if __name__ == "__main__":
    node1 = TNode(11)
    node1.left = TNode(12)
    node1.right = TNode(13)
    node1.right.left = TNode(14)

    binary_tree = BinaryTree(node1)

    print(binary_tree.pre_order())
    print(binary_tree.pre_order())

    # binary_tree.pre_order_iter()
    print("*******************")
    print(binary_tree.in_order())

    print("*******************")
    print(binary_tree.post_order())

# Think about
class KNode:
  def __init__(self, data=None):
    self.data = data
    # How could you implement this for k of any size?
    self.children = []
