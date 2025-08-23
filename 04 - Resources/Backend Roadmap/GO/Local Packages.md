## Same Directory

- Ensure that all files belong to the same package.
- Run multiple files together using:
```sh
go run .
```
### Example:

```go
// main.go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, world!", name)
}
```

```go
// another.go
package main

var name = "another"
```

## Different Directories

- The file in the other directory should have a different package name.
- Import using the module name followed by the directory name.
- Variables or functions that need to be accessed externally should have their first letter capitalized.

### Example:

#### Directory Structure:

```
/events
  |-- /articles
  |     |-- article.go
  |-- main.go
```

#### Code Implementation:

```go
// main.go
package main

import (
	"fmt"
	article "new.com/events/articles"
)

func main() {
	fmt.Println("Hello, world!", article.Ar)
}
```

```go
// article.go
package article

var Ar = "LOL"
```

### Additional Notes

Using Functions Instead of Variables:
- If you prefer to use functions instead of variables:
```go
package article   

func GetMessage() string {
    return "LOL"
}
```
Then, in `main.go`:
```go
fmt.Println("Hello, world!", article.GetMessage())
```