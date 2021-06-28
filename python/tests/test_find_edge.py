from challenges.graph.graph import *

def test_edge():
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
    
    actual = graph.business_trip([node_c ,node_e])
    expect = (True, '9$')
    assert expect == actual

def test_edge2():
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
    
    actual = graph.business_trip([node_c ,node_e, node_f])
    expect = (True, '16$')
    assert expect == actual

def test_edge3():
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
    
    actual = graph.business_trip([node_a ,node_e, node_f])
    expect = (False, '$0')
    assert expect == actual