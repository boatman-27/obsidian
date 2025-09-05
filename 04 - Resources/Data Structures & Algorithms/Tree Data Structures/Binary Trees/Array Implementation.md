---
tags:
  - DSA
  - go
date: 2025-08-25T21:18:00
---
To avoid the cost of all the shifts in memory that we get from using Arrays, it is useful to implement Binary Trees with pointers from one element to the next, just like Binary Trees are implemented before this point, especially when the Binary Tree is modified often.

But in case we read from the Binary Tree a lot more than we modify it, an Array implementation of a Binary Tree can make sense as it needs less memory, it can be easier to implement, and it can be faster for certain operations due to cache locality.

**Cache Locality** is when the fast cache memory in the computer stores parts of memory that was recently accessed, or when the cache stores parts of memory that is close to the address that is currently accessed. This happens because it is likely that the CPU needs something in the next cycle that is close to what it used in the previous cycle, either close in time or close in space.

Since Array elements are stored contiguously in memory, one element right after the other, computers are sometimes faster when reading from Arrays because the next element is already cached, available for fast access in case the CPU needs it in the next cycle.

This Binary Tree can be stored in an Array starting with the root node R on index 0. The rest of the tree can be built by taking a node stored on index i, and storing its left child node on index 2⋅i+1, and its right child node on index 2⋅i+2.

```go
package main

import "fmt"

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

// getNodeData safely returns the data at a given index in the tree.
// If the index is out of bounds, it returns a space character ' '.
// (Not strictly needed for your traversal functions, but handy.)
func getNodeData(index int, tree []rune) rune {
	if 0 <= index && index < len(tree) {
		return tree[index]
	}
	return ' '
}

// preOrder traversal: Visit node first, then left subtree, then right subtree.
// Order: Node → Left → Right
func preOrder(index int, tree []rune) {
	if index >= len(tree) || tree[index] == ' ' {
		return
	}

	fmt.Println(string(tree[index])) // "visit" current node
	preOrder(getLeftNodeIndex(index), tree)
	preOrder(getRightNodeIndex(index), tree)
}

// inOrder traversal: Traverse left subtree, visit node, then right subtree.
// Order: Left → Node → Right
func inOrder(index int, tree []rune) {
	if index >= len(tree) || tree[index] == ' ' {
		return
	}

	inOrder(getLeftNodeIndex(index), tree)
	fmt.Println(string(tree[index])) // "visit" current node
	inOrder(getRightNodeIndex(index), tree)
}

// postOrder traversal: Traverse left subtree, then right subtree, then visit node.
// Order: Left → Right → Node
func postOrder(index int, tree []rune) {
	if index >= len(tree) || tree[index] == ' ' {
		return
	}

	postOrder(getLeftNodeIndex(index), tree)
	postOrder(getRightNodeIndex(index), tree)
	fmt.Println(string(tree[index])) // "visit" current node
}

func main() {
	// Represent the tree as an array of runes:
	// Index:  0   1   2   3   4   5   6   7   8   9   10  11  12  13
	// Value:  R   A   B   C   D   E   F   ' ' ' ' ' ' ' ' ' '  G
	//
	// Which corresponds to the tree:
	//            R
	//          /   \
	//         A     B
	//        / \   / \
	//       C   D E   F
	//                  \
	//                   G
	binaryTreeArray := []rune{'R', 'A', 'B', 'C', 'D', 'E', 'F', ' ', ' ', ' ', ' ', ' ', ' ', 'G'}

	// Run a pre-order traversal starting at the root (index 0).
	preOrder(0, binaryTreeArray)
}

```