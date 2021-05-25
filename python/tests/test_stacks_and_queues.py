from challenges.stacks_and_queues.stacks_and_queues import *
import pytest

# -----------------------------
# ------------SLACK------------
# -----------------------------

@pytest.fixture
def test_stack():
    test_stack = Stack()
    """helper function to create a stack"""
    test = [10,11,12,13]
    for data in test:
        test_stack.push(data)
    return test_stack

def test_stack_empty():
    empty_stack = Stack()
    assert empty_stack.top == None

def test_stack_push(test_stack):

    test_stack.push(10)
    assert test_stack.top.value == 10
    test_stack.push('yahya')
    assert test_stack.top.value == 'yahya'
    test_stack.push('omari')
    assert test_stack.top.value == 'omari'

def test_stack_pop(test_stack):
    # test = [10,11,12,13]
    assert test_stack.pop() == 13
    assert test_stack.top.value == 12
    assert test_stack.top.next.value == 11
    test_stack.pop()
    test_stack.pop()
    test_stack.pop()
    assert test_stack.top == None
    assert test_stack.top == None

def test_stack_peek(test_stack):
    # test = [10,11,12,13]
    assert test_stack.peek() == 13
    test_stack.pop()
    assert test_stack.peek() == 12
    test_stack.pop()
    test_stack.pop()
    assert test_stack.peek() == 10

# -----------------------------
# ------------QUEUE------------
# -----------------------------

@pytest.fixture
def test_queue():
    test_queue = Queue()
    test = ['yahya', 'abed', 'hasan', 'test']
    for data in test:
        test_queue.enqueue(data)
    return test_queue

def test_queue_is_empty(test_queue):
    assert test_queue.is_empty() == False
    test_queue = Stack()
    assert test_queue.is_empty() == True

def test_queue_one_el(test_queue):
    assert test_queue.is_empty() == False
    assert test_queue.rear.value == "test"
    assert test_queue.front.value == "yahya"
    assert test_queue.peek() == "yahya"


def test_queue_empty():
    test_queue = Queue()
    assert test_queue.front == None
    assert test_queue.rear == None

def test_queue_enqueu():
    test_queue = Queue()
    assert test_queue.front == None
    test_queue.enqueue('yahya')
    assert test_queue.front.value == 'yahya'
    test_queue.enqueue('abed')
    assert test_queue.rear.value == 'abed'
    assert test_queue.front.value == 'yahya'
    test_queue.enqueue('5')
    assert test_queue.rear.value == '5'
    assert test_queue.front.value == 'yahya'

def test_queue_dequeue(test_queue):
    # test = ['yahya', 'abed', 'hasan', 'test']
    assert test_queue.dequeue() == 'yahya'
    assert test_queue.front.value == 'abed'
    assert test_queue.front.next.value == 'hasan'
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.front == None

def test_queue_peek(test_queue):
    # test = ['yahya', 'abed', 'hasan', 'test']
    assert test_queue.peek() == 'yahya'
    test_queue.dequeue()
    assert test_queue.peek() == 'abed'
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.dequeue()
    assert test_queue.front == None


# -----------------------------------------
# ------------queue_with_stack-------------
# -----------------------------------------


@pytest.fixture
def queue_list():
    test_list = [5, 10, 15, 20]
    test_queue = PseudoQueue()
    for i in test_list:
        test_queue.enqueuePs(i)
    
    return test_queue


def test_enqueue_to_empty():
    test = PseudoQueue()
    test.enqueuePs(5)
    actual = test.__str__()
    expected = "5"
    assert actual == expected

def test_enqueue(queue_list):
    queue_list.enqueuePs(25)
    actual = queue_list.__str__()
    excepted = "25\n20\n15\n10\n5"
    assert actual == excepted

def test_dequeue(queue_list):
    first_value = queue_list.dequeuePs()
    second_value = queue_list.dequeuePs()
    third_value = queue_list.dequeuePs()
    fourth_value = queue_list.dequeuePs()
    actual = [first_value, second_value, third_value, fourth_value]
    excepted = [5, 10, 15, 20]
    assert actual == excepted
