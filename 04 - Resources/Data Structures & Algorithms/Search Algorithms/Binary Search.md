---
tags:
  - DSA
  - go
date: 2025-08-20T23:58:00
---
Binary Search is a type of search algorithm that follows the divide and conquer strategy. It works on a sorted array by repeatedly dividing the search interval in half. Initially, the search space is the entire array and the target is compared with the middle element of the array.

If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target, and repeating this until the target is found. If the search ends with the remaining half being empty, the target is not in the array. Binary Search is log(n) as it cuts down the search space by half each step.

## Implementation
```go
func binarySearch(val int, arr []int) int {
	// Initialize the lower and upper bounds for the search
	left := 0
	right := len(arr) - 1

	for left <= right {
		// Safe mid calculation
		mid := left + (right-left)/2
		// Check if the midpoint element matches the target value
		if arr[mid] == val {
			return mid // found it, return index
		}
		// If the midpoint element is less than the target, search the right half
		if arr[mid] < val {
			left = mid + 1 // search right half
		// If the midpoint element is greater than the target, search the left half
		} else {
			right = mid - 1 // search left half
		}
	}
	// not found
	return -1
}
```