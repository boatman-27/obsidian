- **Python:**

```python
# Input array to be sorted
arr = [8, 2, 4, 7, 1, 3, 9, 6, 5]
def quickSort(arr):
    if len(arr) <= 1:  # Base case
        return arr  # Return the array if it has 1 or 0 elements
    pivot = arr[-1]  # Choose the last element as the pivot

    i = -1  # Initialize the partition index

    for j in range(len(arr) - 1):  # Iterate through all elements except the pivot

        if arr[j] <= pivot:  # If the element is smaller than or equal to the pivot

            i += 1  # Move the partition index

            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements

  

    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]  # Place the pivot in its correct position

    left = quickSort(arr[:i + 1])  # Recursively sort the left partition

    right = quickSort(arr[i + 2:])  # Recursively sort the right partition

  

    return left + [arr[i + 1]] + right  # Combine the sorted partitions

  

print(quickSort(arr))

```

- **JavaScript:**

```javascript
// Input array to be sorted
const arr = [8, 2, 4, 7, 1, 3, 9, 6, 5];

function quickSort(arr) {
  // Base case: if the array has 1 or no elements, it's already sorted
  if (arr.length <= 1) return arr;

  // Initialize pointers
  let i = -1; // Index of the smaller element boundary
  let j = 0; // Current index being checked
  let pivot = arr[arr.length - 1]; // Choose the last element as the pivot

  // Partition the array around the pivot
  while (arr[j] != pivot) {
    if (arr[j] <= pivot) {
    
      // Increment the boundary for smaller elements
      i += 1;
      
      // Swap the current element with the boundary element
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    j += 1; // Move to the next element
  }
  
  // Place the pivot in its correct position
  [arr[i + 1], arr[arr.length - 1]] = [arr[arr.length - 1], arr[i + 1]];

  // Recursively sort the left and right partitions
  const left = quickSort(arr.slice(0, i + 1)); // Elements smaller than pivot
  const right = quickSort(arr.slice(i + 2, arr.length)); // Elements larger than pivot

  // Combine the sorted left partition, pivot, and right partition
  return [...left, arr[i + 1], ...right];
}

// Print the sorted array
console.log(quickSort(arr));
```

- **C++:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

// QuickSort function to sort the array
vector<int> quickSort(vector<int> arr) {
    // Base case: if the array has 1 or no elements, it's already sorted
    if (arr.size() <= 1) {
        return arr;
    }

    // Choose the last element as the pivot
    int pivot = arr[arr.size() - 1];

    // Index for the smaller element
    int i = -1;
    
    // Partition the array based on the pivot
    for (size_t j = 0; j < arr.size() - 1; j++) {
    
        // If the current element is less than or equal to the pivot
        if (arr[j] <= pivot) {
            i++; // Move the boundary of the smaller elements
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
  
    // Place the pivot in its correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[arr.size() - 1];
    arr[arr.size() - 1] = temp;

    // Recursively apply QuickSort to the left and right partitions
    vector<int> left = quickSort(vector<int>(arr.begin(), arr.begin() + i + 1)); // Left subarray
    vector<int> right = quickSort(vector<int>(arr.begin() + i + 2, arr.end())); // Right subarray

  
    // Combine the sorted left, pivot, and right arrays
    left.push_back(pivot); // Add pivot to the end of the left array
    left.insert(left.end(), right.begin(), right.end()); // Append the right array to the left

    return left; // Return the sorted array
}

int main() {
    // Input array
    vector<int> arr = {10, 7, 8, 9, 1, 5};
    
    // Call the QuickSort function
    vector<int> sortedArr = quickSort(arr);

    // Print the sorted array
    for (int num : sortedArr) {
        cout << num << " ";
    }
}
```
