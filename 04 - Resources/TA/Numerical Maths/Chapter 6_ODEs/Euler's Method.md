Euler's Method is a numerical technique for approximating the solution of a first-order ordinary differential equation (ODE) of the form:

$\frac{dy}{dx} = f(x, y)$

## Algorithm

Given an initial value problem:
$y'(x) = f(x, y), \quad y(x_0) = y_0$
we approximate the solution using the iterative formula:

$y_{n+1} = y_n + h f(x_n, y_n)$

where:
-  $y_n$ is the current approximation,
- $h$ is the step size,
- $f(x_n, y_n)$ is the derivative at $(x_n, y_n)$,
- $y_{n+1}$ is the next approximation.

## Example 1: Simple Differential Equation

Consider the ODE:

$\frac{dy}{dx} = x + y$
with the initial condition $y(0) = 1$, using step size $h = 0.1$ to approximate $y(0.3)$.

### Steps:
1. Compute $f(0,1) = 0 + 1 = 1$
2. Compute $y_1 = 1 + 0.1(1) = 1.1$
3. Compute $f(0.1,1.1) = 0.1 + 1.1 = 1.2$
4. Compute $y_2 = 1.1 + 0.1(1.2) = 1.22$
5. Compute $f(0.2,1.22) = 0.2 + 1.22 = 1.42$
6. Compute $y_3 = 1.22 + 0.1(1.42) = 1.362$

Thus, the approximation for $y(0.3)$ is **1.362**.

## Example 2: Exponential Growth

Given:
$\frac{dy}{dx} = 2y, \quad y(0) = 1$
with step size $h = 0.2$ to approximate $y(0.4)$.

### Steps:
1. Compute $f(0,1) = 2(1) = 2$
2. Compute $y_1 = 1 + 0.2(2) = 1.4$
3. Compute $f(0.2,1.4) = 2(1.4) = 2.8$ 
4. Compute $y_2 = 1.4 + 0.2(2.8) = 1.96$

Thus, the approximation for $y(0.4)$ is **1.96**.