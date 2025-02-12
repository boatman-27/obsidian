- **Python:**

```python
# Initial array to be sorted using Selection Sort
arr = [2, 8, 5, 3, 9, 4, 1]

# Outer loop: iterates through the entire array except the last element
# Since the last element will already be sorted when we finish the second last iteration
for i in range(0, len(arr) - 1):
    # Assume the smallest element is at the current index `i` i.e. first element of the unsorted portion
    minIndex = i

    # Inner loop: find the index of the smallest element in the unsorted portion of the array
    for j in range(i + 1, len(arr)):
        # Compare current element `arr[j]` with the smallest known element `arr[minIndex]`
        if arr[j] < arr[minIndex]:
            # Update `minIndex` to the index of the new smallest element
            minIndex = j
            
    # After inner loop, `minIndex` holds the index of the smallest element in the unsorted portion
    # If the smallest element is not already at the current position `i`, swap them
    if minIndex != i:
        # Swap the elements at indices `i` and `minIndex`
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
# Print the sorted array
print(arr)
```

- **JavaScript:**

```javascript
// Initial array to be sorted
let arr = [2, 8, 5, 3, 9, 4, 1];

// Outer loop: iterate through the entire array except the last element
for (let i = 0; i < arr.length - 1; i++) {
  let minIndex = i; // Assume the smallest element is at the current index
  // Inner loop: find the index of the smallest element in the unsorted portion
  for (let j = i + 1; j < arr.length; j++) {
    if (arr[j] < arr[minIndex]) {
      minIndex = j; // Update minIndex if a smaller element is found
    }
  }

  // Swap the smallest element with the current element if needed
  if (minIndex !== i) {
    [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]]; // ES6 destructuring for swapping
  }
}

// Print the sorted array
console.log(arr);
```

- **C++:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr = {2, 8, 5, 3, 9, 4, 1}; // Initial array to be sorted

    // Outer loop: iterate through the entire array except the last element
    for (size_t i = 0; i < arr.size() - 1; i++) {
        size_t minIndex = i; // Assume the smallest element is at the current index
        // Inner loop: find the index of the smallest element in the unsorted portion
        for (size_t j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j; // Update minIndex if a smaller element is found
            }
        }
        
        // Swap the smallest element with the current element if needed
        if (minIndex != i) {
            swap(arr[i], arr[minIndex]);
        }
    }
    
    // Print the sorted array
    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
```
