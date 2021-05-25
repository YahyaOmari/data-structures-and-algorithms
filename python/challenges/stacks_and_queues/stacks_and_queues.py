class EmptyStackException(Exception):
  pass



class Node: 
  def __init__(self, value=None):
    self.value = value
    self.next = None

# ------------------STACK------------------
class Stack:
  def __init__(self, node=None):
    self.top = node
  
  def push(self, value):
    """
    Push the elements to the top of the (stack)
    returns none 
    """
    if not self.top:
        self.top = Node(value)
    else:
      node = Node(value)
      node.next = self.top
      self.top = node
  
  def pop(self):
      if self.is_empty():
        print("stack is empty")
        raise EmptyStackException("stack is empty")
      else:
          temp = self.top
          self.top = self.top.next
          temp.next = None
          return temp.value

  
  def is_empty(self):
    """ Returns False if the stack is empty or False if it is not """
    if self.top:
      return False
    return True 

  def peek(self):
    """ Returns the value at the top without modifying the stack, raises an exception otherwise """
    if not self.is_empty():
      return self.top.value
    
    raise EmptyStackException("Cannot peek an empty stack")
  
  def __str__(self):
    current = self.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)



# ------------------QUEUE------------------
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, value):
        """ Add an item to the rear fo the queue """
        node = Node(value)

        if not self.front:
        # we have an emtpy queue
            self.front = node
            self.rear = node
        else:
        # make sure the previous rear will now point to the new node
            self.rear.next = node
        # move our rear to point to the new node
            self.rear = self.rear.next
    
    def dequeue(self):
        """ deletes an from the rear of the queue """

        if self.is_empty():
            raise EmptyStackException("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

        
    
        
    def is_empty(self):
        """ Returns False if the queue is empty or False if it is not """
        if self.front:
            return False
        return True 

    

    def peek(self):
        """ Returns the value at the top without modifying the queue, raises an exception otherwise """
        if not self.is_empty():
          return self.front.value
    
        raise EmptyStackException("Cannot peek an empty stack")
  
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

class PseudoQueue:
  def __init__(self):
    self.first_stack = Stack()
    self.second_stack = Stack()
  
  def enqueuePs(self, value):
    self.first_stack.push(value)
  
  def dequeuePs(self):
    if not self.second_stack.top and not self.first_stack.top:
        return "Can not remove, because the queue is empty"
      
    while self.first_stack.top:
      first_top = self.first_stack.pop()
      self.second_stack.push(first_top)
      
    final = self.second_stack.pop()
    temp = self.second_stack
    self.second_stack =Stack()
      
    while temp.top:
      temp_top = temp.pop()
      self.first_stack.push(temp_top)
    return final
  
  def __str__(self):
    current = self.first_stack.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)

if __name__ == "__main__":
  stack = Stack()

  # print(stack)
#   print(stack.peek())
  # stack.push(5)
  # stack.push(99)
  # stack.push(2222)
  # stack.push("Hello")
  # print(stack)
  # print("------------------")
  # print(stack.pop())
#   # print(stack)
# #   stack.push(4)
# #   print(stack)
# #   print(stack.pop)
#   print(stack.peek())
#   # print(stack)
#   stack.pop()

#   queue = Queue()
# #   print(queue)
#   queue.enqueue("Abed")
# # #   print(queue)
#   queue.enqueue("Faisal")
# # #   print(queue)
#   queue.enqueue("Yahya")
#   print(queue)
#   print("------------------")
# #   print(queue.peek())
#   print(queue.dequeue())
#   queue.dequeue()
#   queue.dequeue()
#   print("********")
#   print(queue)
#   print(queue.is_empty())
  fake = PseudoQueue()
  fake.enqueue(4)
  fake.enqueue(5)
  fake.enqueue(6)
  print(fake)
  print(fake.dequeue())
  print("--------------------")
  print(fake)