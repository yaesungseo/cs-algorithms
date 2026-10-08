# Graphs, BFS, and DFS
## Core idea
A graph has vertices and edges. Specify whether edges are directed, whether they have weights, and whether self-loops or parallel edges are allowed.

An adjacency list stores neighbors for each vertex and typically uses O(V + E) space. An adjacency matrix uses O(V²) space but supports direct edge lookup.

## Breadth-first search
BFS uses a queue to explore vertices in layers. Mark a vertex when it is enqueued so it is queued only once. In an unweighted graph, the first discovery gives a shortest path length measured in number of edges.

BFS does not generally solve shortest paths with unequal edge weights.

## Depth-first search
DFS follows a branch before returning to alternatives. It can use recursion or an explicit stack. Marking visited vertices prevents cycles from causing repeated exploration.

Traversal from one source visits only reachable vertices. To cover a disconnected graph, restart from each still-unvisited vertex.

## Complexity and implementation
With adjacency lists and expected constant-time hashing, BFS and DFS take O(Vr + Er) time for the reachable vertices and their outgoing edges. The [implementations](../../examples/python/algorithms.py) keep O(Vr) auxiliary state. They mark vertices on discovery.

Inputs map string vertex labels to lists of neighbor labels. Missing keys are treated as vertices with no outgoing edges, including a missing source. Neighbor order determines DFS traversal order; no particular DFS ordering is promised.

## Try it
Draw a cycle, an isolated vertex, and two equal-length routes to a destination. Trace BFS distances and explain why the cycle terminates.

## Expand next
Topological sorting; cycle detection; Dijkstra; Bellman–Ford; minimum spanning trees; union-find.

[Back to index](../../README.md)
