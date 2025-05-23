In Go, **structs** and **interfaces** are fundamental building blocks for organizing and structuring data and behavior. Structs define the data structure, while interfaces define the expected behavior.

---

## Structs
A **struct** is a collection of named fields, useful for grouping related data.

### Declaring a Struct
```go
type Person struct {
    Name string
    Age  int
}
```

### Initializing a Struct
```go
p1 := Person{"Alice", 25} // Positional order
p2 := Person{Name: "Bob", Age: 30} // Named fields
p3 := new(Person) // Returns a pointer
p3.Name = "Charlie"
```

### Accessing Struct Fields
```go
fmt.Println(p1.Name) // Output: Alice
fmt.Println(p2.Age)  // Output: 30
```

### Struct Methods
Methods can be associated with structs.
```go
type Rectangle struct {
    Width, Height float64
}

// Method with value receiver
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}

// Method with pointer receiver (modifies the struct)
func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

rect := Rectangle{4, 5}
fmt.Println(rect.Area()) // Output: 20
rect.Scale(2)
fmt.Println(rect.Width) // Output: 8
```

---

## Interfaces
An **interface** defines a set of method signatures. Any type implementing these methods is implicitly part of the interface.

### Declaring an Interface
```go
type Shape interface {
    Area() float64
}
```

### Implementing an Interface
A type satisfies an interface if it implements all its methods.
```go
type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return 3.14 * c.Radius * c.Radius
}
```

### Using Interfaces
```go
func PrintArea(s Shape) {
    fmt.Println("Area:", s.Area())
}

c := Circle{5}
PrintArea(c) // Output: Area: 78.5
```

### Empty Interface
An `interface{}` (empty interface) can hold any type.
```go
var x interface{} = "Hello"
x = 42
```

### Type Assertion
```go
value, ok := x.(int)
if ok {
    fmt.Println("x is an int with value", value)
}
```

### Type Switch
```go
switch v := x.(type) {
case string:
    fmt.Println("String:", v)
case int:
    fmt.Println("Integer:", v)
default:
    fmt.Println("Unknown type")
}
```

---

## Structs vs. Interfaces
| Feature   | Structs          | Interfaces          |
|-----------|-----------------|---------------------|
| Purpose   | Data storage     | Behavior definition |
| Fields    | Yes             | No                 |
| Methods   | Can have methods | Defines method signatures |
| Inheritance | No | Implicit via method implementation |

---

## Summary
- **Structs** group related fields and can have methods.
- **Interfaces** define behavior; types implement interfaces implicitly.
- **Methods** can have value or pointer receivers.
- **Empty interfaces** allow handling values of any type.
- **Type assertion and type switches** are used for runtime type checking.

Understanding structs and interfaces allows for more effective Go programming, especially in designing scalable and maintainable applications.

---
