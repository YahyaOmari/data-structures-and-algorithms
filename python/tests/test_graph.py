from challenges.graph.graph import * 
import pytest

@pytest.fixture
def graph():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c)
    graph.add_edge(node_a,node_d)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_f)
    graph.add_edge(node_c,node_e)
    graph.add_edge(node_d ,node_e)
    graph.add_edge(node_e,node_f)
    return graph
    
@pytest.fixture
def graph_weight():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,1)
    graph.add_edge(node_a,node_d,3)
    graph.add_edge(node_b,node_c,5)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,9)
    graph.add_edge(node_d ,node_e,8)
    graph.add_edge(node_e,node_f,4)
    return graph
    
def test_add_node():
    expected = 'a'
    graph = Graph()
    actual = graph.add_node('a').value
    assert actual == expected

def test_add_edge_exists():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    graph.add_edge(node_a,node_b)
    expected = ['b',0]
    edge = graph.adjacency_list[node_a][0]
    actual = [edge.vertex.value,edge.weight]
    assert actual == expected

def test_add_edge_does_not_exists():
    with pytest.raises(KeyError):
        graph = Graph()
        node_a = graph.add_node('a')
        node_b = Vertex('b')
        graph.add_edge(node_a,node_b)

def test_get_nodes(graph):
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    nodes = graph.get_nodes()
    actual = []
    for node in nodes:
        actual.append(node.value)
    assert actual == expected

def test_get_neighbors(graph):
    expected = ['c', ['a', 0], ['b', 0], ['e', 0]]
    nodes = graph.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_neighbors_with_wieght(graph_weight):
    expected = ['c', ['a', 1], ['b', 5], ['e', 9]]
    nodes = graph_weight.get_nodes()
    for node in nodes:
        if node.value == 'c':
            node_c = node
    neighbors = graph_weight.get_neighbors(node_c)
    actual = [node_c.value]
    for edge in neighbors:
        actual += [[edge.vertex.value,edge.weight]]
    assert actual == expected

def test_get_size(graph):
    expected = 6
    actual = graph.size()
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    assert not actual

