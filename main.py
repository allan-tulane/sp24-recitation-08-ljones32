import heapq
from collections import deque

def compute_optimal_paths(graph, start):
    # Initialize distances with infinity for cost and path length
    optimal = {vertex: (float('inf'), float('inf')) for vertex in graph}
    optimal[start] = (0, 0)

    # Priority queue to manage vertices exploration based on distance and path length
    queue = [(0, 0, start)]  # (distance, number of edges, vertex)

    while queue:
        dist, edges, vertex = heapq.heappop(queue)

        if (dist, edges) > optimal[vertex]:
            continue

        for adjacent, weight in graph[vertex]:
            new_dist = dist + weight
            new_edges = edges + 1

            if (new_dist, new_edges) < optimal[adjacent]:
                optimal[adjacent] = (new_dist, new_edges)
                heapq.heappush(queue, (new_dist, new_edges, adjacent))

    return optimal

def build_bfs_tree(graph, root):
    """ Construct the BFS tree as a dictionary mapping each vertex to its parent. """
    tree = {root: None}
    queue = deque([root])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in tree:
                tree[neighbor] = node
                queue.append(neighbor)

    return tree

def generate_graph():
    """ Provides a sample graph for demonstration. """
    return {
        's': {'a', 'b'},
        'a': {'b'},
        'b': {'c'},
        'c': {'a', 'd'},
        'd': {}
    }

def retrieve_path(tree, target):
    """ Build the path from source to target using the BFS tree, excluding the target itself. """
    path = []
    node = target
    while node is not None:
        path.append(str(node))
        node = tree[node]
    return ''.join(path[:0:-1])

