---
tags:
  - go
date: 2025-03-14T15:38:00
---


The `fmt` package in Go provides formatted I/O functions, including printing to the console and scanning input from the user.

## 📌 Importing `fmt`

To use the `fmt` package, you need to import it:

```go
import "fmt"
```

---

## 🖨 Printing Functions

### `fmt.Print`

Prints output without a newline.

```go
fmt.Print("Hello ")
fmt.Print("World!")
// Output: Hello World!
```

### `fmt.Println`

Prints output with a newline.

```go
fmt.Println("Hello World!")
fmt.Println("Go is awesome!")
// Output:
// Hello World!
// Go is awesome!
```

### `fmt.Printf`

Prints formatted output using format specifiers.

```go
name := "Adham"
age := 25
fmt.Printf("My name is %s and I am %d years old.\n", name, age)
// Output: My name is Adham and I am 25 years old.
```

---

## 📌 Format Specifiers

|Specifier|Description|
|---|---|
|`%s`|String|
|`%d`|Integer|
|`%f`|Floating-point number|
|`%.2f`|Floating-point with 2 decimal places|
|`%t`|Boolean|
|`%v`|Default format for any value|
|`%T`|Type of the value|

Example:

```go
fmt.Printf("Value: %v, Type: %T\n", 42.5, 42.5)
// Output: Value: 42.5, Type: float64
```

---

## 📌 String Formatting Without Printing

### `fmt.Sprintf`

Returns a formatted string instead of printing it.

```go
message := fmt.Sprintf("Pi is %.2f", 3.14159)
fmt.Println(message) // Output: Pi is 3.14
```

---

## 📌 Scanning User Input

### `fmt.Scan`

Scans user input into variables.

```go
var name string
fmt.Print("Enter your name: ")
fmt.Scan(&name)
fmt.Println("Hello,", name)
```

### `fmt.Scanf`

Scans formatted input.

```go
var age int
fmt.Print("Enter your age: ")
fmt.Scanf("%d", &age)
fmt.Println("Your age is", age)
```

### `fmt.Scanln`

Scans input until a newline.

```go
var text string
fmt.Print("Enter something: ")
fmt.Scanln(&text)
fmt.Println("You entered:", text)
```

---

## 🛠 Common Use Cases

✅ Debugging with `fmt.Println` ✅ Logging with `fmt.Printf` ✅ Formatting strings with `fmt.Sprintf` ✅ Reading user input with `fmt.Scan`

---

## ⚠️ When **Not** to Use `fmt`

- For structured logging → Use `log` package (`log.Println`)
- For advanced text formatting → Use `text/template` or `html/template`

---

## 🔗 References

- [Official fmt Docs](https://pkg.go.dev/fmt)