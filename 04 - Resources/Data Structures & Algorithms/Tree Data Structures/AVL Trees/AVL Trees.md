---
tags:
  - DSA
date: 2025-09-06T12:41:00
---
An **AVL tree** defined as a self-balancing [[Binary Search Tree]] where the difference between heights of left and right subtrees for any node cannot be more than one.

A Binary Search Tree is in balance when the difference in height between left and right subtrees is less than 2. By keeping balance, the **AVL Tree** ensures a minimum tree height, which means that search, insert, and delete operations can be done really fast.

![[Pasted image 20250906124257.png]]

The two trees above are both Binary Search Trees, they have the same nodes, and the same in-order traversal (alphabetical), but the height is very different because the AVL Tree has balanced itself.

---
## The Balance Factor
A node's balance factor is the difference in subtree heights.

The subtree heights are stored at each node for all nodes in an AVL Tree, and the balance factor is calculated based on its subtree heights to check if the tree has become out of balance.

The height of a subtree is the number of edges between the root node of the subtree and the leaf node farthest down in that subtree.

The **Balance Factor** (BF) for a node (X) is the difference in height between its right and left subtrees. `BF(X)=height(rightSubtree(X))−height(leftSubtree(X))`
Balance factor values
- 0: The node is in balance.
- more than 0: The node is "right heavy".
- less than 0: The node is "left heavy".
If the balance factor is less than -1, or more than 1, for one or more nodes in the tree, the tree is considered not in balance, and a rotation operation is needed to restore balance.

---
