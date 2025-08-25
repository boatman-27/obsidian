---
tags:
  - DSA
date: 2025-08-25T21:04:00
---
Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.

What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.

![[Pasted image 20250825210644.png]]

The `postOrderTraversal()` function keeps traversing the left subtree recursively, until `None` is returned when C's left child node is called as the `node` argument.

After C's left child node returns `None`, runs and C's right child node returns `None`, and then the letter 'C' is printed.

This means that C is visited, or printed, "after" its left and right child nodes are traversed, that is why it is called "post" order traversal.

The `postOrderTraversal()` function continues to propagate back to previous recursive function calls, so the next node to be printed is 'D', then 'A'.

The function continues to propagate back and printing nodes until all nodes are printed, or visited.