---
tags:
  - DSA
  - go
date: 2025-08-25T22:20:00
---
BFS is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.

## Pointer Implementation
```go
// TreeNode represents a single node in a binary tree.
// Each node holds an integer value (Data) and may have
// a left and/or right child node.
type TreeNode struct {
	Data      int
	LeftNode  *TreeNode
	RightNode *TreeNode
}

func BFS(root *TreeNode) {
	if root == nil {
		return
	}

	// queue is just a slice of *TreeNode
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		// Pop the first element
		node := queue[0]
		queue = queue[1:]

		// "Visit" the node
		fmt.Println(node.Data)

		// Enqueue children if they exist
		if node.LeftNode != nil {
			queue = append(queue, node.LeftNode)
		}
		if node.RightNode != nil {
			queue = append(queue, node.RightNode)
		}
	}
}


```

## Array Implementation
```go
// getLeftNodeIndex calculates the index of the left child
// in an array-based binary tree representation.
// Formula: left = 2*index + 1
func getLeftNodeIndex(rootIndex int) int {
	return 2*rootIndex + 1
}

// getRightNodeIndex calculates the index of the right child
// in an array-based binary tree representation.
// Formula: right = 2*index + 2
func getRightNodeIndex(rootIndex int) int {
	return 2*rootIndex + 2
}

func BFS(index int, tree []rune) {
	// If the root index is invalid or empty, nothing to do
	if index >= len(tree) || tree[index] == ' ' {
		return
	}

	// Queue of node indexes, starting with the root
	queue := []int{index}

	// Process nodes until the queue is empty
	for len(queue) != 0 {
		// Dequeue: take the first index out
		root := queue[0]
		queue = queue[1:]

		// "Visit" the node by printing its data
		fmt.Println(string(tree[root]))

		// Enqueue left child if it's valid and not empty
		leftNodeIndex := getLeftNodeIndex(root)
		if leftNodeIndex < len(tree) && tree[leftNodeIndex] != ' ' {
			queue = append(queue, leftNodeIndex)
		}

		// Enqueue right child if it's valid and not empty
		rightNodeIndex := getRightNodeIndex(root)
		if rightNodeIndex < len(tree) && tree[rightNodeIndex] != ' ' {
			queue = append(queue, rightNodeIndex)
		}
	}
}

```
