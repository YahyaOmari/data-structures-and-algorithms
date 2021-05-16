# Defining Node Class
class Node:
  def __init__ (self, data = None):
    self.data = data
    self.next =  None
    
  # use a magic method so when you print node you see it's value
  def __str__ (self, data):
    return f'{self.data}'

# Define linked list
class Linking:
  # Constructor
  def __init__(self):
    self.head = None

    # Defining append method
  def insert(self, data=None):
    new_node = Node(data)

    # Once we have a head 
    if self.head:
      # set our current pointer to the head
      new_node.next = self.head
      #Assign new_node to self.head 
    self.head = new_node
      # while there is a following node that's not None

  def includes(self,value):
    current = self.head
    including = False
    while (current):
      if current.data == value:
        including = True
      current = current.next
    return including

  def __str__(self):
    # step 0 - create a new empty string
    output = ""
    # step 1 iterate over each node
    current = self.head
    while current:
      # step 2 - insert each data to the string
      output += "{%s} -> " %(current.data,)
      # step 2b:  move to the next item
      current = current.next
    output += "NULL"

    # step 3 - return the final string
    return output
# ------------------------------------------
# -----------------APPEND-------------------
# ------------------------------------------
  def append(self, data):

    current = self.head
    while(current.next):
      current = current.next
    
    new_data = Node(data)
    current.next = new_data
# ------------------------------------------
# -----------------insert_after-------------
# ------------------------------------------

  def insert_after(self,data, new_value):
    new_node = Node(new_value)
    current = self.head

    while current:
      if current.data == data:
        new_node.next = current.next
        current.next = new_node
        break

      current = current.next

      if current == None:
        # As a Python developer you can choose to throw an exception if a condition occurs. 
        # The raise keyword is used to raise an exception.
        raise Exception("Sorry, search value found")
# ------------------------------------------
# -----------------insert_before------------
# ------------------------------------------
  
  def insert_before(self, data, new_value):
    new_node = Node(new_value)
    current = self.head

    if current.data == data:
      new_node.next = current
      self.next = new_node
    else:
      while current.next:
        if current.next.data == data:
          new_node.next = current.next
          current.next = new_node
          break

      current = current.next

      if current == None:
        raise Exception("Sorry, search value found")



if __name__ == "__main__":
  linked = Linking()
  linked.insert("Zakaria")
  linked.insert("Yahya")
  linked.insert(8)
  # linked.append(88)
  # linked.append(22)
  # linked.append(20)
  # linked.append(1)
  linked.insert_before("Yahya", 88)
  linked.insert_before(88, "hello")
  linked.insert_before("hello", 'world')

  print(linked)
  # print(linked.includes("Zakaria"), linked.includes("Yahya"), linked.includes(18))
