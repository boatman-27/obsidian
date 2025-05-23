
## Arrays

An array is a fixed-size, sequential collection of elements of the same type.
### **Key Properties of Arrays**
- Fixed size: Once defined, the size cannot be changed.
- Zero-valued by default (e.g., `[0 0 0]` for `int` arrays).
- Can be initialized inline: `arr := [3]int{1, 2, 3}`.
- Can infer size: `arr := [...]int{1, 2, 3, 4}`.
- Pass-by-value: Arrays are copied when passed to functions.

### Syntax

```go
var arr [5]int // An array of 5 integers
```

```go
package main
import "fmt"

func main() {
    var numbers [3]int // Declare an array of size 3
    numbers[0] = 10    // Assign values
    numbers[1] = 20
    numbers[2] = 30

    fmt.Println(numbers) // Output: [10 20 30]
}
```

---

## Slices

A slice is a dynamically-sized, more flexible version of an array.

When a slice is created, it references an underlying array. If an element is appended to it and the slice has enough capacity, the element is added in place. However, if there isn't enough *capacity*, Go creates a new, larger array (typically doubling the previous *capacity*), copies the elements to the new array, and then appends the new element. The slice's **length** increases by one, while its *capacity* may grow significantly more.

### **Slice Properties**
- Not fixed-size, can grow dynamically.
- Reference to underlying array (modifications affect original).
- `len(slice)`: Number of elements.
- `cap(slice)`: Capacity from the underlying array.

### Syntax

```go
var mySlice []int32 = []int {4, 5, 6}

mySlice = append(mySlice, 7)
```

### Copying a slice

```go
src := []int{1, 2, 3}
dst := make([]int, len(src))
copy(dst, src) // Copies elements
fmt.Println(dst) // Output: [1 2 3]
```

### Iterating over a slice

```go
for i, v := range slice {
    fmt.Println("Index:", i, "Value:", v)
}
```

---
## Maps

A map is a collection of key-value pairs.

### **Properties of Maps**

- Keys must be unique.
- Keys must be comparable (`int`, `string`, etc.).
- Fast lookup compared to slices.

### **Declaring and Initializing Maps**

```go
m := map[string]int{"Alice": 25, "Bob": 30}
```

### **Adding and Accessing Values**

```go
m["Charlie"] = 35 // Add a new key-value pair
fmt.Println(m["Alice"]) // Output: 25
```

### **Checking if a Key Exists**

```go
val, exists := m["Bob"]
if exists {
    fmt.Println("Bob's age is", val)
} else {
    fmt.Println("Bob not found")
}
```

### **Deleting a Key**

```go
delete(m, "Alice")
```

### **Iterating Over a Map**

```go
for key, value := range m {
    fmt.Println("Key:", key, "Value:", value)
}
```

---
## Summary

|Feature|Arrays|Slices|Maps|
|---|---|---|---|
|Fixed size?|✅ Yes|❌ No|❌ No|
|Can grow dynamically?|❌ No|✅ Yes|✅ Yes|
|Ordered?|✅ Yes|✅ Yes|❌ No|
|Supports indexing?|✅ Yes|✅ Yes|❌ No|
|Key-value storage?|❌ No|❌ No|✅ Yes|
