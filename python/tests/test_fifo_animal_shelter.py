from challenges.fifo_animal_shelter.fifo_animal_shelter import *

def test_enqueu():
    animal = Animalshelter()
    animal.enqueue(Dog('mishmish'))
    animal.enqueue(Cat('lexi'))

    animal.enqueue(Cat('milo'))
    animal.enqueue(Dog('lexi'))
    assert animal.front.data == 'mishmish'
    assert animal.front.next.data == 'lexi'
    assert animal.front.next.next.data=='milo'
    assert animal.front.next.next.next.data=='lexi'

def test_dequeue_dog():
    animal = Animalshelter()
    animal.enqueue(Cat('milo'))
    animal.enqueue(Dog('lexi'))
    animal.enqueue(Dog('lexi2'))
    assert animal.animal_dequeue('dog')== None



def test_dequeue_cat():
    animal = Animalshelter()
    animal.enqueue(Cat('mishmish'))
    animal.enqueue(Dog('lexi'))
    assert animal.animal_dequeue('cat')== None