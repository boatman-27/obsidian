---
tags:
  - DSA
  - go
date: 2025-08-18T12:30:00
---
This document will contain all the array snippets written in Golang
## 1. **Declaration & Initialization**
``` go
package main

func main() {
	// Static array (fixed size)
	var staticArray [4]int

	// Slice (dynamic array)
	var dynamicArray []any

	// Initialized static array
	initializedArray := [4]int{1, 2, 3, 5}

	// Initialized slice
	initializedSlice := []int{10, 20, 30}
}
```
---
## 2. **Accessing Elements**
```go 
package main

import "fmt"

func main() {
	initializedArray := [4]int{1, 2, 3, 5}
	fmt.Println(initializedArray[0]) // prints 1

	initializedArray[2] = 4
	fmt.Println(initializedArray) // prints [1,2,4,5]
}
```
---
## 3. **Traversal**
```go
func main() {
	initializedArray := [4]int{1, 2, 3, 5}

	// classic for loop
	for i := 0; i < len(initializedArray); i++ {
		fmt.Println(initializedArray[i])
	}

	// Range with index
	for i := range len(initializedArray) {
		fmt.Println(initializedArray[i])
	}

	// Range with index and value, either can be _ to ignore
	for index, value := range initializedArray {
		fmt.Println(index, value)
	}
}
```
---
## 4. **Insertion**

### 4.1 **Appending to the end (slices)**
```go 
package main

import "fmt"

func main() {
	var dynamicSlice []any
	staticArray := [4]int{1, 2, 3, 5}

	// Append elements to slice
	dynamicSlice = append(dynamicSlice, "first elm")
	dynamicSlice = append(dynamicSlice, 2)

	fmt.Println("Slice after appending:", dynamicSlice)
	fmt.Println("Static array remains unchanged:", staticArray)
}

```
**Notes:**
- Only slices (`[]type`) can grow dynamically.
- Static arrays cannot be appended to; their size is fixed.
### 4.2 **Insert at a specific index (slices, with shifting)**
```go
package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5}
	index := 2
	value := 99

	// Insert value at index 2, shifting the rest
	slice = append(slice[:index], append([]int{value}, slice[index:]...)...)

	fmt.Println("After inserting 99 at index 2:", slice)
	// Output: [1 2 99 3 4 5]
}
```
**Notes:**
- This only works for slices.
- The elements after the insertion index are automatically shifted right.
- Static arrays cannot accommodate new elements, so “shifting” in the sense of increasing size isn’t possible.
---
## 5. **Deletion**
### 5.1 **Remove the last element from a slice.**
```go
package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5}
	index := 2
	value := 99

	slice = slice[:len(slice)-1]
	fmt.Println(slice)
	// output [1, 2, 3, 4]
}
```

### 5.2 **Remove from a specific index.**
```go
package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5}
	index := 2
	value := 99

	slice = append(slice[:index], slice[index+1:]...)
	fmt.Println(slice)
	// output [1, 2, 4, 5]
}
```
---
## 6. **Searching**
```go
package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5}
	toFind := 3
	found := false

	for index, value := range slice {
		if value == toFind {
			fmt.Printf("found at: %d", index)
			found = true
			break
		}
	}

	if !found {
		fmt.Println("not found")
	}
}
```
---
## 7. Multidimensional Arrays 
```go
package main

import "fmt"

func main() {
	matrix := [2][3]int {
	{1, 2, 3},
		{4, 5, 6},
	}

	// Access element
	fmt.Println("Element at [1][2]:", matrix[1][2]) // prints 6

	// Traversal
	for i := range matrix {
		for j := range matrix[i] {
			fmt.Print(matrix[i][j], " ")
		}
		fmt.Println()
	}
	// 1 2 3 
	// 4 5 6 
}
```