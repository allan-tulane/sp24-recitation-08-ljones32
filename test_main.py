from main import *

def test_compute_optimal_paths():
    graph = {
        's': {('a', 1), ('c', 4)},
        'a': {('b', 2)},
        'b': {('c', 1), ('d', 4)},
        'c': {('d', 3)},
        'd': {},
        'e': {('d', 0)}
    }
    result = compute_optimal_paths(graph, 's')
    # Verifying both the weight and number of edges in the optimal path
    assert result['s'] == (0, 0)
    assert result['a'] == (1, 1)
    assert result['b'] == (3, 2)
    assert result['c'] == (4, 1)
    assert result['d'] == (7, 2)

def test_build_bfs_tree():
    graph = generate_graph()
    tree = build_bfs_tree(graph, 's')
    # Testing the parent relationships established by BFS
    assert tree['a'] == 's'
    assert tree['b'] == 's'    
    assert tree['c'] == 'b'
    assert tree['d'] == 'c'

def test_retrieve_path():
    graph = generate_graph()
    tree = build_bfs_tree(graph, 's')
    # Testing the path from the source 's' to the destination 'd'
    assert retrieve_path(tree, 'd') == 'sbc'
