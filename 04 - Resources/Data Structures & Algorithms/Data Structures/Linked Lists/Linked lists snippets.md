---
tags:
  - DSA
  - go
date: 2025-08-18T14:21:00
---
This document will contain all the linked list snippets written in Golang
## 1. **Declaration**
### 1.1 Single linked list
```go
package main

type Node struct {
	Data int
	Next *Node
}

func single() {
	head := &Node{Data: 1}
	node2 := &Node{Data: 2}
	node3 := &Node{Data: 3}
	node4 := &Node{Data: 4}
	tail := &Node{Data: 5, Next: nil}

	head.Next = node2
	node2.Next = node3
	node3.Next = node4
	node4.Next = tail
}
```
### 1.2 Doubly linked list
```go
package main

type Node struct {
	Prev *Node
	Data int
	Next *Node
}

func double() {
	head := &Node{Data: 1, Prev: nil}
	node2 := &Node{Data: 2, Prev: head}
	node3 := &Node{Data: 3, Prev: node2}
	node4 := &Node{Data: 4, Prev: node3}
	tail := &Node{Data: 5, Next: nil, Prev: node4}

	head.Next = node2
	node2.Next = node3
	node3.Next = node4
	node4.Next = tail
}
```
### 1.3 Circular linked list
```go
package main

type Node struct {
	Prev *Node
	Data int
	Next *Node
}

func circular() {
	head := &Node{Data: 1}
	node2 := &Node{Data: 2}
	node3 := &Node{Data: 3}
	node4 := &Node{Data: 4}
	tail := &Node{Data: 5}

	// next
	head.Next = node2
	node2.Next = node3
	node3.Next = node4
	node4.Next = tail
	tail.Next = head

	// prev
	head.Prev = tail
	node2.Prev = head
	node3.Prev = node2
	node4.Prev = node3
	tail.Prev = node4
}
```
---
## 2. **Insertion**
### 2.1 Single linked list
#### 2.1.1 Insert at Beginning 
```go
package main

import "fmt"

// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type Node struct {
	Data int
	Next *Node
}

// SLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type SLinkedList struct {
	head *Node
}

// InsertAtBeginning puts a new node at the start of the list.
// 1. Create the new node.
// 2. Point its Next to the current head (whatever that is).
// 3. Move the head to point at the new node.
func (s *SLinkedList) InsertAtBeginning(val int) {
	newNode := &Node{Data: val, Next: s.head}
	s.head = newNode
}
```
#### 2.1.2 Insert at Tail 
```go
package main

import "fmt"

// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type Node struct {
	Data int
	Next *Node
}

// SLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type SLinkedList struct {
	head *Node
}

// InsertAtTail puts a new node at the end of the list.
// 1. Create the new node (its Next = nil by default, since it’s the tail).
// 2. If the list is empty, the new node becomes head.
// 3. Otherwise, walk the list until you find the current tail.
// 4. Point the current tail’s Next to the new node.
func (s *SLinkedList) InsertAtTail(val int) {
	newNode := &Node{Data: val}
	if s.head == nil {
		// Empty list, new node is now the head.
		s.head = newNode
		return
	}

	current := s.head
	for current.Next != nil {
		current = current.Next
	}
	current.Next = newNode
}
```
#### 2.1.3 Insert At Index
```go
package main

import "fmt"

// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type Node struct {
	Data int
	Next *Node
}

// SLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type SLinkedList struct {
	head *Node
}

func (s *SLinkedList) InsertAtIndex(val, index int) {
	newNode := &Node{Data: val}

	// Case 1: insert at the very start
	if index == 0 {
		newNode.Next = s.head
		s.head = newNode
		return
	}

	// Case 2: if the list is empty but index > 0,
	// the index is invalid. Just bail out.
	if s.head == nil {
		fmt.Println("Index out of range")
		return
	}

	// Walk the list until the node BEFORE the insertion point
	current := s.head
	count := 0
	for current != nil && count < index-1 {
		current = current.Next
		count++
	}

	// If we ran out of nodes before reaching index-1,
	// the index was too large.
	if current == nil {
		fmt.Println("Index out of range")
		return
	}

	// Insert the new node in the chain
	newNode.Next = current.Next
	current.Next = newNode
}
```

