---
tags:
  - go
date: 2025-03-16T20:36:00
---
GoRoutines are way to launch multiple functions and have them execute concurrently. 

A ***GoRoutine*** is a lightweight, independently executing function in Go that runs concurrently with other GoRoutines. It is similar to a thread but managed by Go’s runtime, making it more efficient in terms of memory and scheduling.

Concurrency $\neq$ Parallel Execution. Concurrency means that i have multiple tasks running at the same, this can be done by jumping back and forth between tasks. So, for example task 1 can have a database call that takes 3 seconds, so as the CPU is waiting for the response it moves to task 2, when the response arrives from the database, the CPU jumps back to task 1. 

However, Parallel Execution, instead of having one CPU core working on both tasks we can have 2 cores each working on one task. So, this means a program can be running concurrently but not be running tasks in parallel.

This is our starting code:

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

var dbData = []string{"id1", "id2", "id3", "id4", "id5"}


func dbCall(i int) {
	var delay = rand.Float32() * 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	fmt.Printf("The result from the database is: ", dbData[i])
}

func main() {
	t0 = time.Now()
	for i := 0; i < len(dbData); i++ {
		dbCall(i)
	}
	fmt.Println("\n Total execution time: %v", time.Since(t0))
}
```

In order to start goRoutines, we use the `go` keyword infront of the function we want to run concurrently.  


```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

var dbData = []string{"id1", "id2", "id3", "id4", "id5"}


func dbCall(i int) {
	var delay = rand.Float32() * 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	fmt.Println("The result from the database is: ", dbData[i])
}

func main() {
	t0 := time.Now()
	for i := 0; i < len(dbData); i++ {
		go dbCall(i)
	}
	fmt.Println("\n Total execution time: %v", time.Since(t0))
}
```

The `go dbCall(i)` inside the `for` loop launches a new GoRoutine for each `dbCall(i)`. Since GoRoutines run independently and concurrently, the database calls are executed in parallel (assuming multiple CPU cores are available).

However, the main function does not wait for the GoRoutines to complete before printing the total execution time. The main function itself finishes execution almost immediately, without giving enough time for the GoRoutines to execute.

When `go dbCall(i)` is executed, it spawns a new GoRoutine that runs `dbCall(i)`. Inside `dbCall`, the `time.Sleep` function causes that GoRoutine to pause for a random delay, but this **only affects that specific GoRoutine**, not the entire program.

In order to fix that, we need to use `WaitGroup`. `WaitGroup` works like a counter and only executes whats after it, when the counter reaches 0. 

```go
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

  

var dbData = []string{"id1", "id2", "id3", "id4", "id5"}
var wg sync.WaitGroup
  
func dbCall(i int) {
	var delay = rand.Float32() * 2000
	time.Sleep(time.Duration(delay) * time.Millisecond)
	fmt.Println("The result from the database is: ", dbData[i])
	wg.Done()
}

  

func main() {
	t0 := time.Now()
	for i := 0; i < len(dbData); i++ {
		wg.Add(1)
		go dbCall(i)
	}
	wg.Wait()
	fmt.Printf("\n Total execution time: %v", time.Since(t0))

}
```

Now this works normally, because before we call `dbCall` we increment the `wg` by $1$, Inside `dbCall`, after sleeping for the delay period and printing the id, the counter is decremented and the process continues till the `for` loop ends. Now since all GoRoutines are complete, the printing statement is executed. 

