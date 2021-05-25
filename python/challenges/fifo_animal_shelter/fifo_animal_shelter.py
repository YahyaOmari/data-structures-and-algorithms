class Dog:
    def __init__(self,data):
        self.data = data
        self.type = 'Dog'
        self.next = None

class Cat:
    def __init__(self,data):
        self.data = data
        self.type = 'Cat'
        self.next = None


class Animalshelter():
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        node =  data
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node
            
    def animal_dequeue(self,type):
        
        if self.front:
            temp=self.front
            while temp:
                if temp.type==type:
                    self.front=temp.next
                    temp.next=None
                    if self.rear.data==temp.data:
                        self.front=None
                    return temp.data
                else:
                    temp=temp.next
                    if self.front==self.rear:
                        break
        else:
            print("The queue is Empty")
            return "The queue is Empty"
  
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.data))
            current = current.next
        return "\n".join(items)


if __name__ == "__main__":
    c=Cat('Cat')
    c2=Cat('Cat')
    d=Dog('Dog')
    d2=Dog('Dog')
    animal=Animalshelter()   
    animal.enqueue(c)
    animal.enqueue(c2)
    animal.enqueue(d)
    print(animal)
    animal.animal_dequeue('Cat')
    animal.animal_dequeue('Cat')
    animal.animal_dequeue('Dog')
    animal.animal_dequeue('Dog')
    print("**********")
    print(animal)
    animal.animal_dequeue('Dog')
    print(animal)