### 2.2 Double linked list
#### 2.2.1 Insert at Beginning
```go
package main

import "fmt"


// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type dNode struct {
	Prev *dNode
	Data int
	Next *dNode
}

// DLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type DLinkedList struct {
	head *dNode
}

func (d *DLinkedList) InsertAtBeginning(val int) {
	newNode := &dNode{Data: val, Next: d.head}
	
	// If list not empty, link the old head back to newNode
	if d.head != nil {
		newNode.Next = d.head
		d.head.Prev = newNode
	}

	d.head = newNode
}
```
#### 2.2.2 Insert at Tail 
```go
package main

import "fmt"


// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type dNode struct {
	Prev *dNode
	Data int
	Next *dNode
}

// DLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type DLinkedList struct {
	head *dNode
}

func (d *DLinkedList) InsertAtTail(val int) {
	// Create a new node with the given value.
	newNode := &dNode{Data: val}

	// Case 1: if the list is empty, the new node becomes the head.
	if d.head == nil {
		d.head = newNode
		return // nothing else to do
	}

	// Start at the head node
	current := d.head

	// Traverse the list until we reach the last node (whose Next is nil)
	for current.Next != nil {
		current = current.Next
	}

	// Link the new node to the last node
	newNode.Prev = current // new node's previous pointer points to current tail
	current.Next = newNode // current tail's next pointer points to new node
}
```
#### 2.2.3 Insert at Index 
```go
package main

import "fmt"


// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type dNode struct {
	Prev *dNode
	Data int
	Next *dNode
}

// DLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type DLinkedList struct {
	head *dNode
}

func (d *DLinkedList) InsertAtIndex(val, index int) {
	newNode := &dNode{Data: val}

	// Case 1: inserting at the head
	if index == 0 {
		newNode.Next = d.head // new node points to current head (may be nil)
		if d.head != nil {    // only update Prev if the list is not empty
			d.head.Prev = newNode
		}
		d.head = newNode // move head pointer to the new node
		return
	}

	// Case 2: list is empty and index > 0, invalid insertion
	if d.head == nil {
		fmt.Println("Index out of range")
		return
	}

	// Walk to the node just before the target index
	current := d.head
	count := 0
	for count < index-1 && current.Next != nil {
		current = current.Next
		count++
	}

	// If index is beyond the end of the list
	if count < index-1 {
		fmt.Println("Index out of range")
		return
	}
	// Link the new node into the list
	newNode.Next = current.Next // new node points forward to the next node
	newNode.Prev = current      // new node points back to current
	if current.Next != nil {    // update Prev of the node after new node, if it exists
		current.Next.Prev = newNode
	}
	current.Next = newNode // current now points forward to the new node
}
```
### 2.3 Circular linked list
#### 2.3.1 Insert at Beginning
```go
package main

// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type cNode struct {
	Prev *cNode
	Data int
	Next *cNode
}

// CLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type CLinkedList struct {
	head *cNode
}

func (c *CLinkedList) InsertAtBeginning(val int) {
	newNode := &cNode{Data: val}

	// Case 1: list is empty
	if c.head == nil {
		newNode.Next = newNode // points to itself
		newNode.Prev = newNode // points to itself
		c.head = newNode
		return
	}

	// Case 2: list has at least one node
	tail := c.head.Prev
	newNode.Prev = tail
	newNode.Next = c.head
	c.head.Prev = newNode
	tail.Next = newNode

	c.head = newNode
}

```
#### 2.3.2 Insert At Tail
```go
package main

// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type cNode struct {
	Prev *cNode
	Data int
	Next *cNode
}

// CLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type CLinkedList struct {
	head *cNode
}

func (c *CLinkedList) InsertAtTail(val int) {
	newNode := &cNode{Data: val}

	// Case 1: list is empty
	if c.head == nil {
		newNode.Next = newNode // points to itself
		newNode.Prev = newNode // points to itself
		c.head = newNode
		return
	}

	// Case 2: list has at least one node
	oldTail := c.head.Prev
	oldTail.Next = newNode
	newNode.Prev = oldTail
	newNode.Next = c.head
	c.head.Prev = newNode
}
```
#### 2.3.3 Insert at Index 
```go
package main

// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type cNode struct {
	Prev *cNode
	Data int
	Next *cNode
}

// CLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type CLinkedList struct {
	head *cNode
}

func (c *CLinkedList) InsertAtIndex(val, index int) {
	newNode := &cNode{Data: val}
	// Case 1: list is empty
	if c.head == nil {
		newNode.Next = newNode // points to itself
		newNode.Prev = newNode // points to itself
		c.head = newNode
		return
	}

	count := 0
	current := c.head
	for count < index-1 {
		current = current.Next
		count++
	}

	prevNode := current.Prev
	prevNode.Next = newNode
	newNode.Prev = prevNode
	newNode.Next = current
	current.Prev = newNode

	// If inserting at the beginning, update head pointer
	if index == 0 {
		c.head = newNode
	}
}
```
---
## 3. **Traversal**
### 3.1 Single linked list
```go 
// Print just walks through the list from head to tail
// and prints each node’s Data value.
func (s *SLinkedList) Print() {
	current := s.head
	for current != nil {
		fmt.Printf("%d -> ", current.Data)
		current = current.Next
	}
	fmt.Println("nil")
}
```
### 3.2 Doubly linked list
```go
func (d *DLinkedList) PrintFromHead() {
	current := d.head
	for current != nil {
		fmt.Printf("%d -> ", current.Data)
		current = current.Next
	}
	fmt.Println("nil")
}

func (d *DLinkedList) PrintFromTail() {
	if d.head == nil {
		fmt.Println("nil")
		return
	}

	// Walk to tail
	current := d.head
	for current.Next != nil {
		current = current.Next
	}

	// Now print backwards
	for current != nil {
		fmt.Printf("%d <- ", current.Data)
		current = current.Prev
	}
	fmt.Println("nil")
}

func main() {
	list := &DLinkedList{}
	
	// Insert at beginning
	list.InsertAtBeginning(1)
	list.InsertAtBeginning(2)
	list.InsertAtBeginning(3)

	// Insert at tail
	list.InsertAtTail(4)
	list.InsertAtTail(5)

	// Print full list
	list.PrintFromTail() // 5 <- 4 <- 1 <- 2 <- 3 <- nil
	list.PrintFromHead() // 3 -> 2 -> 1 -> 4 -> 5 -> nil

}
```
### 3.2.3 Circular linked list
```go
func (c *CLinkedList) PrintFromHead() {
	if c.head == nil {
		fmt.Println("empty")
		return
	}

	current := c.head
	for {
		fmt.Printf("%d -> ", current.Data)
		current = current.Next
		if current == c.head {
			break
		}
	}
}

func (c *CLinkedList) PrintFromTail() {
	if c.head == nil {
		fmt.Println("empty")
		return
	}

	// Go to the tail (one step back from head in circular DLL)
	current := c.head.Prev
	for {
		fmt.Printf("%d <- ", current.Data)
		current = current.Prev
		if current == c.head.Prev {
			break
		}
	}
}

func main() {
	list := &CLinkedList{}

	list.InsertAtBeginning(1)
	list.InsertAtBeginning(2)
	list.InsertAtBeginning(3)

	list.InsertAtTail(4)
	list.InsertAtTail(5)

	list.PrintFromHead() // 3 -> 2 -> 1 -> 4 -> 5 -> 
	fmt.Println()
	list.PrintFromTail() // 5 <- 4 <- 1 <- 2 <- 3 <-
}
```
## 4. **Deletion**
### 4.1 Single linked list
#### 4.1.1 Delete head
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type Node struct {
	Data int
	Next *Node
}

// SLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type SLinkedList struct {
	head *Node
}

func (s *SLinkedList) DeleteHead() {
	if s.head == nil {
		return // empty list
	}

	s.head = s.head.Next
}
```
#### 4.1.2 Delete tail
```go 
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type Node struct {
	Data int
	Next *Node
}

// SLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type SLinkedList struct {
	head *Node
}

func (s *SLinkedList) DeleteTail() {
	if s.head == nil {
		return // empty list
	}

	if s.head.Next == nil {
		s.head = nil // only one element
		return
	}

	current := s.head
	for current.Next != nil {
		current = current.Next
	}

	current.Next = nil
}
```
#### 4.1.3 Delete Specific Node 
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node.
type Node struct {
	Data int
	Next *Node
}

// SLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type SLinkedList struct {
	head *Node
}

func (s *SLinkedList) DeleteSpecificNode(nodeToDelete *Node) {
	if s.head == nil {
		return // empty list
	}

	// Case 1: deleting the head
	if s.head == nodeToDelete {
		s.head = s.head.Next
		return
	}

	// Case 2: deleting something else
	current := s.head
	for current.Next != nil && current.Next != nodeToDelete {
		current = current.Next
	}

	if current.Next == nil {
		fmt.Println("node doesn’t exist")
		return
	}
	current.Next = current.Next.Next // jumps the one to delete. current -> current.Next(one to Delete) -> current.Next.Next (after the node to be deleted )
	// reconnects current with the node that after the deleted one
}
```
### 4.2 Double linked list
#### 4.2.1 Delete head
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type dNode struct {
	Prev *dNode
	Data int
	Next *dNode
}

// DLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type DLinkedList struct {
	head *dNode
}

// DeleteHead removes the first node from the doubly linked list.
func (d *DLinkedList) DeleteHead() {
	// Case 1: empty list, nothing to delete
	if d.head == nil {
		return
	}

	// Case 2: only one node in the list
	if d.head.Next == nil {
		d.head = nil // set head to nil, list is now empty
		return
	}

	// Case 3: more than one node
	d.head = d.head.Next   // move head to the next node
	d.head.Prev = nil      // remove the back-link to the old head
}
```
#### 4.2.2 Delete tail
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type dNode struct {
	Prev *dNode
	Data int
	Next *dNode
}

// DLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type DLinkedList struct {
	head *dNode
}

// DeleteTail removes the last node from the doubly linked list.
func (d *DLinkedList) DeleteTail() {
	// Case 1: empty list, nothing to delete
	if d.head == nil {
		return
	}

	// Case 2: only one node in the list
	if d.head.Next == nil {
		d.head = nil // list becomes empty
		return
	}

	// Case 3: more than one node
	// Traverse to the last node (tail)
	current := d.head
	for current.Next != nil {
		current = current.Next
	}

	// current is now the tail node
	newTail := current.Prev // get the node before the tail
	newTail.Next = nil      // disconnect the old tail
	current.Prev = nil      // clear the backwards pointer (cleanup purposes :)) 
}
```
#### 4.2.3 Delete Specific Node
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type dNode struct {
	Prev *dNode
	Data int
	Next *dNode
}

// DLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type DLinkedList struct {
	head *dNode
}


func (d *DLinkedList) DeleteSpecificNode(nodeToDelete *dNode) {
	// Case 1: empty list, nothing to delete
	if d.head == nil {
		return
	}

	// Case 2: deleting the head
	if d.head == nodeToDelete {
		if d.head.Next == nil {
			d.head = nil // set head to nil, list is now empty
			return
		}

		d.head = d.head.Next // move head to the next node
		d.head.Prev = nil    // remove the back-link to the old head
		return
	}

	// Case 3: more than one node
	current := d.head
	for current != nil && current != nodeToDelete {
		current = current.Next
	}

	if current == nil {
		fmt.Println("node doesn't exist")
		return
	}

	// unlink `current`
	prevNode := current.Prev
	prevNode.Next = current.Next // links prev to node after deleted node 

	if current.Next != nil { // important check: avoid nil dereference at tail
		current.Next.Prev = prevNode // links node after deleted with node before deleted
	}

	// clean up current
	current.Next = nil
	current.Prev = nil
}
```
### 4.3 Circular linked list
#### 4.3.1 Delete head
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type cNode struct {
	Prev *cNode
	Data int
	Next *cNode
}

// CLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type CLinkedList struct {
	head *cNode
}


func (c *CLinkedList) DeleteHead() {
	if c.head == nil {
		return // empty list
	}

	// Only one node
	if c.head.Next == c.head {
		c.head = nil
		return
	}

	tail := c.head.Prev     // last node
	nextNode := c.head.Next // second node

	tail.Next = nextNode // rewire tail to skip old head
	nextNode.Prev = tail // rewire second node's prev

	c.head = nextNode // move head forward
}
```
#### 4.3.2 Delete tail
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type cNode struct {
	Prev *cNode
	Data int
	Next *cNode
}

// CLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type CLinkedList struct {
	head *cNode
}

func (c *CLinkedList) DeleteTail() {
	if c.head == nil {
		return // empty list
	}

	// Only one node in the list
	if c.head.Next == c.head {
		c.head = nil // list becomes empty
		return
	}

	// General case: more than one node
	tail := c.head.Prev  // current tail
	newTail := tail.Prev // node before tail

	newTail.Next = c.head // skip old tail
	c.head.Prev = newTail // maintain circular prev link

	// cleanup
	tail.Next = nil
	tail.Prev = nil
}
```
#### 4.3.3 Delete specific node
```go
// Node represents a single element in the linked list.
// It stores some data and a pointer to the next node and previous.
type cNode struct {
	Prev *cNode
	Data int
	Next *cNode
}

// CLinkedList is just a wrapper around the head pointer.
// This way, the list stores the starting point of the chain.
type CLinkedList struct {
	head *cNode
}

func (c *CLinkedList) DeleteSpecificNode(nodeToDelete *cNode) {
	if c.head == nil {
		return // empty list
	}

	// Only one node in the list
	if c.head == nodeToDelete && c.head.Next == c.head {
		c.head.Next = nil
		c.head.Prev = nil
		c.head = nil
		return
	}

	// Deleting the head (but more than one node)
	if c.head == nodeToDelete {
		tail := c.head.Prev
		newHead := c.head.Next

		tail.Next = newHead
		newHead.Prev = tail

		// cleanup old head
		c.head.Next = nil
		c.head.Prev = nil

		c.head = newHead
		return
	}

	// Deleting a node that is not head
	current := c.head.Next
	for current != c.head && current != nodeToDelete {
		current = current.Next
	}

	if current == c.head {
		fmt.Println("node not found")
		return
	}

	// bypass current
	current.Prev.Next = current.Next
	current.Next.Prev = current.Prev

	// cleanup current
	current.Next = nil
	current.Prev = nil
}
```

## 5. **Length**
### 5.1 Single linked list
```go
func (s *SLinkedList) GetLength() int {
	count := 0
	current := s.head
	for current != nil {
		count++
		current = current.Next
	}
	return count

}
```
### 5.2 Double linked list
```go
func (d *DLinkedList) GetLength() int {
	count := 0
	current := d.head
	for current != nil {
		count++
		current = current.Next
	}
	return count
}
```
### 5.3 Circular linked list
```go
func (c *CLinkedList) GetLength() int {
	if c.head == nil {
		return 0
	}

	count := 1
	current := c.head.Next
	for current != c.head {
		count++
		current = current.Next
	}
	return count
}
```
## 6. **Reverse**
### 6.1 Single linked list
```go
func (s *SLinkedList) Reverse() {
	if s.head == nil || s.head.Next == nil {
		return
	}

	var prev *Node = nil
	current := s.head

	for current != nil {
		next := current.Next     // save the next node
		current.Next = prev      // reverse the link
		prev = current           // move prev forward
		current = next           // move current forward
	}

	s.head = prev               // update head to new first node
}
```
### 6.2 Double linked list
```go
func (d *DLinkedList) Reverse() {
	// Case 1: empty list or single node → nothing to do
	if d.head == nil || d.head.Next == nil {
		return
	}

	current := d.head
	var temp *dNode

	// Traverse and swap Next <-> Prev for each node
	for current != nil {
		temp = current.Next // save the next node
		current.Next = current.Prev
		current.Prev = temp
		current = temp // move to the original next
	}

	// After the loop, temp is nil, but the new head
	// is the *last non-nil node we touched*
	if temp != nil {
		d.head = temp.Prev
	}
}
```
### 6.3 Circular linked lIS
```go
func (c *CLinkedList) Reverse() {
	if c.head == nil || c.head.Next == c.head {
		return // empty or single-node list
	}

	current := c.head
	var temp *cNode
	for {
		// swap next and prev
		temp = current.Next
		current.Next = current.Prev
		current.Prev = temp

		// move forward
		current = temp
		if current == c.head {
			break
		}
	}

	// update head (old tail is new head)
	c.head = c.head.Prev
}
```