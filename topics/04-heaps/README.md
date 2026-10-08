# Heaps and Priority Queues
## Core idea
A priority queue removes items according to priority. A binary heap is one implementation.

A binary min-heap is a complete binary tree with the invariant that each parent is no larger than either child. The minimum is at the root. Siblings and separate subtrees are not globally sorted.

## Array representation
Using zero-based positions:
- Parent of i > 0: (i - 1) // 2.
- Left child: 2 * i + 1.
- Right child: 2 * i + 2.

Only positions inside the array correspond to actual nodes.

## Operations
Insertion appends a value and moves it upward until the invariant holds. Removing the minimum replaces the root with the last value and moves it downward.

Peek is O(1). Sifting traverses at most O(log n) levels. With dynamic-array storage, push is amortized O(log n); an individual resize can cost O(n). Bottom-up heap construction can achieve O(n), though the starter class builds by repeated insertion in O(n log n).

## Implementation
[MinHeap](../../examples/python/algorithms.py) implements push, peek, and pop for integers, including duplicates. Peek and pop raise IndexError on an empty heap.

## Common confusion
A heap is not a BST, and its backing array is not a sorted array. The “heap” used for dynamic memory allocation is a different concept.

## Try it
Insert 7, 2, 5, 1 by hand. Show the array after each insertion, then remove the minimum twice.

## Expand next
Bottom-up heapify; max-heaps; top-k problems; heapsort.

[Back to index](../../README.md)
