---
tags:
  - DSA
date: 2025-08-25T20:19:00
---
In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does a recursive In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it returns values in ascending order.

What makes this traversal "in" order, is that the node is visited in between the recursive function calls. The node is visited after the In-order Traversal of the left subtree, and before the In-order Traversal of the right subtree.

![[Pasted image 20250825204441.png]]

The `inOrderTraversal()` function keeps calling itself with the current left child node as an argument until that argument is `None` and the function returns.

The first time the argument `node` is `None` is when the left child of node C is given as an argument (C has no left child).

After that, the `data` part of node C is printed, which means that 'C' is the first thing that gets printed.

Then, node C's right child is given as an argument, which is `None`, so the function call returns without doing anything else.

After 'C' is printed, the previous `inOrderTraversal()` function calls continue to run, so that 'A' gets printed, then 'D', then 'R', and so on.