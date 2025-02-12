# Sorting Algorithms

## Quick Sort

Quick Sort is a divide-and-conquer sorting algorithm. It picks an element as a pivot and partitions the array around the pivot such that elements smaller than the pivot come before it and elements larger come after.

### How It Works:
1. Pick a pivot element.
2. Partition the array into two halves:
   - Elements smaller than the pivot.
   - Elements greater than or equal to the pivot.
3. Recursively apply the above steps to the subarrays.
### Time Complexity:
- **Best Case:** \( O(n \log n) \)
- **Worst Case:** \( O(n^2) \) (occurs when the pivot is the smallest or largest element)
- **Average Case:** \( O(n \log n) \)
### Space Complexity:
- \( O(\log n) \) for recursive stack.
### Applications:
- Suitable for large datasets.
- Common in libraries due to its average-case efficiency.
#### Code Examples [[Quick Sort]]

---
## Bubble Sort

Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
### How It Works:
1. Compare adjacent elements.
2. Swap them if necessary.
3. Repeat the process for all elements until the array is sorted.

### Time Complexity:
- **Best Case:** \( O(n) \) (when the array is already sorted)
- **Worst Case:** \( O(n^2) \)
- **Average Case:** \( O(n^2) \)
### Space Complexity:
- \( O(1) \)
### Applications:
- Used for small datasets.
- Useful for educational purposes.
#### Code Examples [[Bubble Sort]]

---
## Insertion Sort

Insertion Sort builds the final sorted array one element at a time by picking elements and placing them at their correct position.
### How It Works:
1. Start with the second element.
2. Compare it with elements before it.
3. Insert it in the correct position.
4. Repeat for all elements.
### Time Complexity:
- **Best Case:** \( O(n) \) (when the array is already sorted)
- **Worst Case:** \( O(n^2) \)
- **Average Case:** \( O(n^2) \)
### Space Complexity:
- \( O(1) \)
### Applications:
- Suitable for small or partially sorted datasets.
#### Code Examples [[Insertion Sort]]

---
## Merge Sort

Merge Sort is a divide-and-conquer sorting algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.

### How It Works:
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves.
  
### Time Complexity:
- **Best Case:** \( O(n \log n) \)
- **Worst Case:** \( O(n \log n) \)
- **Average Case:** \( O(n \log n) \)

### Space Complexity:
- \( O(n) \) for temporary arrays.
### Applications:
- Suitable for large datasets.
- Used in stable sorting scenarios.
#### Code Examples [[Merge Sort]]

---
## Selection Sort

Selection Sort repeatedly selects the smallest element from the unsorted part and swaps it with the first unsorted element.

### How It Works:
1. Find the smallest element in the unsorted part.
2. Swap it with the first unsorted element.
3. Repeat for all elements.
### Time Complexity:
- **Best Case:** \( O(n^2) \)
- **Worst Case:** \( O(n^2) \)
- **Average Case:** \( O(n^) \)
### Space Complexity:
- \( O(1) \)
### Applications:
- Simple to implement for small datasets.
- Used when memory is constrained.
#### Code Examples [[Selection Sort]]

---
# Searching Algorithms

## Linear Search
  
Linear Search checks every element in the array sequentially until the desired element is found or the array ends.

### How It Works:
1. Start from the first element.
2. Compare each element with the target.
3. Stop when the target is found or the array ends.
### Time Complexity:
- **Best Case:** \( O(1) \) (when the target is the first element)
- **Worst Case:** \( O(n) \)
- **Average Case:** \( O(n) \)
### Space Complexity:
- \( O(1) \)
### Applications:
- Suitable for small datasets.
- Useful for unsorted arrays.
#### Code Examples [[Linear Search]]

---
## Binary Search

Binary Search efficiently searches for a target in a sorted array by repeatedly dividing the search interval in half.
### How It Works:
1. Compare the target with the middle element.
2. Narrow the search to the left or right half based on the comparison.
3. Repeat until the target is found or the interval is empty.

### Time Complexity:
- **Best Case:** \( O(1) \) (when the target is the middle element)
- **Worst Case:** \( O(\log n) \)
- **Average Case:** \( O(\log n) \)

### Space Complexity:
- \( O(1) \) (iterative version)
- \( O(\log n) \) (recursive version)

### Applications:
- Suitable for large datasets that are sorted.
- Widely used in search algorithms and databases.
#### Code Examples [[Binary Search]]

---
