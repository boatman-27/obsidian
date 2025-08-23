---
tags:
  - programming
  - go
date: 2025-03-14T14:33:00
yt vid: https://www.youtube.com/watch?v=8uiZC0l4Ajw
---
### Main points about GO
- Statically typed language: need to declare variable types explicitly
- Strongly typed language: the operation that can be performed on the variable depends on the data type
- GO is compiled, which translates your code into machine code, unlike Python which comes with an interpreter, making it slower than GO as the interpreter translates the code line by line as its compiled.
- Fast compile time. 
- Built in concurrency: no need for special packages or workarounds done by GoRoutines.
- simplicity. 
- Garbage collection: automatically frees up unused memory without having to do it manually. 

**Package**: A collection of .go files. 
**Module**: A collection of packages. 

when initialising a new GO project, we are initialising a module. Done by: `go mod init $(Path).  

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
}
```

Package [[FMT]] implements formatted I/O with functions analogous to C's printf and scanf. The format 'verbs' are derived from C's but are simpler.

## 📌 Variable and Constant Declaration

In Go, variables are declared using the `var` keyword, while constants are declared using `const`.

To learn more about the [[GO Data Types]]

#### **Variable Declaration:**

```
var age int = 25 // Explicit type declaration
name := "Adham" // Short-hand syntax (type inferred)
```

#### **Constant Declaration:**

```
const Pi float64 = 3.14159
```

Constants cannot be changed after declaration.

In order to use variables while printing, we can use 
`fmt.Printf("printing the variable $v", someVariable)`

`and` is `&&`, 'or' is '||'.

[[04 - Resources/Backend Roadmap/GO/Functions]] in Go are defined using the `func` keyword. They allow you to encapsulate a block of code that can be executed multiple times with different inputs. Functions in Go can return multiple values, have variadic parameters, and more.

[[Control Structures]] in Go allow programmers to dictate the flow of execution within a program. These include conditional statements, loops, and switch cases.

[[Array, Slices, Maps]]


Go provides robust support for working with text data using [[Strings, Runes, Bytes]]. Understanding how these types interact is essential for handling Unicode characters and text processing efficiently.

In Go, [[Structs and Interfaces]] are fundamental building blocks for organising and structuring data and behaviour. Structs define the data structure, while interfaces define the expected behaviour.

[[Pointers]] are important for working with memory directly, managing resources efficiently, and implementing certain data structures (like linked lists).

[[GoRoutines]] are lightweight threads managed by the Go runtime. They enable concurrent execution of functions, making Go highly efficient for parallel tasks.

[[Generics]] are a powerful feature that allows you to write more flexible and reusable code without sacrificing type safety.

[[Local Packages]]

In Go, data is sent and received across different systems, APIs, and functions. Understanding how to specify and use **types** or **structs** for data is essential for building robust and well-structured applications. Learn more in [[Sending and Receiving Data in Go]]

[[Defer]]

[[Go `flag` Package]]