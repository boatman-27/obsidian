---
tags:
  - DSA
date: 2025-08-25T13:51:00
---
A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:

- Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
- Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
- Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
- Binary Trees can be represented as arrays, making the tree more memory efficient.
---
## Binary Trees vs Arrays and Linked Lists
Benefits of Binary Trees over Arrays and Linked Lists:
- **Arrays** are fast when you want to access an element directly, like element number 700 in an array of 1000 elements for example. But inserting and deleting elements require other elements to shift in memory to make place for the new element, or to take the deleted elements place, and that is time consuming.
- **Linked Lists** are fast when inserting or deleting nodes, no memory shifting needed, but to access an element inside the list, the list must be traversed, and that takes time.
- **Binary Trees**, such as Binary Search Trees and AVL Trees, are great compared to Arrays and Linked Lists because they are BOTH fast at accessing a node, AND fast when it comes to deleting or inserting a node, with no shifts in memory needed.
---
## Types of Binary Trees
A **balanced** tree is one where there is a difference of at most **1** in the **height** between the left and right subtrees. 
A **complete** Binary Tree has all levels full of nodes, except the last level, which is can also be full, or filled from left to right. The properties of a complete Binary Tree means it is also balanced. (No jumps between nodes till there is no more nodes).
A **full** Binary Tree is a kind of tree where each node has either 0 or 2 child nodes.
A **perfect** Binary Tree has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal/parent nodes have two child nodes.The properties of a perfect Binary Tree means it is also full, balanced, and complete.

---
## Binary Tree Traversal
Going through a Tree by visiting every node, one node at a time, is called traversal.

There are two main categories of Tree traversal methods:
- **[[Breadth First Search]] (BFS)** is when the nodes on the same level are visited before going to the next level in the tree. This means that the tree is explored in a more sideways direction.
- **Depth First Search (DFS)** is when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in a downwards direction.
	- [[pre-order]]
	- [[in-order]]
	- [[post-order]]

[[Array Implementation]] of Binary Trees

---
## Binary Tree snippets
See the full code examples here: [[Binary Tree Snippets]]
