---
tags:
  - go
date: 2025-03-14T15:35:00
---

Go has several built-in data types, categorized into numerical types, boolean, string, and complex types.

---
## 📌 Important Key points

- for numbers (ints, floats), you can do all arithmetic operation like addition, subtraction, multiplication and division `+, -, *, /, %`
- you can't do arithmetic operations between numbers of different types
```go
func main() {
	var num1 int = 8
	var num2 float32 = 32.5
	var sum int = num1 + num2 // wont work bc invalid operation: num1 + num2 (mismatched types int and float32)
}
```
- Integer division results in an Integer and is rounded down. To get the reminder use `%.  
- Strings can be initialized by double quotes or back tics , double quotes must be in the same line, but back ticks can be on multiple lines
- Variables can be initialized in a ***fancier*** way 
```go 
func main() {
	myInt := 34
	myString := "LMAO"		
}
```

## 📌 Integer Types (`int`, `uint`)

Integers can be signed (`int`) or unsigned (`uint`).

### **Signed Integers (`int` variants)**

|Type|Size|Range|
|---|---|---|
|`int8`|8-bit|-128 to 127|
|`int16`|16-bit|-32,768 to 32,767|
|`int32`|32-bit|-2,147,483,648 to 2,147,483,647|
|`int64`|64-bit|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|
|`int`|Platform-dependent (32-bit or 64-bit)||

### **Unsigned Integers (`uint` variants)**

|Type|Size|Range|
|---|---|---|
|`uint8`|8-bit|0 to 255|
|`uint16`|16-bit|0 to 65,535|
|`uint32`|32-bit|0 to 4,294,967,295|
|`uint64`|64-bit|0 to 18,446,744,073,709,551,615|
|`uint`|Platform-dependent (32-bit or 64-bit)||

### **Special Integer Types**

|Type|Description|
|---|---|
|`byte`|Alias for `uint8`|
|`rune`|Alias for `int32` (used for Unicode characters)|

#### **Example:**

```go
var a int16 = -1000
var b uint8 = 255
fmt.Println(a, b) // Output: -1000 255
```

---

## 📌 Floating-Point Types (`float`)

Used for decimal numbers.

|Type|Size|Precision|
|---|---|---|
|`float32`|32-bit|~6-7 decimal digits|
|`float64`|64-bit|~15 decimal digits|

#### **Example:**

```go
var pi float64 = 3.14159265359
fmt.Println(pi) // Output: 3.14159265359
```

---

## 📌 Complex Numbers (`complex`)

Used for complex numbers with real and imaginary parts.

|Type|Size|
|---|---|
|`complex64`|64-bit (uses `float32` for real & imaginary parts)|
|`complex128`|128-bit (uses `float64` for real & imaginary parts)|

#### **Example:**

```go
var c complex64 = 1 + 2i
fmt.Println(c) // Output: (1+2i)
```

---

## 📌 Boolean Type (`bool`)

Holds `true` or `false` values.

#### **Example:**

```go
var isGoFun bool = true
fmt.Println(isGoFun) // Output: true
```

---

## 📌 String Type (`string`)

A sequence of characters (UTF-8 encoded).

#### **Example:**

```go
var greeting string = "Hello, Go!"
fmt.Println(greeting) // Output: Hello, Go!
```

---

## 📌 Derived Types

|Type|Description|
|---|---|
|`array`|Fixed-size list of elements|
|`slice`|Dynamically-sized list of elements|
|`map`|Key-value pairs (like dictionaries)|
|`struct`|Custom data structure|
|`pointer`|Memory address reference|
|`interface{}`|Dynamic type for any value|

#### **Example:**

```go
var numbers = [3]int{1, 2, 3} // Array
var names = []string{"Alice", "Bob"} // Slice
var person = map[string]int{"age": 25} // Map
fmt.Println(numbers, names, person)
```

---

## 📌 Error 

The `error` type represents errors in Go. It is an interface that has a single `Error()` method returning a string.

```go
import (
	"errors"
	"fmt"
)

func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero is not allowed")
	}
	return a / b, nil
}

func main() {
	result, err := divide(10, 0)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Result:", result)
	}
}
```

## 🛠 Type Conversion

Go **does not support implicit type conversion**, so you must **explicitly convert** types when needed.

#### **Example:**

```go
var x int = 10
var y float64 = float64(x) // Explicit conversion
fmt.Println(y) // Output: 10.0
```

---

## 🔗 References

- [Official Go Data Types Docs](https://golang.org/ref/spec#Types)