---
tags:
  - go
date: 2025-03-14T17:25:00
---

A basic function in Go is defined as follows:

```go
func functionName(parameter1 type1, parameter2 type2) returnType {
    // function body
}
```

## 📌 Important Key points

- parameter type is enforced, so we can't define a function that takes a `string` then pass an `int.  
## 📌 Function parameters

Parameters are specified within the parentheses. You can define multiple parameters, separated by commas, and each parameter has a type.

```go
func greet(name string, age int) string {
    return "Hello, " + name + " who is " + fmt.Sprint(age) + " years old."
}
```

## 📌 Return Values

A function can return a single value, or multiple values, depending on the function's definition.

```go
func multiply(a int, b int) int {
    return a * b
}
```

```go
func divide(a int, b int) (int, int) {
    quotient := a / b
    remainder := a % b
    return quotient, remainder
}
```

## 📌 Multiple Return Values

Go allows functions to return multiple values, which can be useful in many cases, such as when performing calculations that return both a result and an error.

```go
func getValues() (int, string) {
    return 1, "Hello"
}
```

We can use the multiple return values as follows:

```go
func main() {
	x, y := getValues()
	fmt.Println(x)  // 1
	fmt.Println(y)  // Hello
}
```

## 📌 Variadic Functions

Go supports variadic functions, which can accept a variable number of arguments of the same type. You can define a variadic function by using an ellipsis (`...`) before the parameter type.

```go
func sum(numbers ...int) int {
    total := 0
    for _, num := range numbers {
        total += num
    }
    return total
}
```

we can call this function with any number of `int` arguments

```go
result := sum(1, 2, 3, 4)
fmt.Println(result)  // 10
```

## 📌 Anonymous Functions

Anonymous functions are functions that do not have a name. They are useful for passing functions as arguments or for defining simple functions in place.

```go
func main() {
    greeting := func(name string) {
        fmt.Println("Hello, " + name)
    }

    greeting("Alice")
}
```

