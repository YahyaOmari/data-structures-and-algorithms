class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,key,value):
        new_node = Node(key,value)

        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __str__(self):
        output= ''
        current = self.head
        while current:
            output += f'{{{current.key}}}: {{{current.value}}}->'
            current = current.next
            if current == None:
                output += 'NULL'
        return output

class Hashtable:
    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None]*size
    """
    This function takes in an arbitrary key and returns an index in the collection.
    """

    def hash(self,key):
        total = 0
        for i in key:
            total += ord(i)
        hash_key = (total*29)%(self.size)
        return hash_key

    """
    This function takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.        
    """

    def add(self,key,value):
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = LinkedList()
            self._buckets[index].insert(key,value)
        else:
            self._buckets[index].insert(key,value)

    """
    This function takes in the key and returns the value from the table.      
    """


    def get(self,key):
        index = self.hash(key)

        if self._buckets[index] is None:
            return self._buckets[index]
        else:
            current = self._buckets[index].head
            while current:
                if current.key == key:
                    return current.value
                current = current.next

    """
    This function  takes in the key and returns a boolean, indicating if the key exists in the table already.   
    """

    def contains(self,key):
        index = self.hash(key)
        if self._buckets[index] != None:

            current = self._buckets[index].head
            while current:
                if current.key == key:
                    return True
                current = current.next
        else:
            return False

if __name__ == "__main__":
    hashtable = Hashtable()
    hashtable.add("yahya", 10)
    hashtable.add("go", 'play football')
    hashtable.add("no", False)
    print(hashtable.get("go"))
    print(hashtable.get("no"))
    print(hashtable.contains("yahya"))
    print(hashtable.hash('united'), "hashh")