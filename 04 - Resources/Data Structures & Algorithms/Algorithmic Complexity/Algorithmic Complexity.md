---
tags:
  - DSA
date: 2025-08-20T19:46:00
---
**Algorithmic Complexity** refers to the computing resources needed by an algorithm to solve a problem. These computing resources can be the time taken for program execution (*time complexity*), or the space used in memory during its execution (*space complexity*).

The aim is to minimize these resources, so an algorithm that takes less time and space is considered more efficient. Complexity is usually expressed using Big O notation, which describes the upper bound of time or space needs, and explains how they grow in relation to the input size. It's important to analyze and understand the algorithmic complexity to choose or design the most efficient algorithm for a specific use-case.

---
## What is time complexity?
Time complexity is a measure of how long an algorithm takes to run, based on the size of the input. It is expressed using Big-O notation, which provides a rough estimate of the running time. An algorithm with a lower time complexity will generally be faster than an algorithm with a higher time complexity.

---
## What is space complexity?
Space complexity is a measure of how much memory an algorithm requires, based on the size of the input. Like time complexity, it is expressed using Big-O notation. An algorithm with a lower space complexity will generally require less memory than an algorithm with a higher space complexity.

---
## Common Runtimes

![big o notation in data structure](https://dotnettrickscloud.blob.core.windows.net/article/data%20structures/2720231115130534.png "big o notation in data structure")

### 1. **$O(1)$ (Constant Time)**

- **Description**: This means the running time of the algorithm remains constant, regardless of the size of the input data set. Whether you're working with an array of 10 elements or 1 million, if an operation takes the same amount of time regardless of the size of the array, it is said to have a constant time complexity.
- **Example**: Accessing an element in an array by index is an example of $O(1)$ time complexity.

**Real-life Example**: Retrieving a value from a hash table given the key.

---
### 2. **$O(log_{2} n)$ (Logarithmic Time)**

- **Description**: An algorithm has logarithmic time complexity when the running time grows logarithmically in proportion to the input size. This typically happens when the algorithm halves the input size at each step (e.g., binary search).
- **Example**: A **binary search** algorithm has $O(log_{2}n)$ time complexity, as it repeatedly divides the search space in half.
- The math:
$$
\begin{aligned}
\text{Start with } & n. \\
\text{After 1 step: } & \frac{n}{2} \\
\text{After 2 steps: } & \frac{n}{4} \\
\text{After } k \text{ steps: } & \frac{n}{2^k} \\
\text{Stop when: } & \frac{n}{2^k} = 1 \\
\text{Solve for } k: & n = 2^k \implies k = \log_2(n)
\end{aligned}
$$

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

---
### 9. **$O(n^k)$ (Polynomial Time)**

- **Description**: Is a class of time complexity that represents the amount of time an algorithm takes to run as being proportional to the size of the input data raised to a constant power $k$. The value $n$ is a representation of the size of the input, while $k$ represents a constant. Algorithms running in polynomial time are considered to be reasonably efficient for small and medium-sized inputs, but can become impractical for large input sizes due to the rapid growth rate of function.
- **Example**: Selection sort will have **$O(n^2)$
---
There are mainly three asymptotic notations for the complexity analysis of algorithms: 
1. [[Big-O Notation]]
2. [[Omega Notation]]
3. [[Theta Notation]]