---
tags:
  - DSA
  - complexity_analysis
date: 2025-02-12T14:42:00
---

**Complexity Analysis:** is defined as a technique to measure how long an algorithm would take to complete given an input of size $n$; independent of the machine, language in which the algorithm is written in and the compiler. It is used for evaluating the variations of execution time on different algorithms. 

While complexity is usually in terms of time, it is also analyzed in terms of space $i.e.$ algorithm's memory requirements(how much space it would need). 

### Why Complexity Analysis is Required?
- Gives an estimated time and space required to execute a program. 
- Used for comparing different algorithms for different input sizes.
- Helps to determine the difficulty of a problem. (refers to how time and space complexity can give an estimate of the *effort* required to solve a problem)

Your algorithm doesn't need to behave in the same way for different input sizes. its performance may vary. The study of the variations in the performance of the algorithm with the change in the order of the input size is **Asymptotic Analysis**. 

**Asymptotic notations** are mathematical notations to describe the running time of an algorithm when the input tends towards a particular value or a limiting value. In other words, it defines the mathematical limits of its run-time performance. Using the asymptotic analysis, we can easily conclude the average-case, best-case, and worst-case scenario of an algorithm.

There are mainly three asymptotic notations for the complexity analysis of algorithms: 
1. [[Big-O Notation]]
2. [[Omega Notation]]
3. [[Theta Notation]]

Common Asymptotic Notations

| **Type of Complexity** | **Asymptotic Notation** |
| ---------------------- | ----------------------- |
| constant               | ?(1)                    |
| linear                 | ?(n)                    |
| logarthmic             | ?($log(n)$)             |
| $n log n$              | ?($nlog(n)$)            |
| exponential            | ?($2^n$)                |
| cubic                  | ?($n^3$)                |
| polynomial             | ?($n^k$)                |
| quadratic              | ?($n^2$)                |


| **Algorithm**        | **Complexity**          |
| -------------------- | ----------------------- |
| Linear Search        | $O(n)$                  |
| Binary Search        | $O(log(n))$             |
| Bubble Sort          | $O(n^2)$                |
| Insertion Sort       | $O(n^2)$                |
| Selection Sort       | $O(n^2)$                |
| QuickSort            | $O(n^2)$                |
| Merge Sort           | $O(nlog(n))$            |
| Radix Sort           | $O((n +b) + \log{b}{k}$ |
| Breadth First Search | $O(V + E)$              |
| Depth First Search   | $O(V + E)$              |

**Worst-case time complexity of different data structures for different operations**

| **Data Structure** | **Access** | **Search** | **Insertion** | **Deletion** |
| ------------------ | ---------- | ---------- | ------------- | ------------ |
| Array              | $O(1)$     | $O(n)$     | $O(n)$        | $O(n)$       |
| Stack              | $O(n)$     | $O(n)$     | $O(1)$        | $O(1)$       |
| Queue              | $O(n)$     | $O(n)$     | $O(1)$        | $O(1)$       |
| Singly Linked List | $O(n)$     | $O(n)$     | $O(n)$        | $O(n)$       |
| Double Linked List | $O(n)$     | $O(n)$     | $O(1)$        | $O(1)$       |
| Hash Table         | $O(n)$     | $O(n)$     | $O(n)$        | $O(n)$       |
| Binary Search Tree | $O(n)$     | $O(n)$     | $O(n)$        | $O(n)$       |
| AVL Tree           | $O(log n)$ | $O(log n)$ | $O(log n)$    | $O(log n)$   |
| Binary Tree        | $O(n)$     | $O(n)$     | $O(n)$        | $O(n)$       |
| Red Black Tree     | $O(log n)$ | $O(log n)$ | $O(log n)$    | $O(log n)$   |
