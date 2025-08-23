---
date: 2025-06-24T22:10:00
tags:
  - go
---
## 🧠 What is `defer`?

In Go, `defer` schedules a function call to be run **after the current function completes**—regardless of how it exits (normal return, error, or panic).

```go
defer functionName()
```

---

## 📌 Common Use Cases

### 1. **Closing Files**

```go
file, err := os.Open("input.jpg")
if err != nil {
    log.Fatal(err)
}
defer file.Close()
```

✅ Ensures the file is closed even if an error occurs later.

---

### 2. **Unlocking a Mutex**

```go
mu.Lock()
defer mu.Unlock()
```

✅ Prevents deadlocks in case of early return or panic.

---

### 3. **Timing Execution**

```go
start := time.Now()
defer func() {
    fmt.Println("Elapsed:", time.Since(start))
}()
```

✅ Measures how long a function took to run.

---

## ⚙️ How It Works

- Deferred functions are **executed in LIFO order** (Last-In, First-Out).
- They're run **after** the surrounding function returns.

```go
func example() {
    defer fmt.Println("first")
    defer fmt.Println("second")
    fmt.Println("end")
}
```

**Output:**

```
end
second
first
```

---

## ✅ Best Practices

- Use `defer` immediately after acquiring a resource (e.g., opening a file, locking a mutex).
- Keep deferred functions short and simple.
- Be aware of argument evaluation timing.
---
