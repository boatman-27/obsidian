---
tags:
  - numerical
  - maths
date: 2025-02-07T16:45:00
Pqs: "[[Chapter_2_PQs.pdf]]"
Sols: "[[Chapter_2_Solutions.pdf]]"
---

Non-linear equations arise frequently in various fields of science, engineering, and mathematics. These equations cannot be expressed as a linear combination of their variables or unknowns, making their solutions more complex and requiring specialised numerical techniques.

The general form of a non-linear equation is:

$f(x) = 0$

where $f(x)$ is a non-linear function. Unlike linear equations, non-linear equations may have multiple solutions, no solutions, or even infinitely many solutions, depending on the nature of $f(x)$.
### Challenges in Solving Non-Linear Equations
1. **Existence and Uniqueness**: Not all non-linear equations have solutions, and when they do, the solution might not be unique.
2. **Sensitivity**: The solutions may be highly sensitive to initial guesses or parameter changes.
3. **Computational Complexity**: Analytical solutions are often unavailable, necessitating numerical approximation methods.

### Numerical Methods Overview
Numerical methods provide iterative approaches to approximate solutions of non-linear equations. These methods rely on specific properties of the function \( f(x) \) and its derivatives, where applicable. The choice of method often depends on:
- The nature of the equation.
- The required accuracy.
- The computational resources available.

In the following sections, we will explore three widely-used methods for solving non-linear equations:
1. **Bisection Method**: A simple, robust method based on interval halving. [[Bisection Method]]
2. **Newton's Method**: A fast, derivative-based approach. [[Newton's Method]]
3. **Secant Method**: An approximation to Newton's method that avoids explicit derivative computation. [[Secant Method]]

Each method has its advantages, limitations, and specific conditions for applicability.