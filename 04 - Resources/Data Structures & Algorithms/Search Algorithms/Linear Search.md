---
tags:
  - DSA
  - go
date: 2025-08-20T23:38:00
---
Linear search is one of the simplest search algorithms. In this method, every element in an array is checked sequentially starting from the first until a match is found or all elements have been checked. It is also known as sequential search. 

It works on both sorted and unsorted lists, and does not need any preconditioned list for the operation. However, its efficiency is lesser as compared to other search algorithms since it checks all elements one by one.

## Implementation
### With arrays
```go
package main

import "fmt"

// linearSearch scans through the array from left to right
// and returns the index of the first occurrence of val.
// If val is not found, it returns -1.
func linearSearch(val int, arr []int) int {
	for index, value := range arr {
		// Check if the current element matches the target value
		if value == val {
			return index // Found it! Return its position.
			break        // Redundant since return already exits, but harmless.
		}
	}

	// If we make it this far, val wasn’t in the array
	return -1
}

func main() {
	// Example array to search in
	arr := []int{5, 3, 4, 9, 10, 12, 27, 100, 2987}

	// Value we want to search for
	valToFind := 10

	// Call linearSearch and capture the index result
	index := linearSearch(valToFind, arr)

	// Print the index (or -1 if not found)
	fmt.Print(index)
}
```
### With Linked Lists 
```go
package main

import (
	"fmt"
)

// Node represents a single element in the linked list
type Node struct {
	Data int
	Next *Node
}

// LinkedList represents the whole linked list with a pointer to the head node
type LinkedList struct {
	head *Node
}

// Add inserts a new node at the beginning of the linked list
func (l *LinkedList) Add(val int) {
	newNode := &Node{Data: val}

	// If list is empty, just point head to the new node
	if l.head == nil {
		l.head = newNode
		return
	}

	// Otherwise, insert new node at the head
	newNode.Next = l.head
	l.head = newNode
}

// LinearSearch scans through the linked list looking for val.
// Returns the index of the node containing val, or -1 if not found.
func (l *LinkedList) LinearSearch(val int) int {
	if l.head == nil {
		fmt.Println("list is empty")
		return -1
	}

	current := l.head
	index := 0

	// Traverse until we hit the end (nil)
	for current != nil {
		if current.Data == val {
			return index
		}
		current = current.Next
		index++
	}

	// Value not found
	return -1
}

func main() {
	list := &LinkedList{}

	// Add some values to the list
	list.Add(10)
	list.Add(20)
	list.Add(30)

	// Search for an existing value
	fmt.Println("Index of 20:", list.LinearSearch(20))

	// Search for a missing value
	fmt.Println("Index of 99:", list.LinearSearch(99))
}
```
### With Circular Linked list
```go
func (l *CircularLinkedList) LinearSearch(val int) int {
	if l.head == nil {
		fmt.Println("list is empty")
		return -1
	}

	current := l.head
	index := 0

	// Traverse until we return to head
	for {
		if current.Data == val {
			return index
		}
		current = current.Next
		index++

		// if we’ve circled back, item isn’t there
		if current == l.head {
			break
		}
	}

	return -1
}
```