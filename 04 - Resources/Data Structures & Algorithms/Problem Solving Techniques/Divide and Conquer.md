---
tags:
  - DSA
date: 2025-09-03T20:53:00
---
**Divide and conquer** is a powerful algorithm design technique that solves a problem by breaking it down into smaller and easier-to-manage sub-problems, until these become simple enough to be solved directly.

This approach is usually carried out recursively for most problems. Once all the sub-problems are solved, the solutions are combined to give a solution to the original problem. It is a common strategy that significantly reduces the complexity of the problem.

## Working of Divide and Conquer Algorithm

Divide and Conquer Algorithm can be divided into three steps: ****Divide****, ****Conquer**** and ****Merge****.

![Working-of-Divide-and-Conquer-Algorithm](https://media.geeksforgeeks.org/wp-content/uploads/20240501171531/Working-of-Divide-and-Conquer-Algorithm.webp)

The above diagram shows working with the example of [Merge Sort](https://www.geeksforgeeks.org/dsa/merge-sort/) which is used for sorting

### ***1. Divide:***
- Break down the original problem into smaller subproblems.
- Each subproblem should represent a part of the overall problem.
- The goal is to divide the problem until no further division is possible.
In Merge Sort, we divide the input array in two halves.
### ***2. Conquer:***
- Solve each of the smaller subproblems individually.
- If a subproblem is small enough (often referred to as the “base case”), we solve it directly without further recursion.
- The goal is to find solutions for these subproblems independently.
In Merge Sort, the conquer step is to sort the two halves individually.
### ***3. Merge***:
- Combine the sub-problems to get the final solution of the whole problem.
- Once the smaller subproblems are solved, we recursively combine their solutions to get the solution of larger problem.
- The goal is to formulate a solution for the original problem by merging the results from the subproblems.
In Merge Sort, the merge step is to merge two sorted halves to create one sorted array.

## ***Examples of Divide and Conquer Algorithm***
***1. [[Merge Sort]]:***
We can use Divide and Conquer Algorithm to sort the array in ascending or descending order by dividing the array into smaller subarrays, sorting the smaller subarrays and then merging the sorted arrays to sort the original array.
***2. [[Quick Sort]]:***
It is a sorting algorithm that picks a pivot element and rearranges the array elements so that all elements smaller than the picked pivot element move to the left side of the pivot, and all greater elements move to the right side. Finally, the algorithm recursively sorts the subarrays on the left and right of the pivot element.