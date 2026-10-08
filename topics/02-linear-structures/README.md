# Linear Structures and Hash Tables
## Choose by operations
A data structure organizes values so selected operations are efficient. Choose based on what you repeatedly need to do.

- **Array:** supports O(1) indexed access in the standard model. Inserting near the front typically requires shifting elements.
- **Dynamic array:** grows its backing storage as needed; geometric growth supports amortized O(1) append.
- **Linked list:** connects nodes by references. Insertion can be O(1) when the needed node references are already available; finding a position is generally O(n).
- **Stack:** last in, first out. Useful for undo histories and DFS.
- **Queue:** first in, first out. Useful for scheduling and BFS.
- **Hash table:** maps keys to buckets using a hash function. Expected lookup can be O(1) under suitable hashing and load assumptions; worst-case lookup can be O(n).

## Python connection
A list is a dynamic array, not a linked list. Removing its first element shifts remaining elements. A deque supports efficient operations at both ends, which makes it suitable for BFS queues.

A hash collision means different keys map to the same hash value or bucket. Correct implementations still distinguish keys using equality checks.

## Try it
Choose a structure for each task and justify the operations:
1. Undo the most recent edit.
2. Process requests in arrival order.
3. Count occurrences of each word.
4. Read the item at position 500 repeatedly.

## Expand next
Linked-list implementation; circular buffers; collision resolution; resizing; sets.

[Back to index](../../README.md)
