---
tags:
  - DSA
  - go
date: 2025-08-21T22:16:00
---
**Bubble Sort** is an algorithm that sorts an array from the lowest value to the highest value. The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

**How it works:**
1. Go through the array, one value at a time.
2. For each value, compare the value with the next value.
3. If the value is higher than the next one, swap the values so that the highest value comes last.
4. Go through the array as many times as there are values in the array.
## Implementation
```go
// bubbleSort sorts an integer slice in ascending order using Bubble Sort.
// It repeatedly steps through the list, compares adjacent elements,
// and swaps them if they are in the wrong order.
func bubbleSort(arr []int) []int {
    // Outer loop: run n-1 passes through the array
    for i := 0; i < len(arr)-1; i++ {
        // Inner loop: compare adjacent elements up to the last unsorted element
        for j := 0; j < len(arr)-i-1; j++ {
            // If the current element is greater than the next, swap them
            if arr[j] > arr[j+1] {
                arr[j], arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
    // Return the sorted array
    return arr
}
```
### Improved version
```go
// improvedBubbleSort sorts an integer slice in ascending order using Bubble Sort,
// with an optimization: if no swaps occur during a pass, the algorithm stops early
// because the array is already sorted.
func improvedBubbleSort(arr []int) []int {
    // Outer loop: go through the slice up to n-1 passes
    for i := 0; i < len(arr)-1; i++ {
        swapped := false // Track whether any swap happened this pass

        // Inner loop: compare adjacent elements up to the last unsorted one
        for j := 0; j < len(arr)-i-1; j++ {
            if arr[j] > arr[j+1] {
                // Swap elements if they’re in the wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = true
            }
        }

        // If no swaps happened, array is already sorted → break early
        if !swapped {
            break
        }
    }

    return arr // Return the sorted slice
}
```
---
## Bubble Sort Time Complexity
The Bubble Sort algorithm loops through every value in the array, comparing it to the value next to it. So for an array of n values, there must be n such comparisons in one loop. And after one loop, the array is looped through again and again n times. This means there are $n⋅n$ comparisons done in total, so the time complexity for Bubble Sort is: $O(n^2)$

---
## **Advantages of Bubble Sort:**
- Bubble sort is easy to understand and implement.
- It does not require any additional memory space.
- It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.

## **Disadvantages of Bubble Sort:**
- Bubble sort has a time complexity of O(n2) which makes it very slow for large data sets.
- Bubble sort has almost no or limited real world applications. It is mostly used in academics to teach different ways of sorting.