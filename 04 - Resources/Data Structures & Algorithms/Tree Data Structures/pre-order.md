---
tags:
  - DSA
date: 2025-08-25T14:44:00
---
Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, followed by a recursive pre-order traversal of the right subtree.

This traversal is "pre" order because the node is visited "before" the recursive pre-order traversal of the left and right subtrees.

visited is the fancy word of saying *do something with the data stored in the node*. 
But in real code, “visit” could mean anything:
- printing,
- summing values,
- searching for a key.
- mutating values.

![[Pasted image 20250825145532.png]]

The first node to be printed is node R, as the Pre-order Traversal works by first visiting, or printing, the current node, before calling the left and right child nodes recursively.

The `preOrderTraversal()` function keeps traversing the left subtree recursively, before going on to traversing the right subtree. So the next nodes that are printed are 'A' and then 'C'.

The first time the argument `node` is `None` is when the left child of node C is given as an argument (C has no left child).

After `None` is returned the first time when calling C's left child, C's right child also returns `None`, and then the recursive calls continue to propagate back so that A's right child D is the next to be printed.b 

The code continues to propagate back so that the rest of the nodes in R's right subtree gets printed.