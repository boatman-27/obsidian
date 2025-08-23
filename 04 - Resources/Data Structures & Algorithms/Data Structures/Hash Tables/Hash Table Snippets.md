---
tags:
  - DSA
  - go
date: 2025-08-20T14:56:00
---
```go
package main

import (
	"fmt"
)

// Node for linked list in each bucket
type Node struct {
	key   string
	value int
	next  *Node
}

// HashTable with chaining
type HashTable struct {
	buckets []*Node
	size    int
}

// Create a new hash table with given size
func NewHashTable(size int) *HashTable {
	return &HashTable{
		buckets: make([]*Node, size),
		size:    size,
	}
}

// Simple hash function: sum of char codes % table size
func (ht *HashTable) hash(key string) int {
	sum := 0
	for _, c := range key {
		sum += int(c)
	}
	return sum % ht.size
}

// Insert key-value pair
func (ht *HashTable) Put(key string, value int) {
	index := ht.hash(key)
	head := ht.buckets[index]

	// Check if key exists → update
	for node := head; node != nil; node = node.next {
		if node.key == key {
			node.value = value
			return
		}
	}

	// Insert at head (chaining)
	newNode := &Node{key: key, value: value, next: head}
	ht.buckets[index] = newNode
}

// Get value by key, returns -1 if not found
func (ht *HashTable) Get(key string) int {
	index := ht.hash(key)
	for node := ht.buckets[index]; node != nil; node = node.next {
		if node.key == key {
			return node.value
		}
	}
	return -1 // not found
}

// Delete key from table
func (ht *HashTable) Delete(key string) {
	index := ht.hash(key)
	head := ht.buckets[index]

	var prev *Node
	for node := head; node != nil; node = node.next {
		if node.key == key {
			if prev == nil {
				// removing head
				ht.buckets[index] = node.next
			} else {
				prev.next = node.next
			}
			return
		}
		prev = node
	}
}

// Print the table (for visualization)
func (ht *HashTable) Print() {
	for i, node := range ht.buckets {
		fmt.Printf("[%d]: ", i)
		for n := node; n != nil; n = n.next {
			fmt.Printf("(%s:%d) -> ", n.key, n.value)
		}
		fmt.Println("nil")
	}
}

func main() {
	ht := NewHashTable(10)

	ht.Put("Bob", 42)
	ht.Put("Alice", 100)
	ht.Put("Eve", 77)
	ht.Put("Mallory", 55)

	fmt.Println("Bob's value:", ht.Get("Bob"))
	fmt.Println("Eve's value:", ht.Get("Eve"))

	ht.Delete("Alice")
	fmt.Println("After deleting Alice:")

	ht.Print()
}

```