# CS Algorithms
Understand the structure. Explain the algorithm. Verify the result.

An English-language learning repository for core data structures and algorithms. Examples use Python 3.10+ and only the standard library.

## Learning path
Basic knowledge of variables, loops, functions, and Python syntax is assumed.

1. [Complexity and correctness](topics/01-foundations/README.md)
2. [Arrays, linked lists, stacks, queues, and hash tables](topics/02-linear-structures/README.md)
3. [Trees and binary search trees](topics/03-trees/README.md)
4. [Heaps and priority queues](topics/04-heaps/README.md)
5. [Graphs, BFS, and DFS](topics/05-graphs/README.md)
6. [Searching and sorting](topics/06-searching-and-sorting/README.md)
7. [Problem-solving patterns](topics/07-problem-solving/README.md)

Trees, heaps, and graphs are data structures. Searching, traversal, and sorting are algorithms that operate on data. Learn the representations and operations together.

## Available implementations
[Python examples](examples/python/algorithms.py) include:
- Binary search.
- Breadth-first search with unweighted distances.
- Iterative depth-first search.
- Binary-tree inorder traversal.
- A binary min-heap with push, peek, and pop.
- Merge sort.

Run the tests from the repository root:
```sh
python3 -m unittest discover -s tests -v
```

The introductory notes and these six implementations are available now. Advanced topics in the [roadmap](ROADMAP.md) are planned, not implemented.

## How to study each topic
1. Explain the problem and identify the required operations.
2. Work through a small example by hand.
3. State the invariant or correctness argument.
4. Implement the idea without looking at the reference.
5. Test empty inputs, duplicates, boundaries, and disconnected structures where relevant.
6. Analyze time and space, including assumptions about representation.

Use the [algorithm template](templates/algorithm.md) and [contribution guidelines](CONTRIBUTING.md) for new notes.

## Companion repository
[CS Fundamentals](https://github.com/yaesungseo/cs-fundamentals) explains Git, hardware, programming languages, operating systems, networking, APIs, and databases.

## Further reading
[Open Data Structures](https://opendatastructures.org/) provides a freely accessible treatment of data structures and their analysis.
