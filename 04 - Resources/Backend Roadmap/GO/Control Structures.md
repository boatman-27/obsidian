---
tags:
  - go
date: 2025-03-14T18:17:00
---
## 📌 Conditional Statements

Go provides three main types of conditional statements:

### `if` Statement
The `if` statement allows for conditional execution of code.

#### Syntax:
```go
if condition {
    // Code to execute if condition is true
}
```

#### Example:
```go
package main
import "fmt"

func main() {
    x := 10
    if x > 5 {
        fmt.Println("x is greater than 5")
    }
}
```

### `if-else` Statement
The `if-else` statement executes one block of code if the condition is true, and another if it is false.

#### Syntax:
```go
if condition {
    // Code if condition is true
} else {
    // Code if condition is false
}
```

#### Example:
```go
package main
import "fmt"

func main() {
    x := 3
    if x > 5 {
        fmt.Println("x is greater than 5")
    } else {
        fmt.Println("x is less than or equal to 5")
    }
}
```

### `if-else if-else` Statement
Used to check multiple conditions sequentially.

#### Syntax:
```go
if condition1 {
    // Code for condition1
} else if condition2 {
    // Code for condition2
} else {
    // Code if neither condition1 nor condition2 are true
}
```

#### Example:
```go
package main
import "fmt"

func main() {
    x := 15
    if x < 10 {
        fmt.Println("x is less than 10")
    } else if x > 10 && x < 20 {
        fmt.Println("x is between 10 and 20")
    } else {
        fmt.Println("x is greater than or equal to 20")
    }
}
```

### Short Variable Declaration in `if`
A short variable declaration can be used inside the `if` condition.

#### Example:
```go
package main
import "fmt"

func main() {
    if x := 5; x > 3 {
        fmt.Println("x is greater than 3")
    }
}
```

---

## 📌 Loops
Go has only one looping construct: `for`.

### Basic `for` Loop
The standard loop iterates while a condition is true.

#### Syntax:
```go
for initialization; condition; post {
    // Loop body
}
```

#### Example:
```go
package main
import "fmt"

func main() {
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
}
```

### `for` as a While Loop
If only a condition is provided, the `for` loop behaves like a `while` loop.

#### Example:
```go
package main
import "fmt"

func main() {
    x := 0
    for x < 5 {
        fmt.Println(x)
        x++
    }
}
```

### Infinite Loop
A `for` loop without a condition runs indefinitely.

#### Example:
```go
package main
import "fmt"

func main() {
    for {
        fmt.Println("This is an infinite loop")
    }
}
```

### Looping Over Collections
Using `for` with `range` allows iteration over arrays, slices, maps, and strings.

#### Example:
```go
package main
import "fmt"

func main() {
    numbers := []int{1, 2, 3, 4, 5}
    for index, value := range numbers {
        fmt.Println("Index:", index, "Value:", value)
    }
}
```

---

## 📌 Switch Case
A `switch` statement is an alternative to multiple `if-else` statements.

### Basic Switch
#### Syntax:
```go
switch variable {
case value1:
    // Code for value1
case value2:
    // Code for value2
default:
    // Default case
}
```

#### Example:
```go
package main
import "fmt"

func main() {
    day := "Monday"
    switch day {
    case "Monday":
        fmt.Println("Start of the work week")
    case "Friday":
        fmt.Println("End of the work week")
    default:
        fmt.Println("A regular day")
    }
}
```

### Switch Without Expression
A `switch` without an expression acts like a series of `if-else` statements.

#### Example:
```go
package main
import "fmt"

func main() {
    x := 10
    switch {
    case x < 5:
        fmt.Println("x is less than 5")
    case x == 10:
        fmt.Println("x is exactly 10")
    default:
        fmt.Println("x is greater than 10")
    }
}
```

### Fallthrough
In Go, `fallthrough` forces execution of the next case.

In Go, the `fallthrough` statement is used within a `switch` case to force the execution of the next case, even if its condition does not match. By default, Go's `switch` does **not** automatically fall through to the next case (unlike C or JavaScript), but you can enable this behavior explicitly using `fallthrough`.

#### Example:
```go
package main
import "fmt"

func main() {
    x := 2
    switch x {
    case 1:
        fmt.Println("One")
    case 2:
        fmt.Println("Two")
        fallthrough
    case 3:
        fmt.Println("Three")
    default:
        fmt.Println("Other number")
    }
}
```