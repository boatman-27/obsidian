- **Python:**

```python
# Define the array of elements to search in and the value to look for
arr = [12, 8, 9, 11, 5, 11]
valueToLookFor = 11

# Function to perform linear search
def linearSearch(arr, valueToLookFor):
    """
    Perform a linear search in the given array to find the index of the target value.
    Parameters:
    arr (list): The array in which to search for the value.
    valueToLookFor (int): The target value to search for in the array.
    Returns:
    int: The index of the first occurrence of the target value if found, otherwise -1.
    """
    # Iterate over the array using a loop
    for i in range(len(arr)):  
        # Check if the current element matches the value we are looking for
        if arr[i] == valueToLookFor:  
            # If a match is found, return the index of the current element
            return i  
    # If no match is found after the loop ends, return -1 to indicate failure
    return -1  
    
# Call the linearSearch function and print the result
print(linearSearch(arr, valueToLookFor))

```

- **JavaScript:**

```javascript
// Define an array to search within
const arr = [12, 8, 9, 11, 5, 11];

// Define the value we want to search for
const valueToLookFor = 11;

// Function to perform a linear search on the array
function linearSearch(arr, valueToLookFor) {
  // Iterate over the array using a for loop
  for (let i = 0; i < arr.length; i++) {
    // Check if the current element matches the value we are looking for
    if (valueToLookFor === arr[i]) {
      return i; // Return the index of the first match
    }
  }
  
  // If the value is not found after checking all elements, return -1
  return -1;
}

// Call the linearSearch function and log the result to the console
console.log(linearSearch(arr, valueToLookFor));  
```

- **C++:**

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Linear search function template to work with any data type
template <typename T>
int linearSearch(vector<T> arr, T key) {
    // Iterate through the vector
    for (int i = 0; i < arr.size(); i++) {
        // Check if the current element matches the key
        if (arr[i] == key) {
            return i;  // Return the index if a match is found
        }
    }
    // Return -1 if the key is not found
    return -1;
}

int main() {
    // Initialize a vector of integers
    vector<int> arr = {1, 2, 3, 4, 5};
    
    // Define the key to search for
    int key = 3;

    // Call the linearSearch function and store the result
    int index = linearSearch(arr, key);
  
    // Output the result
    cout << "Index of " << key << " is " << index << endl;
    
    return 0;  // Indicate successful execution
}
```