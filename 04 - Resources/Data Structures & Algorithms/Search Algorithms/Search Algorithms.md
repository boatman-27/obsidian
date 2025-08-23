---
tags:
  - DSA
date: 2025-08-20T23:35:00
---
***Searching algorithms*** are essential tools in computer science used to locate specific items within a collection of data. In this tutorial, we are mainly going to focus upon searching in an array. When we search an item in an array, there are two most common algorithms used based on the type of input array.

The two classic methods for array searching are **linear search** and **binary search**.
- **[[04 - Resources/Data Structures & Algorithms/Search Algorithms/Linear Search|Linear Search]]** is the brute-force method: you start at the first element, check if it’s the target, then move to the next, and keep going until you either find the item or collapse from exhaustion at the end of the array. It works on any type of array—sorted or unsorted—but it’s slow if the array is huge.
- **[[04 - Resources/Data Structures & Algorithms/Search Algorithms/Binary Search|Binary Search]]** is the smarter cousin, but it only works if the array is already sorted. Instead of checking every element, it keeps halving the search space. You look at the middle element: if it’s the target, done; if the target is smaller, search the left half; if larger, search the right half. This “divide and conquer” strategy is lightning-fast compared to linear search.