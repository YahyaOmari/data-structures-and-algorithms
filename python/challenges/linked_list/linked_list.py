# class Node:
#   def __init__ (self,value, next_node = None):
#     self.value = value
#     self.next_node =  next_node
# class LinkedList:
#   def __init__(self, head = None ): #empty_linked_list = []
#     self.head = head
#   def insert(self):
# Setting values to the nodes
# node1 = Node('5')
# node2 = Node('7')
# node3 = Node('9')
# node4 = Node('9')

# # Now we want to connect them 
# node1.next_node = (node2) # 5 => 7
# node2.next_node = (node3) # 7 => 9
# node3.next_node = (node4) # 7 => 9

# current_node = node1
# while True:
#   for i in current_node.value:
#     print (i , "=>")

#   if current_node.next_node is None:
#     print (None)
#     break
#   current_node = current_node.next_node
    # print (current_node)

class Node:
  def __init__ (self, data = None):
    self.data = data
    self.next =  None
    
  # use a magic method so when you print node you see it's value
  def __str__ (self, data):
    return f'{self.data}'

class Linking:
  def __init__(self):
    self.head = None

    # Defining append method
  def insert(self, data=None):
    new_node = Node(data)

    if self.head:
      new_node.next = self.head
    self.head = new_node

  def includes(self,value):
    current = self.head
    including = False
    while (current):
      if current.data == value:
        including = True
      current = current.next
    return including

  def __str__(self):
    output = ""

    current = self.head
    while current:
      output += "{%s} -> " %(current.data,)
      
      current = current.next
    output += "NULL"

    return output


if __name__ == "__main__":
  linked = Linking()
  linked.insert("Zakaria")
  linked.insert("Yahya")
  linked.insert(8)

  print(linked)
  print(linked.includes("Zakaria"), linked.includes("Yahya"), linked.includes(18))
