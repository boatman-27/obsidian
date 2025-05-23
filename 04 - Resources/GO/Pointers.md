---
tags:
  - go
date: 2025-03-15T21:34:00
---
In Go, a pointer is a variable that stores the memory address of another variable. Instead of holding data directly, a pointer holds the location of where the data is stored in memory. This allows us to manipulate values at their memory locations, making it efficient to pass large data structures around, such as arrays or structs, without copying the data.

### Syntax of pointers

```go
var ptr *int
```

Here, `ptr` is a pointer to an integer (`int`). The `*` symbol is used to declare a pointer.

### Declaring Pointers

To declare a pointer in Go, you need to specify the type of the value it will point to. A pointer is denoted by the `*` before the type name. By initialising with `new()`, its given a free memory location that `p` now points to.

```go
var p *int32 = new(int32)
```

#### Initialising a Pointer

A pointer is usually initialised with the memory address of a variable, using the address-of operator `&`:

```go
x := 58
ptr := &x  // 'ptr' now holds the memory address of 'x'
```

In this example, `ptr` holds the memory address of `x`.

## Dereferencing Pointers

Dereferencing a pointer means accessing the value stored at the memory address the pointer is pointing to. This is done using the `*` operator.

```go
x := 58
ptr := &x
fmt.Println(*ptr)  // Dereferencing ptr to get the value of x
```

Here, `*ptr` gives us the value stored at the memory address that `ptr` points to, which in this case is `58`.

## Pointer Types

Go pointers can point to variables of any type. These include built-in types, structs, arrays, and slices.

### Pointer to a Struct
```go
type Person struct {
	Name string
	Age uint8
}

p := Person{"Adham", 23}
ptr := &p
```

### Pointer to Array

```go
arr := [3]int{1, 2, 3}
ptr := &arr  // Pointer to an array
```

### Pointer to a Slice

```go
arr := []int{1, 2, 3}
ptr := &arr  // Pointer to a slice
```

## Nil Pointers

In Go, a pointer that is declared but not initialized automatically points to `nil`. A `nil` pointer does not point to any valid memory location.

```go
var ptr *int
fmt.Println(ptr)  // This will print 'nil'
```

You can check if a pointer is `nil` using an `if` statement:
```go
if (ptr == nil) {
	fmt.Println("Pointer is nil")
}
```

## Pointers to Structs

Go allows pointers to structs, which is a common use case for pointers. Structs are composite types that can be large, and using pointers avoids copying them.

```go
type Rectangle struct {
    Width  float64
    Height float64
}

func (r *Rectangle) Area() float64 {
    return r.Width * r.Height
}

r := &Rectangle{Width: 5, Height: 4}
fmt.Println(r.Area())  // Accessing a method using a pointer

```

Here, `r` is a pointer to a `Rectangle`, and the method `Area()` is called via the pointer.
## Pointers and Functions

Pointers are often used when passing large data structures (like arrays, slices, or structs) to functions. Passing pointers avoids copying data, making the function more efficient.

```go
func increment(x *int) {
    *x++
}

num := 58
increment(&num)  // Pass the address of num
fmt.Println(num)  // Outputs: 59

```

In this example, the function `increment` modifies the value of `num` directly by using the pointer `x`.

## Pointer Arithmetic

Go does not allow pointer arithmetic like C or C++. You cannot directly manipulate pointers or add/subtract integers to pointers. This restriction makes Go safer, as it prevents accessing memory outside of the bounds of allocated variables.

```go
int arr[3] = {10, 20, 30};
int *ptr = arr;
ptr++;  // Moves pointer to the next element in C (NOT ALLOWED IN GO)
```

#### How to Work Around This in Go?

```go
package main

import "fmt"

func main() {
    arr := [3]int{10, 20, 30}
    ptr := &arr[0] // Pointer to the first element

    for i := 0; i < len(arr); i++ {
        fmt.Println(*ptr) // Dereference pointer to access value
        ptr = &arr[i]     // Manually move to next element
    }
}
```


## Pointer to Arrays

You can create pointers to arrays in Go, which is useful in certain situations, such as when you need to manipulate the entire array in a function without copying it.

```go
arr := [3]int{10, 20, 30}
ptr := &arr
fmt.Println(ptr)  // Prints the address of the array
```

## Go's Garbage Collection and Pointers

Go has an automatic garbage collection (GC) system, which helps in managing memory. When a pointer no longer points to any object (i.e., no references exist to the allocated memory), the garbage collector will automatically free the memory.

However, Go’s garbage collector uses the concept of **reachability**. If a pointer is unreachable (i.e., no variables can reference it), it will be cleaned up.


## Best Practices for Using Pointers

1. **Use pointers to avoid copying large data structures**: When passing large structs, arrays, or slices to functions, use pointers to avoid expensive copies.
2. **Use pointers to modify values in functions**: When you need to modify the value of a variable inside a function, pass a pointer to that variable.
3. **Avoid unnecessary pointers**: If the data is small or primitive, avoid using pointers. Simple values (like `int` or `float64`) are better passed by value.
4. **Check for `nil` pointers**: Always check if a pointer is `nil` before dereferencing it to avoid runtime panics. This will happen if the pointer is created and not initialised `var ptr *int32`. However, on initialising `var ptr *int32 = new(int32)` then the `ptr` is pointing to an empty memory address and is not 'nil'. 

Pointers in Go are primarily used for **efficiency reasons**, but they also serve several other purposes in certain scenarios.