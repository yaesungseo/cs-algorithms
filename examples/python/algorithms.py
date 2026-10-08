"""Small reference implementations for the accompanying learning notes."""

from collections import deque
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence


def binary_search(values: Sequence[int], target: int) -> int:
    """Return any matching index, or -1. Requires ascending sorted values."""
    low, high = 0, len(values)
    while low < high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle
    return -1


def bfs_distances(graph: Mapping[str, Sequence[str]], source: str) -> dict[str, int]:
    """Return unweighted distances. Missing keys have no outgoing edges."""
    distances = {source: 0}
    queue = deque([source])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.get(vertex, ()):
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    return distances


def dfs(graph: Mapping[str, Sequence[str]], source: str) -> list[str]:
    """Visit reachable vertices once; no specific DFS ordering is promised."""
    seen = {source}
    order = [source]
    # Each frame remembers the remaining neighbors, like a recursive call.
    stack = [iter(graph.get(source, ()))]
    while stack:
        neighbor = next(stack[-1], None)
        if neighbor is None:
            stack.pop()
        elif neighbor not in seen:
            seen.add(neighbor)
            order.append(neighbor)
            stack.append(iter(graph.get(neighbor, ())))
    return order


@dataclass
class TreeNode:
    value: int
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


def inorder(root: TreeNode | None) -> list[int]:
    """Traverse a finite binary tree; cycles and shared nodes are unsupported."""
    result = []
    stack = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


class MinHeap:
    """Integer min-heap. Construction uses repeated insertion: O(n log n)."""

    def __init__(self, values: Iterable[int] = ()) -> None:
        self._items: list[int] = []
        for value in values:
            self.push(value)

    def __len__(self) -> int:
        return len(self._items)

    def peek(self) -> int:
        """Return the smallest value, raising IndexError when empty."""
        if not self._items:
            raise IndexError("peek from empty heap")
        return self._items[0]

    def push(self, value: int) -> None:
        self._items.append(value)
        child = len(self._items) - 1
        while child > 0:
            parent = (child - 1) // 2
            if self._items[parent] <= self._items[child]:
                break
            self._items[parent], self._items[child] = self._items[child], self._items[parent]
            child = parent

    def pop(self) -> int:
        """Remove the smallest value, raising IndexError when empty."""
        if not self._items:
            raise IndexError("pop from empty heap")
        smallest = self._items[0]
        last = self._items.pop()
        if self._items:
            self._items[0] = last
            parent = 0
            while 2 * parent + 1 < len(self._items):
                child = 2 * parent + 1
                right = child + 1
                if right < len(self._items) and self._items[right] < self._items[child]:
                    child = right
                if self._items[parent] <= self._items[child]:
                    break
                self._items[parent], self._items[child] = self._items[child], self._items[parent]
                parent = child
        return smallest


def merge_sort(values: Sequence[int]) -> list[int]:
    """Return a sorted copy using stable merging; leave the input unchanged."""
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
