---
tags:
  - DSA
  - complexity_analysis
date: 2025-02-12T15:19:00
---
The Notation symbolizes the ***upper-bound*** of the running time of an algorithm or the algorithm's longest time to complete its operation. Therefore, it gives the ***worst-case*** complexity of an algorithm. 



![big o notation in data structure](https://dotnettrickscloud.blob.core.windows.net/article/data%20structures/2720231115130534.png "big o notation in data structure")


### 1. **$O(1)$ (Constant Time)**

- **Description**: An algorithm is said to have constant time complexity if the running time does not depend on the size of the input. The time it takes to execute the algorithm remains the same, no matter how large the input is.
- **Example**: Accessing an element in an array by index is an example of $O(1)$ time complexity.

**Real-life Example**: Retrieving a value from a hash table given the key.

---

### 2. **$O(log n)$ (Logarithmic Time)**

- **Description**: An algorithm has logarithmic time complexity when the running time grows logarithmically in proportion to the input size. This typically happens when the algorithm halves the input size at each step (e.g., binary search).
- **Example**: A **binary search** algorithm has $O(logn)$ time complexity, as it repeatedly divides the search space in half.

**Real-life Example**: Searching for a value in a sorted list using binary search.

---

### 3. **$O(n)$ (Linear Time)**

- **Description**: Linear time complexity occurs when the running time of an algorithm grows directly in proportion to the size of the input. If the input size doubles, the execution time also doubles.
- **Example**: A **for loop** that iterates through an array once has $O(n)$ time complexity.

**Real-life Example**: Looping through an array to find the maximum or minimum element.

---

### 4. **$O(n log n)$ (Log-Linear Time)**

- **Description**: This time complexity is often found in efficient sorting algorithms like **Merge Sort** and **Quick Sort**. It combines the linear and logarithmic complexities, meaning the algorithm performs a logarithmic operation NNN times.
- **Example**: The **Merge Sort** and **Quick Sort** algorithms have $O(nlogn)$ time complexity.

**Real-life Example**: Sorting an array using Merge Sort or Quick Sort.

---

### 5. **$O(n^2)$ (Quadratic Time)**

- **Description**: Quadratic time complexity occurs when the running time is proportional to the square of the input size. This is common in algorithms with **nested loops** that perform operations on pairs of elements.
- **Example**: A **Bubble Sort** algorithm has $O(n^2)$ time complexity because it compares each element with every other element in the list.

**Real-life Example**: Sorting an array using Bubble Sort or Selection Sort.

---

### 6. **$O(n^3)$ (Cubic Time)**

- **Description**: Cubic time complexity happens when the algorithm has three nested loops or operations that each iterate over the input. The running time grows as the cube of the input size.
- **Example**: Certain matrix multiplication algorithms have $O(n^3)$ complexity, where each row and column are multiplied in a 3-dimensional space.

**Real-life Example**: An algorithm that checks all possible combinations of three different items from a list.

---

### 7. **$O(2^n)$ (Exponential Time)**

- **Description**: Exponential time complexity grows very rapidly as the input size increases. For each additional element, the running time doubles. This is common in brute-force solutions for problems like the **Traveling Salesman Problem** and other combinatorial problems.
- **Example**: A **recursive solution** to the Fibonacci sequence, where each call generates two new calls, has $O(2^n)$ time complexity.

**Real-life Example**: Solving the **Traveling Salesman Problem** using brute force (checking all possible routes).

---

### 8. **$O(n!)$ (Factorial Time)**

- **Description**: Factorial time complexity occurs in algorithms that generate all possible permutations of an input. As the input grows, the running time increases factorially, making it very inefficient for larger inputs.
- **Example**: An algorithm that generates all permutations of a list of NNN elements will have $O(n!)$ time complexity.

**Real-life Example**: Solving the **Traveling Salesman Problem** using brute force (checking every possible arrangement of cities).