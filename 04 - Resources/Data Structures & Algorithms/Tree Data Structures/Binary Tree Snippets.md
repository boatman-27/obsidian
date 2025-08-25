---
tags:
  - DSA
  - go
date: 2025-08-25T14:19:00
---
## 1. **Declaration & Initialization**
```go
package main

// TreeNode represents a single node in a binary tree.
// Each node holds an integer value (Data) and may have
// a left and/or right child node.
type TreeNode struct {
	Data      int
	LeftNode  *TreeNode
	RightNode *TreeNode
}

func main() {
	// Create the root node with value 1
	root := &TreeNode{Data: 1}

	// Create two child nodes
	nodeA := &TreeNode{Data: 2}
	nodeB := &TreeNode{Data: 3}

	// Attach child nodes to the root
	root.LeftNode = nodeA
	root.RightNode = nodeB

	// At this point, the tree looks like:
	//       1
	//      / \
	//     2   3
}
```
## 2. **Traversal**
## 2.1 PreOrder
```go
package main

import "fmt"

// TreeNode represents a node in a binary tree.
// Each node holds an integer (Data) and has pointers
// to a left and right child (which may be nil).
type TreeNode struct {
	Data      int
	LeftNode  *TreeNode
	RightNode *TreeNode
}

// PreOrder traverses the tree using "pre-order" traversal.
// Pre-order means: visit the current node first, then
// recursively traverse the left subtree, then the right subtree.
func (t *TreeNode) PreOrder(node *TreeNode) {
	// Base case: if the current node is nil, just return (nothing to do).
	if node == nil {
		return
	}

	// "Visit" the node: here we print its data.
	fmt.Println(node.Data)

	// Recursively traverse the left subtree.
	t.PreOrder(node.LeftNode)

	// Recursively traverse the right subtree.
	t.PreOrder(node.RightNode)
}
```