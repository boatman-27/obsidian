---
tags:
  - DSA
  - go
date: 2025-08-22T16:55:00
---
The **Merge Sort** algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.

**How it works:**
1. Divide the unsorted array into two sub-arrays, half the size of the original.
2. Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
3. Merge two sub-arrays together by always putting the lowest value first.
4. Keep merging until there are no sub-arrays left.
## Implementation
```go
// split recursively divides the array into halves until slices of length 1 remain.
// Then it merges them back in sorted order.
func split(arr []int) []int {
    if len(arr) == 1 {
        return arr
    }

    midpoint := len(arr) / 2
    left := arr[:midpoint]
    right := arr[midpoint:]

    // Recursive split + merge
    return merge(split(left), split(right))
}

// merge combines two sorted slices into one sorted slice.
func merge(left, right []int) []int {
    var result []int

    // Compare elements from both sides until one is exhausted
    for len(left) > 0 && len(right) > 0 {
        if left[0] < right[0] {
            result = append(result, left[0])
            left = left[1:]
        } else {
            result = append(result, right[0])
            right = right[1:]
        }
    }

    // Append any leftovers
    for len(left) > 0 {
        result = append(result, left[0])
        left = left[1:]
    }
    for len(right) > 0 {
        result = append(result, right[0])
        right = right[1:]
    }

    return result
}
```
---
## Merge Sort Time Complexity
The time complexity for Merge Sort is $O(n⋅logn)$. And the time complexity is pretty much the same for different kinds of arrays. The algorithm needs to split the array and merge it back together whether it is already sorted or completely shuffled.

---
****Advantages****
- ****Stability**** : Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
- ****Guaranteed worst-case performance:**** Merge sort has a worst-case time complexity of ****O(N logN)**** , which means it performs well even on large datasets.
- ****Simple to implement:**** The divide-and-conquer approach is straightforward.
- ****Naturally Parallel**** : We independently merge subarrays that makes it suitable for parallel processing.

****Disadvantages****
- ****Space complexity:**** Merge sort requires additional memory to store the merged sub-arrays during the sorting process.
- ****Not in-place:**** Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.