---
tags:
  - go
date: 2025-03-16T22:56:00
---
Generics allow you to define functions, methods, and types that can work with any data type while maintaining type safety. Instead of writing multiple functions for different types, you can define a single function or type that can handle multiple types, making your code more modular and easier to maintain.

Generics are defined using **type parameters** in Go. A type parameter is a placeholder for a type that you specify when the function or type is used.

Before generics, we would have to define the same function many times for all the different data types that can use that function.

```go
package main

import "fmt"

func sumIntSlice(slice []int) int {
	var sum int
	for _,v := range slice {
		sum += v
	}
	return sum
}

func sumFloatSlice(slice []float) float {
	var sum float
	for _,v := range slice {
		sum += v
	}
	return sum
}

func main() {
	var intSlice = []int{1, 2, 3}
	fmt.Println(sumIntSlice(sumInt))
	
	var floatSlice = []float{1.5, 2.2, 3.1}
	fmt.Println(sumFloatSlice(suFloat))
	
}
```

### Generic Function Syntax

Here’s the syntax for defining a generic function:

```go
func functionName[T TypeConstraint](param T) ReturnType {
    // function body
}
```

- `T` is a **type parameter** that can be replaced with any type.
- `TypeConstraint` defines restrictions on the types that can be passed to `T`.
- `param T` means the parameter accepts a type `T`.
- `ReturnType` is the type the function returns.

Now, with generics we only need to define the function once:

```go
func sumSlice[T int | float32 | float64](slice []T) {
	var sum T
	for _,v := range slice {
		sum += v
	}
	return sum
}
```

## Type Constraints

Type constraints define the kinds of types that can be passed to a type parameter. This is achieved using **interfaces**. The most common constraint is the `any` type, which means the parameter can be of any type.

### Common Type Constraints:

- `any`: Accepts any type (similar to `interface{}`).
- `comparable`: Allows only types that can be compared using comparison operators (e.g., `==`, `!=`).
- `string`, `int`, `float64`: You can also define type parameters with specific primitive types.

```go
package main

import "fmt"

// Generic function to find the maximum of two values
func Max[T comparable](a, b T) T {
    if a > b {
        return a
    }
    return b
}

func main() {
    fmt.Println(Max(1, 2))        // Output: 2
    fmt.Println(Max("apple", "banana")) // Output: banana
}
```

```go
func isEmpty[T any](slice []T) bool {
	return len(slice) == 0
}
```

## Generic Types

We can also define generic types, such as structs or interfaces, to hold values of various types.

```go
package main

import "fmt"

type gasEngine struct {
	gallons float32
	mpg float32
}

type electricalEngine struct {
	kwh float32
	mpkwh float32
}

type car[T gasEngine | electricalEngine] struct {
	carMake string
	carModel string
	engine T
}

func main() {
	var gasCar = car[gasEngine] {
		carMake : "Honda",
		carModel : "Civic",
		engin : gasEngine{
			gallons : 12.4
			mpg : 48
		}
	}


	var electricCar = car[electricalEngine] {
		carMake : "Tesla",
		carModel : "Model X",
		engin : electricalEngine{
			kwh : 57.5,
			mpkwh : 4.17
		}
	}
}
```

## Type Inference

Go can often automatically infer the type of a type parameter based on the arguments provided when calling a generic function or creating a generic type.

```go
func Print[T any](value T) {
    fmt.Println(value)
}

func main() {
    Print(42)        // T inferred as int
    Print("Hello")   // T inferred as string
}
```