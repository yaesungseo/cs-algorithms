# Trees
## Core idea
An undirected tree is a connected graph with no cycles. A rooted tree selects one vertex as the root, defining parent-child relationships.

A binary tree has at most two children per node. A binary search tree (BST) additionally orders keys: for a distinct-key convention, keys in the left subtree are smaller and keys in the right subtree are larger. Duplicate handling requires an explicit policy.

## Traversals
- Preorder: visit node, left subtree, right subtree.
- Inorder: visit left subtree, node, right subtree.
- Postorder: visit left subtree, right subtree, node.
- Level order: visit nodes by depth using a queue.

Inorder traversal of a BST produces sorted keys under its ordering convention. Inorder traversal of an arbitrary binary tree does not necessarily do so.

## Complexity
BST lookup takes O(h), where h is tree height. A balanced tree has logarithmic height; an unbalanced chain can have linear height. “BST operations are O(log n)” needs a balance assumption.

A full traversal visits n nodes in O(n) time. An explicit traversal stack can use O(h) auxiliary space. Returning all visited values additionally requires O(n) output space.

## Implementation
[Inorder traversal and TreeNode](../../examples/python/algorithms.py) use an explicit stack. The input must be a proper finite binary tree without cycles or shared child nodes. BST insertion and balancing are planned.

## Try it
Draw a BST after inserting 1, 2, 3, 4 in that order. Compare its height with a balanced arrangement of the same keys.

## Expand next
BST search and deletion; AVL and red-black trees; tries; tree recursion.

[Back to index](../../README.md)
