---
tags:
  - go
date: 2025-03-15T13:42:00
---

## Strings
A **string** in Go is a read-only slice of bytes. It is immutable, meaning that once a string is created, its contents cannot be changed.

### Declaring Strings
```go
str1 := "Hello, World!"
var str2 string = "Go Programming"
```

### String Properties
- Strings are sequences of bytes, not necessarily characters.
- They support indexing and slicing.
- They are UTF-8 encoded.
- Strings are immutable.

### String Length
The built-in `len()` function returns the number of bytes (not characters) in a string.
```go
fmt.Println(len("Hello, 世界")) // Output: 13 (not 9, since 世界 takes 3 bytes each)
```

### String Iteration
Using a **for loop** to iterate over a string:
```go
for i, ch := range "Hello, 世界" {
    fmt.Printf("Index: %d, Character: %c\n", i, ch)
}
```
---

## Runes in Go
A **rune** is an alias for `int32` and represents a single Unicode character. Since GO uses UTF-8 encoding, a single character may be more than one byte long.

### Declaring Runes
```go
var r rune = 'A' // Single quotes for runes
fmt.Println(r)    // Output: 65 (ASCII value of 'A')
```

### Working with Runes
To convert a string to a slice of runes:
```go
runes := []rune("Hello, 世界")
fmt.Println(len(runes)) // Output: 9 (correct character count)
```

### Iterating Over Runes
Using `range` ensures that Unicode characters are handled correctly:
```go
for _, r := range "Go 🏆" {
    fmt.Printf("%c ", r) // Output: G o   🏆
}
```

---

## Bytes in Go
A **byte** in Go is an alias for `uint8`. Since a string is a sequence of bytes, indexing a string returns a `byte`.

### Declaring Byte Slices
```go
b := []byte("Hello")
fmt.Println(b) // Output: [72 101 108 108 111] (ASCII values)
```

### Converting Between Strings and Byte Slices
```go
str := "GoLang"
bytes := []byte(str)
fmt.Println(bytes) // [71 111 76 97 110 103]
```

### Modifying Byte Slices
Unlike strings, byte slices are mutable:
```go
b := []byte("Hello")
b[0] = 'M'
fmt.Println(string(b)) // Output: Mello
```

---

## Comparing Strings, Runes, and Bytes
| Feature   | Strings          | Runes (int32)   | Bytes (uint8) |
|-----------|-----------------|-----------------|---------------|
| Type      | Immutable slice of bytes | Represents a Unicode character | Represents a single byte |
| Encoding  | UTF-8           | UTF-8 character | ASCII/UTF-8 byte |
| Mutability | Immutable       | Mutable when converted to slice | Mutable |
| Length    | `len(str)` returns byte count | `len([]rune(str))` returns character count | `len([]byte(str))` returns byte count |

---

## Summary
- **Strings** are immutable byte slices in UTF-8 format.
- **Runes** represent Unicode characters and are useful when working with multilingual text.
- **Bytes** represent single ASCII/UTF-8 encoded characters and allow modification via byte slices.
- Use **`[]rune(str)`** to handle characters correctly and **`[]byte(str)`** for efficient memory operations.

Understanding these concepts helps in writing efficient and bug-free text processing code in Go.

---

## References
- [Go Official Documentation](https://golang.org/doc/)
