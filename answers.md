# CMPS 2200 Recitation 08

## Answers

London Jones

1. Shortest Path Algorithm

b) Work and Span Analysis
The algorithm's work is O((V+E)log⁡V)O((V+E)logV), and the span is O(Vlog⁡V)O(VlogV), involving heap operations for VV vertices and EE edges.
2. Computing Paths with Breadth-First Search

a) BFS Path Representation
The bfs_path function executes BFS while tracking the shortest path tree using a parent dictionary, as shown:

css

{'a': 's', 'b': 's', 'c': 'b', 'd': 'c'}

b) Path Retrieval Function
The get_path function constructs a path string from the source to a destination using a parent dictionary, simplifying the visualization of BFS paths.

