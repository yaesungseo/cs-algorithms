"""Behavioral checks, including comparisons against independent references."""

import heapq
import random
import unittest

from examples.python.algorithms import (
    MinHeap, TreeNode, bfs_distances, binary_search, dfs, inorder, merge_sort,
)


class AlgorithmTests(unittest.TestCase):
    def test_binary_search_boundaries(self):
        self.assertEqual(binary_search([], 2), -1)
        self.assertEqual(binary_search([2], 2), 0)
        self.assertEqual(binary_search([2], 3), -1)
        values = [-5, -1, 0, 4, 9]
        for index, value in enumerate(values):
            self.assertEqual(binary_search(values, value), index)
        for missing in (-6, -2, 3, 10):
            self.assertEqual(binary_search(values, missing), -1)

    def test_binary_search_duplicates(self):
        values = [1, 2, 2, 2, 5]
        index = binary_search(values, 2)
        self.assertGreaterEqual(index, 0)
        self.assertEqual(values[index], 2)

    def test_binary_search_against_membership(self):
        rng = random.Random(42)
        for _ in range(100):
            values = sorted(rng.randrange(-20, 21) for _ in range(rng.randrange(40)))
            for target in range(-22, 23):
                index = binary_search(values, target)
                if target in values:
                    self.assertTrue(0 <= index < len(values))
                    self.assertEqual(values[index], target)
                else:
                    self.assertEqual(index, -1)

    def test_bfs_cycles_duplicates_and_disconnected_vertex(self):
        graph = {"a": ["b", "c", "b"], "b": ["a", "d"],
                 "c": ["d"], "d": ["d"], "isolated": []}
        self.assertEqual(bfs_distances(graph, "a"),
                         {"a": 0, "b": 1, "c": 1, "d": 2})

    def test_missing_graph_keys(self):
        self.assertEqual(bfs_distances({}, "a"), {"a": 0})
        self.assertEqual(bfs_distances({"a": ["b"]}, "a"), {"a": 0, "b": 1})
        self.assertEqual(dfs({}, "a"), ["a"])
        self.assertEqual(dfs({"a": ["b"]}, "a"), ["a", "b"])

    def test_dfs_reachability_without_repeated_vertices(self):
        graph = {"a": ["b", "c"], "b": ["c"], "c": ["a"], "d": []}
        result = dfs(graph, "a")
        self.assertEqual(result[0], "a")
        self.assertEqual(set(result), {"a", "b", "c"})
        self.assertEqual(len(result), 3)

    def test_graph_algorithms_against_transitive_closure(self):
        rng = random.Random(17)
        for _ in range(25):
            labels = [str(i) for i in range(7)]
            graph = {u: [v for v in labels if rng.random() < 0.25] for u in labels}
            # Floyd-Warshall provides an independent all-pairs reference.
            distance = {(u, v): (0 if u == v else 1 if v in graph[u] else float("inf"))
                        for u in labels for v in labels}
            for k in labels:
                for u in labels:
                    for v in labels:
                        distance[u, v] = min(distance[u, v], distance[u, k] + distance[k, v])
            for source in labels:
                expected = {v: distance[source, v] for v in labels
                            if distance[source, v] != float("inf")}
                self.assertEqual(bfs_distances(graph, source), expected)
                traversal = dfs(graph, source)
                self.assertEqual(set(traversal), set(expected))
                self.assertEqual(len(traversal), len(expected))

    def test_inorder(self):
        self.assertEqual(inorder(None), [])
        self.assertEqual(inorder(TreeNode(7)), [7])
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
        self.assertEqual(inorder(root), [1, 2, 3, 4, 5])
        self.assertEqual(inorder(TreeNode(1, TreeNode(9), TreeNode(0))), [9, 1, 0])

    def test_inorder_deep_tree(self):
        root = None
        for value in range(1500):
            root = TreeNode(value, left=root)
        self.assertEqual(inorder(root), list(range(1500)))

    def test_heap_empty_singleton_and_duplicates(self):
        heap = MinHeap()
        with self.assertRaises(IndexError):
            heap.peek()
        with self.assertRaises(IndexError):
            heap.pop()
        heap.push(3)
        self.assertEqual(heap.peek(), 3)
        self.assertEqual(heap.pop(), 3)
        heap = MinHeap([5, -2, 5, 0, -2])
        self.assertEqual([heap.pop() for _ in range(len(heap))], [-2, -2, 0, 5, 5])

    def test_heap_mixed_operations_against_heapq(self):
        rng = random.Random(8)
        heap = MinHeap()
        reference = []
        for _ in range(1000):
            if not reference or rng.random() < 0.6:
                value = rng.randrange(-100, 101)
                heap.push(value)
                heapq.heappush(reference, value)
            else:
                self.assertEqual(heap.pop(), heapq.heappop(reference))
            self.assertEqual(len(heap), len(reference))
            if reference:
                self.assertEqual(heap.peek(), reference[0])
        self.assertEqual([heap.pop() for _ in range(len(heap))], sorted(reference))

    def test_merge_sort_against_sorted_and_preserves_input(self):
        rng = random.Random(12)
        cases = [[], [1], [2, 1], [3, 3, -1], list(range(30)), list(range(30, -1, -1))]
        cases += [[rng.randrange(-30, 31) for _ in range(n)] for n in range(80)]
        for values in cases:
            original = values[:]
            self.assertEqual(merge_sort(values), sorted(values))
            self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
