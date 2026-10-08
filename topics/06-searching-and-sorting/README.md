# Searching and Sorting
## Searching
Linear search examines values until it finds a match or reaches the end: O(n) worst-case time.

Binary search requires a sorted, random-access sequence. It compares the middle value and discards half of the candidate interval. It takes O(log n) time and O(1) auxiliary space in the iterative implementation.

The [binary_search example](../../examples/python/algorithms.py) returns a matching index or -1. With duplicate values it may return any matching index. It assumes ascending order and does not spend O(n) time validating that precondition.

## Sorting
Merge sort divides an input into halves, sorts them recursively, and merges the sorted results. Selecting from the left half first on equal values preserves stability.

The [merge_sort example](../../examples/python/algorithms.py) returns a new sorted list, leaving its input unchanged. Its worst-case running time is O(n log n), with O(n) peak additional storage for the lists used in this implementation and O(log n) recursion depth.

Other algorithms to compare:
- Insertion sort: O(n²) worst case, useful as a simple baseline.
- Heapsort: O(n log n) worst case; standard in-place variants are not stable.
- Quicksort: expected O(n log n) with suitable randomization, but O(n²) worst case.
- Counting sort: O(n + k) for integer keys in a suitable range of size k.

## Try it
Search for 6 in [1, 3, 5, 7, 9]. Write down every interval. Then explain why the same procedure fails on an unsorted list.

## Expand next
Lower and upper bounds; stable sorting; partitioning; quickselect; sorting lower bounds.

[Back to index](../../README.md)
