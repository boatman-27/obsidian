---
tags:
  - DSA
  - go
date: 2025-08-20T11:42:00
---
## Implementing Queues using linked lists
```go
package main

import "fmt"

type Node struct {
	Data int
	Next *Node
}

type Queue struct {
	head   *Node // front of the queue
	tail   *Node // back of the queue
	length int   // number of elements
}

// Enqueue adds an element at the end of the queue (O(1))
func (q *Queue) Enqueue(val int) {
	newNode := &Node{Data: val}

	if q.IsEmpty() {
		// first element → head and tail are the same
		q.head = newNode
		q.tail = newNode
	} else {
		// attach to the current tail and move tail forward
		q.tail.Next = newNode
		q.tail = newNode
	}
	q.length++
}

// Dequeue removes and returns the front element (O(1))
func (q *Queue) Dequeue() int {
	if q.IsEmpty() {
		fmt.Println("queue is empty")
		return -1
	}

	dequeuedNode := q.head
	q.head = q.head.Next
	q.length--

	// if queue is now empty, reset tail
	if q.head == nil {
		q.tail = nil
	}

	return dequeuedNode.Data
}

// Peek returns the front element without removing it
func (q *Queue) Peek() int {
	if q.IsEmpty() {
		fmt.Println("queue is empty")
		return -1
	}
	return q.head.Data
}

// Len returns the number of elements
func (q *Queue) Len() int {
	return q.length
}

// IsEmpty checks if the queue has no elements
func (q *Queue) IsEmpty() bool {
	return q.length == 0
}

// Print displays the queue from head → tail
func (q *Queue) Print() {
	for curr := q.head; curr != nil; curr = curr.Next {
		fmt.Printf("%d -> ", curr.Data)
	}
	fmt.Println("nil")
}

func main() {
	q := &Queue{}

	q.Enqueue(10)
	q.Enqueue(20)
	q.Enqueue(30)

	q.Print()                // 10 -> 20 -> 30 -> nil
	fmt.Println(q.Peek())    // 10
	fmt.Println(q.Dequeue()) // 10
	q.Print()                // 20 -> 30 -> nil
	fmt.Println(q.Len())     // 2
}
```
---
## Implementing Queues using arrays
```go
package main

import "fmt"

// ArrQueue represents a queue backed by a slice.
type ArrQueue struct {
	data []int
}

// Enqueue adds an element at the end (O(1) amortized).
func (q *ArrQueue) Enqueue(val int) {
	q.data = append(q.data, val)
}

// Dequeue removes and returns the front element.
// If queue is empty, returns -1 and prints a warning.
func (q *ArrQueue) Dequeue() int {
	if q.IsEmpty() {
		fmt.Println("queue is empty")
		return -1
	}

	firstElm := q.data[0]

	q.data = q.data[1:]

	return firstElm
}

// Peek returns the front element without removing it.
func (q *ArrQueue) Peek() int {
	if q.IsEmpty() {
		fmt.Println("queue is empty")
		return -1
	}
	return q.data[0]
}

// Len returns the number of elements.
func (q *ArrQueue) Len() int {
	return len(q.data)
}

// IsEmpty checks if the queue has no elements.
func (q *ArrQueue) IsEmpty() bool {
	return q.Len() == 0
}

func main() {
	q := &ArrQueue{}

	q.Enqueue(10)
	q.Enqueue(20)
	q.Enqueue(30)

	fmt.Println(q.Peek())    // 10
	fmt.Println(q.Dequeue()) // 10
	fmt.Println(q.Dequeue()) // 20
	fmt.Println(q.Dequeue()) // 30
	fmt.Println(q.Dequeue()) // queue is empty → -1
}
```