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
