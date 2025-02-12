- **Python:**

```python
# Initial array to be sorted using Bubble Sort
arr = [2, 8, 5, 3, 9, 4, 1]

# Outer loop that goes through the entire array
# We start at i = 1 because the first pass is always comparing all pairs
for i in range(1, len(arr)):
    # Set swapped to False initially, meaning no swaps have been made yet in this pass
    swapped = False
    # Inner loop to perform the comparison and swapping of adjacent elements
    # We reduce the number of comparisons by 'i' because the last 'i' elements are already sorted

    for j in range(0, len(arr) - i):
        # If the current element is greater than the next one, swap them
        if arr[j] > arr[j + 1]:
        
            # Swap the elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # Mark that a swap occurred during this pass
            swapped = True
            
    # If no swaps occurred during the inner loop, the array is already sorted
    # In that case, we break out of the outer loop early to avoid unnecessary passes
    if not swapped:
        break
        
# Print the sorted array after completing the Bubble Sort
print(arr)
```

- **JavaScript:**

```javascript
// Initial array to be sorted using Bubble Sort
const arr = [2, 8, 5, 3, 9, 4, 1];
  
// Outer loop to iterate through the array, performing passes
for (let i = 1; i < arr.length; i++) {
  // Flag to track if any swaps were made in this pass
  let swapped = false;

  // Inner loop to compare adjacent elements in the array
  // As 'i' increases, the number of comparisons reduces because the largest elements bubble to the end

  for (let j = 0; j < arr.length - i; j++) {
    // If the current element is greater than the next, swap them
    if (arr[j] > arr[j + 1]) {
    
      // Swap the elements at position j and j+1
      [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
      // Set swapped to true since a swap was made
      swapped = true;
    }
  }
  
  // If no swaps were made during this pass, break out of the loop early
  // This indicates the array is already sorted
  if (!swapped) {
    break;
  }
}

// Print the sorted array after completing the Bubble Sort
console.log(arr);

```

- **C++:**

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {

    // Initial array to be sorted
    vector<int> arr = {2, 8, 5, 3, 9, 4, 1}; 
    
    // Outer loop to iterate through the array, performing passes

    for (size_t i = 0; i < arr.size() - 1; i++) {
        // Flag to track if any swaps were made in this pass
        bool swapped = false;
        
        // Inner loop to compare adjacent elements in the array
        // The number of comparisons decreases after each pass as the largest elements bubble to the end

        for (size_t j = 0; j < arr.size() - i - 1; j++) {
            // If the current element is greater than the next, swap them
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]); // Swap the elements at position j and j+1
                swapped = true; // Mark that a swap occurred
            }
        }
        
        // If no swaps were made during this pass, break out of the loop early
        // This indicates that the array is already sorted
        if (!swapped) {
            break;
        }
    }

    // Print the sorted array
    for (const int& num : arr) {
        cout << num << " ";
    }
    return 0;
}
```