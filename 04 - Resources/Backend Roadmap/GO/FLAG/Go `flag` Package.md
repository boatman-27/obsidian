---
date: 2025-06-23T16:55:00
tags:
  - go
---
The `flag` package in Go provides support for **command-line flags**.

---

## ✨ Basic Usage

```go
package main

import (
	"flag"
	"fmt"
)

func main() {
	// Define a flag
	name := flag.String("name", "world", "The name to greet")

	// Parse the command-line flags
	flag.Parse()

	// Use the flag
	fmt.Println("Hello,", *name)
}
```

#### 📌 Explanation

| Part                  | Description                                                                 |
| --------------------- | --------------------------------------------------------------------------- |
| `flag.String(...)`    | Defines a string flag. Returns a pointer to the value.                      |
| `-name`               | The flag name used in the terminal.                                         |
| `"world"`             | Default value if the flag is not provided.                                  |
| `"The name to greet"` | Help/usage text.                                                            |
| `flag.Parse()`        | Parses the command-line arguments. Must be called before using flag values. |
| `*name`               | Dereferences the pointer returned by `flag.String` to get the actual value. |

---
## 🧠 Other Flag Types

| Function                             | Description                                  |
| ------------------------------------ | -------------------------------------------- |
| `flag.Int(name, default, usage)`     | Integer flag                                 |
| `flag.Bool(name, default, usage)`    | Boolean flag                                 |
| `flag.Float64(name, default, usage)` | Float flag                                   |
| `flag.String(...)`                   | String flag                                  |
| `flag.Duration(...)`                 | Time duration flag (e.g., `"5s"`, `"1m30s"`) |

---
## 🔍 Example: Multiple Flags
```go
port := flag.Int("port", 8080, "Port number to listen on")
debug := flag.Bool("debug", false, "Enable debug mode")

flag.Parse()

fmt.Println("Port:", *port)
fmt.Println("Debug mode:", *debug)
```

Usage:
```go
go run main.go -port=3000 -debug=true
```

---

## 📜 Printing Help Text

The default help message is generated when using the `-h` or `--help` flag.

```go
go run main.go -h
```

Output:
```Bash
- name string
    	The name to greet (default "world")
```

---

## ⚙️ Advanced: Custom Flag Variables
```go
var age int
flag.IntVar(&age, "age", 18, "Your age")

```

This assigns the flag value directly to an existing variable.

---

