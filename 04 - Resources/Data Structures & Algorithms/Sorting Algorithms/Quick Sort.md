---
tags:
  - DSA
  - go
date: 2025-08-22T17:31:00
---
As the name suggests, **Quicksort** is one of the fastest sorting algorithms. The **Quicksort** algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

**How it works:**
1. Choose a value in the array to be the pivot element.
2. Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
4. Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.

## Implementation
```go
// quickSort sorts an integer slice in ascending order using Quick Sort.
// It uses the Lomuto partition scheme and recursively sorts the subarrays.
func quickSort(arr []int) []int {
    // Base case: 0 or 1 element is already sorted
    if len(arr) <= 1 {
        return arr
    }

    pivot := arr[len(arr)-1] // Choose the last element as pivot
    i := -1                  // Place for swapping elements <= pivot

    // Partition step
    for j := 0; j < len(arr)-1; j++ {
        if arr[j] <= pivot {
            i++
            arr[i], arr[j] = arr[j], arr[i]
        }
    }

    // Place pivot in its correct position
    arr[i+1], arr[len(arr)-1] = arr[len(arr)-1], arr[i+1]

    // Recursively sort left and right partitions
    leftSide := quickSort(arr[:i+1])
    rightSide := quickSort(arr[i+2:])

    // Build the final result slice
    var result []int
    result = append(result, leftSide...)
    result = append(result, pivot)
    result = append(result, rightSide...)

    return result
}
```
---
## Quicksort Time Complexity
The worst case scenario for Quicksort is $O(n^2)$. This is when the pivot element is either the highest or lowest value in every sub-array, which leads to a lot of recursive calls. With our implementation above, this happens when the array is already sorted. But on average, the time complexity for Quicksort is actually just $O(n.logn)$.

### Advantages of Quick Sort
- It is a divide-and-conquer algorithm that makes it easier to solve problems.
- It is efficient on large data sets.
- It has a low overhead, as it only requires a small amount of memory to function.
- It is Cache Friendly as we work on the same array to sort and do not copy data to any auxiliary array.
### Disadvantages of Quick Sort
- It has a worst-case time complexity of O(n2), which occurs when the pivot is chosen poorly.
- It is not a good choice for small data sets.
- It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we are swapping elements according to the pivot's position (without considering their original positions).
### Applications of Quick Sort
- Sorting large datasets efficiently in memory.
- Arranging records in databases for faster searching.
- Preprocessing step in algorithms requiring sorted input (e.g., binary search, two-pointer techniques).