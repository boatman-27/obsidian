- **Python:**

```python
# Input array to be sorted
arr = [2, 8, 5, 3, 9, 4, 1, 7]

# Function to recursively split the array into halves and merge them back
def split(arr):
    # Base case: If the array has only one element, it's already sorted
    if len(arr) == 1:
        return arr

    # Find the middle index to split the array
    mid = len(arr) // 2
    
    # Divide the array into left and right halves
    left = arr[:mid]
    right = arr[mid:]
    print("Left:", left, "Right:", right)
    
    # Recursively split and merge the left and right halves
    return merge(split(left), split(right))

# Function to merge two sorted arrays into a single sorted array
def merge(left, right):
    result = []  # Initialize an empty list to store the merged result
    print("Left in merge:", left, "Right in merge:", right)

    # Compare elements from both arrays and append the smaller one to 'result'
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:  # If the first element of 'left' is smaller
            result.append(left[0])  # Append it to 'result'
            left.pop(0)  # Remove the appended element from 'left'
        else:  # If the first element of 'right' is smaller or equal
            result.append(right[0])  # Append it to 'result'
            right.pop(0)  # Remove the appended element from 'right'

    # Append any remaining elements from 'left' to 'result'
    while len(left) > 0:
        result.append(left[0])
        left.pop(0)  # Use pop(0) to remove the first element
        
    # Append any remaining elements from 'right' to 'result'
    while len(right) > 0:
        result.append(right[0])
        right.pop(0)  # Use pop(0) to remove the first element

    # Return the merged sorted array
    return result

# Call the split function on the input array and print the sorted array
print(split(arr))
```

- **JavaScript:**
 
```javascript

// Input array to be sorted
const arr = [2, 8, 5, 3, 9, 4, 1, 7, 6];

/**
 * Recursive function to split the array into halves until each piece has one element
 * @param {Array} arr - Array to be split
 * @returns {Array} - Sorted array after merging
 */
function split(arr) {
  // Base case: if the array has only one element, it is already sorted
  if (arr.length === 1) {
    return arr;
  }

  // Find the midpoint of the array
  const mid = arr.length / 2;

  // Divide the array into two halves: left and right
  const left = arr.slice(0, mid); // First half
  const right = arr.splice(mid); // Second half
  console.log(left, right); // Log the split arrays for debugging

  // Recursively split and merge the arrays
  return merge(split(left), split(right));
}

/**
 * Merges two sorted arrays into one sorted array
 * @param {Array} left - Left sorted array
 * @param {Array} right - Right sorted array
 * @returns {Array} - Merged sorted array
 */
function merge(left, right) {
  const result = []; // Array to store the merged result
  
  // Compare elements from both arrays and pick the smallest
  while (left.length > 0 && right.length > 0) {
    if (left[0] < right[0]) {
      result.push(left[0]); // Add the smallest element from "left" to "result"
      left.splice(0, 1); // Remove the smallest element from "left"
    } else {
      result.push(right[0]); // Add the smallest element from "right" to "result"
      right.splice(0, 1); // Remove the smallest element from "right"
    }
  }

  // If there are remaining elements in the "left" array, add them to "result"
  while (left.length) {
    result.push(left[0]); // Add the first element from "left" to "result"
    left.splice(0, 1); // Remove the added element from "left"
  }
  
  // If there are remaining elements in the "right" array, add them to "result"
  while (right.length > 0) {
    result.push(right[0]); // Add the first element from "right" to "result"
    right.splice(0, 1); // Remove the added element from "right"
  }
  return result; // Return the merged sorted array
}

// Call the "split" function to sort the array and log the result
console.log(split(arr)); // Prints the sorted array
```

- **C++:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to recursively split and merge the array
vector<int> split(vector<int>& arr) {
    // Base case: if the array has only one element, it's already sorted
    if (arr.size() == 1) {
        return arr;
    }
    
    // Find the middle index to split the array
    size_t mid = arr.size() / 2;

    // Divide the array into left and right halves
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());

    // Recursively split and sort both halves
    left = split(left);
    right = split(right);

    // Merge the two sorted halves
    vector<int> result;
    size_t i = 0, j = 0;

    // Compare elements from left and right arrays and merge them in sorted order
    while (i < left.size() && j < right.size()) {
        if (left[i] <= right[j]) {
            result.push_back(left[i++]); // Add the smaller element from left
        } else {
            result.push_back(right[j++]); // Add the smaller element from right
        }
    }

    // Add any remaining elements from the left subarray
    while (i < left.size()) {
        result.push_back(left[i++]);
    }

    // Add any remaining elements from the right subarray
    while (j < right.size()) {
        result.push_back(right[j++]);
    }

    return result; // Return the merged and sorted array
}

int main() {
    // Input array to be sorted
    vector<int> arr = {2, 8, 5, 3, 9, 4, 1, 7};

    // Perform the merge sort by calling the split function
    vector<int> sortedArr = split(arr);

    // Print the sorted array
    cout << "Sorted array: ";
    for (int num : sortedArr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
```

  