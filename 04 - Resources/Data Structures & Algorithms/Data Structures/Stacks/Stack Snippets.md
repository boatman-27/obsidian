---
tags:
  - DSA
  - go
date: 2025-08-19T22:11:00
---
## Implementing Stacks using linked lists
```go
package main

import "fmt"

// Node represents a single element in the stack.
type Node struct {
	Data int   // The value stored in the node
	Next *Node // Pointer to the next node in the stack
}

// Stack represents a linked-list-based stack.
type Stack struct {
	head   *Node // Points to the top of the stack
	length int   // Tracks the number of elements in the stack
}

// Push adds a new value onto the top of the stack.
func (s *Stack) Push(val int) {
	// Create a new node pointing to the current head
	newNode := &Node{Data: val, Next: s.head}
	// Update head to the new node
	s.head = newNode
	// Increment length
	s.length++
}

// Pop removes and returns the value at the top of the stack.
func (s *Stack) Pop() int {
	// If stack is empty, return -1 and print warning
	if s.IsEmpty() {
		fmt.Println("stack is empty")
		return -1
	}

	// Store current head to return its data
	poppedNode := s.head
	// Move head pointer to the next node
	s.head = poppedNode.Next
	// Decrement length
	s.length--
	return poppedNode.Data
}

// Peek returns the value at the top of the stack without removing it.
func (s *Stack) Peek() int {
	if s.IsEmpty() {
		fmt.Println("stack is empty")
		return -1
	}
	return s.head.Data
}

// Len returns the number of elements in the stack.
func (s *Stack) Len() int {
	return s.length
}

// IsEmpty checks if the stack has no elements.
func (s *Stack) IsEmpty() bool {
	return s.length == 0
}

// Optional helper to print the stack (top to bottom)
func (s *Stack) Print() {
	current := s.head
	for current != nil {
		fmt.Printf("%d -> ", current.Data)
		current = current.Next
	}
	fmt.Println("nil")
}

// Example usage
func main() {
	stack := &Stack{}

	stack.Push(10)
	stack.Push(20)
	stack.Push(30)

	stack.Print()         // 30 -> 20 -> 10 -> nil
	fmt.Println(stack.Pop()) // 30
	fmt.Println(stack.Peek()) // 20
	fmt.Println(stack.Len())  // 2
}

```
---
## Implementing Stacks using arrays
```go
package main

import "fmt"

// Stack represents a slice-based stack of integers.
type Stack struct {
	data []int
}

// Push adds a value on top of the stack.
func (s *Stack) Push(val int) {
	s.data = append(s.data, val)
}

// Pop removes and returns the top value. Returns error if empty.
func (s *Stack) Pop() (int, error) {
	if len(s.data) == 0 {
		return -1, fmt.Errorf("stack is empty")
	}
	val := s.data[len(s.data)-1]
	s.data = s.data[:len(s.data)-1]
	return val, nil
}

// Peek returns the top value without removing it. Returns error if empty.
func (s *Stack) Peek() (int, error) {
	if len(s.data) == 0 {
		return -1, fmt.Errorf("stack is empty")
	}
	return s.data[len(s.data)-1], nil
}

// Len returns the number of elements in the stack.
func (s *Stack) Len() int {
	return len(s.data)
}

// IsEmpty checks if the stack has no elements.
func (s *Stack) IsEmpty() bool {
	return len(s.data) == 0
}

// Print prints the stack (top -> bottom)
func (s *Stack) Print() {
	for i := len(s.data) - 1; i >= 0; i-- {
		fmt.Printf("%d -> ", s.data[i])
	}
	fmt.Println("nil")
}

func main() {
	stack := &Stack{}

	stack.Push(10)
	stack.Push(20)
	stack.Push(30)

	stack.Print() // 30 -> 20 -> 10 -> nil
	val, _ := stack.Pop()
	fmt.Println(val) // 30
	top, _ := stack.Peek()
	fmt.Println(top)         // 20
	fmt.Println(stack.Len()) // 2
}
```