---
tags:
  - DSA
  - go
date: 2025-08-25T23:39:00
---
## Traversal 
```go
// bfs performs a breadth-first traversal (level-order traversal) 
// starting from the given node. It prints the Data value of each node.
func (t *TreeNode) bfs(node *TreeNode) {
	if node == nil {
		// Nothing to traverse if the node is nil
		return
	}

	// Initialize a queue with the starting node
	queue := []*TreeNode{node}

	// Continue until the queue is empty
	for len(queue) != 0 {
		// Dequeue the front element
		node := queue[0]
		queue = queue[1:]

		// Process the current node (print its value)
		fmt.Println(node.Data)

		// Enqueue left child if it exists
		if node.LeftNode != nil {
			queue = append(queue, node.LeftNode)
		}

		// Enqueue right child if it exists
		if node.RightNode != nil {
			queue = append(queue, node.RightNode)
		}
	}
}
```
## Search Operation
```go
// search looks for a node containing the given value in a binary search tree.
// It returns a pointer to the node if found, or nil if not found.
func (t *TreeNode) search(val int) *TreeNode {
	// Base case: if current node is nil or matches the search value
	if t == nil || t.Data == val {
		return t
	}

	// If the value is smaller, search the left subtree
	if val < t.Data {
		return t.LeftNode.search(val)
	}

	// Otherwise, search the right subtree
	return t.RightNode.search(val)
}

// SearchIter searches for a node containing the given value in the binary search tree.
// It uses an iterative approach (loop) instead of recursion.
// Returns a pointer to the node if found, or nil if the value is not in the tree.
func (t *TreeNode) SearchIter(val int) *TreeNode {
	// Start traversal from the current node (the root of the tree/subtree)
	curr := t

	// Keep traversing until you either find the value or hit a nil node
	for curr != nil {
		if val == curr.Data {
			// Value found, return the node
			return curr
		} else if val < curr.Data {
			// If the value is smaller, go left
			curr = curr.LeftNode
		} else {
			// If the value is larger, go right
			curr = curr.RightNode
		}
	}

	// Value not found in the tree
	return nil
}

```
## Min/Max value
```go
// getMin finds the smallest value in the binary search tree.
// It does this by following the left child pointers until no more remain.
func (t *TreeNode) getMin() int {
	current := t

	// The minimum is always the leftmost node
	for current.LeftNode != nil {
		current = current.LeftNode
	}

	return current.Data
}

// getMax finds the largest value in the binary search tree.
// It does this by following the right child pointers until no more remain.
func (t *TreeNode) getMax() int {
	current := t

	// The maximum is always the rightmost node
	for current.RightNode != nil {
		current = current.RightNode
	}

	return current.Data
}
```
## Number of nodes
```go
// countNodesBFS returns the total number of nodes in the tree
// using breadth-first search (level-order traversal).
func (t *TreeNode) countNodesBFS() int {
	if t == nil {
		return 0
	}

	count := 0
	queue := []*TreeNode{t}

	for len(queue) != 0 {
		// Dequeue
		node := queue[0]
		queue = queue[1:]

		// Increment counter instead of printing
		count++

		// Enqueue children
		if node.LeftNode != nil {
			queue = append(queue, node.LeftNode)
		}
		if node.RightNode != nil {
			queue = append(queue, node.RightNode)
		}
	}

	return count
}

// countNodes returns the total number of nodes in the tree (or subtree).
// It works recursively: 
// - if the current node is nil, count is 0
// - otherwise, count = 1 (the current node) + nodes in left subtree + nodes in right subtree
func (t *TreeNode) countNodes() int {
	if t == nil {
		// Base case: no node here
		return 0
	}
	// Count current node (1) + left subtree + right subtree
	return 1 + t.LeftNode.countNodes() + t.RightNode.countNodes()
}
```
## Insert node
```go
// InsertNode inserts a new value into the binary search tree.
// If the tree is empty (t == nil), it creates a new root node and returns it.
// Otherwise, it recursively finds the correct position in the left or right subtree.
// Returns the (possibly new) root pointer so the caller can update their reference if needed.
func (t *TreeNode) InsertNode(val int) *TreeNode {
	if t == nil {
		// Base case: empty spot found, create a new node here
		return &TreeNode{Data: val}
	}

	// If the value is smaller, insert into the left subtree
	if val < t.Data {
		t.LeftNode = t.LeftNode.InsertNode(val)
	} else {
		// If the value is greater or equal, insert into the right subtree
		t.RightNode = t.RightNode.InsertNode(val)
	}

	// Return the unchanged root pointer
	return t
}

```