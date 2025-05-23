---
tags:
  - DSA
  - complexity_analysis
date: 2025-02-12T23:48:00
---
The Notation symbolizes the ***lower-bound*** of the running time of an algorithm or the algorithm's shortest time to complete its operation. Therefore, it gives the ***best-case*** complexity of an algorithm. 

We say that the running time is "big-$\Omega$ of \[ f(n) \]." We use big-$\Omega$ notation for **asymptotic lower bounds**, since it bounds the growth of the running time from below for large enough input sizes.

### Examples of big $\Omega$ Notation
- Insertion Sort: $\Omega$($n$), if the input is already sorted
- Binary Search: $\Omega$($1$), target is found in the first comparison 
### Why is Big $\Omega$ important?
- Helps understand the **best possible performance** an algorithm can achieve.
- Helps in **optimization** by setting realistic expectations.
