---
tags:
  - maths
  - numerical
date: 2025-02-14T11:43:00
Notes: "[[Chapter_6_Notes.pdf]]"
Pqs: "[[Chapter_6_PQs.pdf]]"
Sols: "[[Chapter_6_Solutions Q3,4.pdf]]"
---

Ordinary Differential Equations (ODEs) describe relationships involving a function and its derivatives. They appear in various fields, including physics, engineering, and economics. An ODE is typically written in the form:

$\frac{dy}{dx} = f(x, y)$

where $y$ is the unknown function of $x$, and $f(x, y)$ defines how $y$ changes with respect to $x$.

## Numerical Methods for Solving ODEs

Many ODEs cannot be solved analytically, so we rely on numerical methods to approximate solutions. Two common methods are Euler's Method and the Fourth-Order Runge-Kutta Method (RK4).

### Euler's Method

[[Euler's method]] is the simplest numerical approach to solving first-order ODEs. It approximates the solution by iterating with small steps: $h$:

$y_{n+1} = y_n + h f(x_n, y_n)$

where:
- $y_n$ is the current approximation,
- $h$ is the step size,
- $f(x_n, y_n)$ is the derivative at $(x_n, y_n)$,
- $y_{n+1}$ is the next approximation.

Euler's method is easy to implement but has limited accuracy, as it accumulates errors quickly.

### Fourth-Order Runge-Kutta Method (RK4)

The [[Runge-Kutta Method (Degree 4)]] RK4 improves accuracy by using intermediate steps to estimate the slope more precisely. The formula is:

$y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$

where:
- $k_1 = f(x_n, y_n)$,
- $k_2 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2} k_1)$,
- $k_3 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2} k_2)$,
- $k_4 = f(x_n + h, y_n + h k_3)$.

The RK4 method provides a much better approximation with a relatively small step size, making it a preferred choice in many applications.