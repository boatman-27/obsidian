---
tags:
  - DSA
  - go
date: 2025-08-22T15:11:00
---
**Insertion sort** is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

**How it works:**
- We start with the second element of the array as the first element is assumed to be sorted.
- Compare the second element with the first element if the second element is smaller then swap them.
- Move to the third element, compare it with the first two elements, and put it in its correct position
- Repeat until the entire array is sorted.
## Implementation
```go
// insertionSort sorts an integer slice in ascending order using Insertion Sort.
// It builds the sorted part of the array one element at a time by inserting
// each new element into its correct position.
func insertionSort(arr []int) []int {
    // Outer loop: iterate through each element
    for i := 0; i < len(arr); i++ {
        temp := arr[i] // The current element to be placed
        j := i - 1     // Index of the last element in the sorted portion

        // Shift elements of the sorted portion to the right
        // until we find the correct place for temp
        for j >= 0 && arr[j] > temp {
            arr[j+1] = arr[j]
            j--
        }

        // Place temp at its correct position
        arr[j+1] = temp
    }

    // Return the sorted slice
    return arr
}
```
## Insertion Sort Time Complexity 
Insertion Sort sorts an array of $n$ values. On average, each value must be compared to about $\frac{n}{2}$ other values to find the correct place to insert it. Insertion Sort must run the loop to insert a value in its correct place approximately $n$ times. We get time complexity for Insertion Sort: $O(n^2)$
Best case: $O(n)$ (already sorted, only one comparison each time).

---
## Advantages
- Simple and easy to implement.
- ****Stable**** sorting algorithm.
- Efficient for small lists and nearly sorted lists.
- Space-efficient as it is an in-place algorithm.
## Disadvantages
- Inefficient for large lists.
- Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.
### Applications of Insertion Sort
- The list is small or nearly sorted.
- Simplicity and stability are important.