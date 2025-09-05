---
tags:
  - DSA
date: 2025-08-25T23:22:00
---
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.

- It is called a binary tree because each tree node has a maximum of two children.
- It is called a search tree because it can be used to search for the presence of a number in `O(log(n))` time.

The properties that separate a binary search tree from a regular [[Binary Tree]] is
1. All nodes of left subtree are less than the root node
2. All nodes of right subtree are more than the root node
3. Both subtrees of each node are also BSTs i.e. they have the above two properties

---
## Search Operation
The algorithm depends on the property of BST that if each left subtree has values less than the root and each right subtree has values bigger than the root.

If the value is below the root, we can say for sure that the value is not in the right subtree; we need to only search in the left subtree and if the value is above the root, we can say for sure that the value is not in the left subtree; we need to only search in the right subtree.

---
## Insert Operation
A new key is always inserted at the leaf by maintaining the property of the binary search tree. We start searching for a key from the root until we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node. The below steps are followed while we try to insert a node into a binary search tree:
- Initilize the current node (say, ***currNode or node***) with root node
- Compare the ***key*** with the current node.
- ***Move left*** if the ***key*** is less than or equal to the current node value.
- ***Move right*** if the ***key*** is greater than current node value.
- Repeat steps 2 and 3 until you reach a leaf node.
- Attach the ***new key*** as a left or right child based on the comparison with the leaf node's value.

---
## Delete Operation 
To delete a node, our function must first search the BST to find it.
After the node is found there are three different cases where deleting a node must be done differently.

**How it works:**
1. If the node is a leaf node, remove it by removing the link to it.
2. If the node only has one child node, connect the parent node of the node you want to remove to that child node.
3. If the node has both right and left child nodes: Find the node's in-order successor, change values with that node, then delete it.