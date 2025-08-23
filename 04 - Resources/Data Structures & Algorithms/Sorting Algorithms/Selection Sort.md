---
tags:
  - DSA
  - go
date: 2025-08-21T23:24:00
---
****Selection Sort**** is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the ****smallest (or largest)**** element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.

**How it works:**
1. Go through the array to find the lowest value.
2. Move the lowest value to the front of the unsorted part of the array.
3. Go through the array again as many times as there are values in the array.
## Implementation
```go
// selectionSort sorts an integer slice in ascending order using Selection Sort.
// It repeatedly selects the smallest element from the unsorted portion
// and swaps it with the first unsorted element.
func selectionSort(arr []int) []int {
    // Outer loop: iterate over the slice
    for i := 0; i < len(arr)-1; i++ {
        minIndex := i // assume the current index holds the minimum

        // Inner loop: find the actual minimum in the remaining unsorted part
        for j := i + 1; j < len(arr); j++ {
            if arr[j] < arr[minIndex] {
                minIndex = j
            }
        }

        // Swap the found minimum with the element at index i
        if minIndex != i {
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        }
    }

    return arr // Return the sorted slice
}
```
---
## Selection Sort Time Complexity
Selection Sort sorts an array of n values. On average, about $\dfrac{n}{2}$ elements are compared to find the lowest value in each loop. And Selection Sort must run the loop to find the lowest value approximately n times. We get time complexity: $O\left( \frac{n}{2}⋅n \right)=O(n^2)$
****Auxiliary Space:**** O(1) as the only extra memory used is for temporary variables.

---
## Advantages of Selection Sort
- Easy to understand and implement, making it ideal for teaching basic sorting concepts.
- Requires only a constant O(1) extra memory space.
- It requires less number of swaps (or memory writes) compared to many other standard algorithms. Only [cycle sort](https://www.geeksforgeeks.org/dsa/cycle-sort/) beats it in terms of memory writes. Therefore it can be simple algorithm choice when memory writes are costly.

## Disadvantages of the Selection Sort****
- Selection sort has a time complexity of $O(n^2)$ makes it slow.
- Does not maintain the relative order of equal elements which means it is not stable.

## Applications of Selection Sort
- Perfect for teaching fundamental sorting mechanisms and algorithm design.
- Suitable for small lists where the overhead of more complex algorithms isn't justified and memory writing is costly as it requires less memory writes compared to other standard sorting algorithm