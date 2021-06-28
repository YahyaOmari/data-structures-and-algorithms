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
            return ("Queue is empty")
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
    
        return ("Cannot peek an empty stack")
  
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)
        
class Vertex:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class  Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self,node1=None,node2=None,weight1=0):
        if node1 not in self.adjacency_list:
            raise KeyError
        elif node2 not in self.adjacency_list:
            raise KeyError
        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adjacency_list[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adjacency_list[node2].append(edge)

    def get_nodes(self):
       return self.adjacency_list.keys()

    def get_neighbors(self,node):
        return self.adjacency_list.get(node,[])

    def size(self):
        return len(self.adjacency_list)
        
    
    def breadth_first_search(self, start_vertex, action=(lambda x: None)):
        queue = Queue()
        visited = set()
        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor_vertex = edge.vertex
                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                queue.enqueue(neighbor_vertex)
    
    def business_trip(self, cities):
            cost = 0
            flag = True
            for i in range(len(cities)-1):
                if not flag:
                    return False, '$0'
                neighbors = self.get_neighbors(cities[i])
                for neighbor in neighbors:
                    if cities[i+1] == neighbor.vertex:
                        print(neighbor.weight)
                        cost += neighbor.weight
                        flag = True
                        break
                    else:
                        flag = False
            if not flag :
                cost = 0
            return flag, str(cost)+'$'

if __name__ == '__main__':
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c, 5)
    graph.add_edge(node_a,node_d,5)
    graph.add_edge(node_b,node_c, 1)
    graph.add_edge(node_b,node_f, 4)
    graph.add_edge(node_c,node_e, 9)
    graph.add_edge(node_d ,node_e, 5)
    graph.add_edge(node_e,node_f, 7)
    graph.get_nodes()
    graph.get_neighbors(node_a)[0].weight
    graph.get_neighbors(node_b)[0].weight
    graph.get_neighbors(node_c)[0].weight
    graph.get_neighbors(node_d)[0].weight
    graph.get_neighbors(node_e)[0].weight
    graph.get_neighbors(node_f)[0].weight
    graph.size()
    list_graph = [node_c ,node_e]
    print(graph.business_trip(list_graph))