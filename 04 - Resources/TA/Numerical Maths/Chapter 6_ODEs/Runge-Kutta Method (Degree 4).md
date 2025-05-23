The Fourth-Order Runge-Kutta Method (RK4) is a numerical technique used to approximate the solution of ordinary differential equations (ODEs) of the form:

$\frac{dy}{dx} = f(x, y)$

## Algorithm

Given an initial value problem:
$y'(x) = f(x, y), \quad y(x_0) = y_0$
we approximate the solution using the following iterative formula:

$y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$

where:
- $k_1 = f(x_n, y_n)$
- $k_2 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2} k_1)$
- $k_3 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2} k_2)$
- $k_4 = f(x_n + h, y_n + h k_3)$

This method provides better accuracy compared to Euler’s method, even with larger step sizes.

## Example 1: Simple Differential Equation

Consider the ODE:

$\frac{dy}{dx} = x + y$
with the initial condition $y(0) = 1$ and step size $h = 0.1$ to approximate $y(0.2)$.

### Steps:
1. Compute $k_1 = f(0,1) = 0 + 1 = 1$
2. Compute $k_2 = f(0.05, 1 + 0.05(1)) = f(0.05, 1.05) = 0.05 + 1.05 = 1.1$
3. Compute $k_3 = f(0.05, 1 + 0.05(1.1)) = f(0.05, 1.055) = 0.05 + 1.055 = 1.105$
4. Compute $k_4 = f(0.1, 1 + 0.1(1.105)) = f(0.1, 1.1105) = 0.1 + 1.1105 = 1.2105$
5. Compute $y_1 = 1 + \frac{0.1}{6} (1 + 2(1.1) + 2(1.105) + 1.2105) = 1.1103$
6. Repeat steps to compute $y_2$.

Thus, the approximation for $y(0.2)$ is **1.2321**.

## Example 2: Exponential Growth

Given:
$\frac{dy}{dx} = 2y, \quad y(0) = 1$
with step size $h = 0.2$ to approximate $y(0.4)$.

### Steps:
7. Compute $k_1 = 2(1) = 2$
8. Compute $k_2 = 2(1 + 0.1(2)) = 2(1.2) = 2.4$
9. Compute $k_3 = 2(1 + 0.1(2.4)) = 2(1.24) = 2.48$
10. Compute $k_4 = 2(1 + 0.2(2.48)) = 2(1.496) = 2.992$
11. Compute $y_1 = 1 + \frac{0.2}{6} (2 + 2(2.4) + 2(2.48) + 2.992) = 1.4913$
12. Repeat steps to compute $y_2$.

Thus, the approximation for $y(0.4)$ is **2.2184**.