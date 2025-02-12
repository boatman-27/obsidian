## Introduction
Cubic spline interpolation is a method used to approximate a function by connecting given data points with piecewise cubic polynomials. It ensures continuity in both function values, first derivatives, and second derivatives, making it a smoother and more accurate interpolation technique than quadratic splines.

## Definition
Given a set of data points:
$$
(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)
$$
where $x_0 < x_1 < ... < x_n$, the cubic spline consists of piecewise cubic functions $S_i(x)$ defined in each interval $[x_i, x_{i+1}]$.

## Construction
For each interval $[x_i, x_{i+1}]$, the cubic spline $S_i(x)$ is defined as:
$$
f(x) = \frac{(x_{i+1} - x)^3}{6h} M_i + \frac{(x - x_i)^3}{6h} M_{i+1} + \frac{x_{i+1} - x}{h} \left(y_i - \frac{h^2}{6} M_i \right) + \frac{x - x_i}{h} \left(y_{i+1} - \frac{h^2}{6} M_{i+1} \right)
$$
where $4h = x_{i+1} - x_i$, and $M_i$ are the second derivatives at each $x_i$ to be determined.

The coefficients $M_i$ are computed using the following system of equations:
$$
M_{i-1} + 4M_i + M_{i+1} = \frac{6}{h^2} (y_{i-1} - 2y_i + y_{i+1}), \quad i = 1 \text{ to } n-1
$$
with natural boundary conditions:
$$
M_0 = 0, \quad M_n = 0
$$

## Properties
- **Continuity:** The cubic spline is continuous across the domain.
- **Smoothness:** The first and second derivatives are continuous at internal points.
- **More Accurate than Quadratic Spline:** Provides a better approximation than both linear and quadratic interpolation.
## Algorithm
1. Given the data points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, sort them if necessary.
2. Construct the system of equations for $M_i$ and solve for $M_1, ..., M_{n-1}$.
3. Compute the piecewise cubic spline functions using the interpolation formula.
## Example
Given the data points:
$$
(1, 2), (3, 4), (5, 7)
$$

We have boundary conditions:
$$
M_0 = 0, \quad M_2 = 0
$$

Solving for $M_1$:

At $i = 1$,
$$
M_{0} + 4M_1 + M_{2} = \frac{6}{2^2} (y_{0} - 2y_1 + y_{2})
$$
$$
0 + 4M_1 + 0 = \frac{6}{4}(2 - 2(4) + 7)
$$
$$
4M_1 = \frac{3}{2} \Rightarrow M_1 = \frac{3}{8}
$$

### Finding the spline equations:
Using the cubic spline formula:
$$
f(x) = \frac{(x_{i+1} - x)^3}{6h} M_i + \frac{(x - x_i)^3}{6h} M_{i+1} + \frac{x_{i+1} - x}{h} \left(y_i - \frac{h^2}{6} M_i \right) + \frac{x - x_i}{h} \left(y_{i+1} - \frac{h^2}{6} M_{i+1} \right)
$$

For $i = 0$ (interval $[1,3]$):
$$
f_0(x) = \frac{(3 - x)^3}{12} (0) + \frac{(x - 1)^3}{12} \left(\frac{3}{8}\right) + \frac{3 - x}{2} \left(2 - \frac{4}{6} (0) \right) + \frac{x - 1}{2} \left(4 - \frac{4}{6} \left(\frac{3}{8}\right) \right)
$$
$$
f_0(x) = \frac{(x - 1)^3}{32} + \frac{3-x}{2} (2) + \frac{x - 1}{2} \left(4 - \frac{1}{4} \right)
$$
$$
f_0(x) = \frac{(x - 1)^3}{32} + (3-x) + (x - 1) \left(2 - \frac{1}{8}\right)
$$
$$
f_0(x) = \frac{(x - 1)^3}{32} + 3 - x + (x - 1) \cdot \frac{15}{8}
$$
$$
f_0(x) = \frac{(x - 1)^3}{32} + 3 - x + \frac{15(x-1)}{8}
$$

For $i = 1$ (interval $[3,5]$):
$$
f_1(x) = \frac{(5 - x)^3}{12} \left(\frac{3}{8}\right) + \frac{(x - 3)^3}{12} (0) + \frac{5 - x}{2} \left(4 - \frac{4}{6} \left(\frac{3}{8}\right) \right) + \frac{x - 3}{2} \left(7 - \frac{4}{6} (0) \right)
$$
$$
f_1(x) = \frac{(5 - x)^3}{32} \cdot 3 + \frac{5 - x}{2} \left(4 - \frac{1}{4} \right) + \frac{x - 3}{2} (7)
$$
$$
f_1(x) = \frac{3(5 - x)^3}{32} + (5 - x) \cdot \frac{15}{8} + \frac{7(x - 3)}{2}
$$

Thus, the piecewise cubic spline function is:
$$
f(x) = 
\begin{cases} 
\frac{(x - 1)^3}{32} + 3 - x + \frac{15(x-1)}{8}, &x \in [1,3] \\
\frac{3(5 - x)^3}{32} + (5 - x) \cdot \frac{15}{8} + \frac{7(x - 3)}{2}, &x \in [3,5]
\end{cases}
$$


## Applications
- Used in numerical analysis for function approximation.
- Commonly applied in computer graphics and animation.
- Useful in engineering and physics for smooth curve fitting.

## Limitations
- Requires solving a system of linear equations, increasing computational complexity.
- Can still produce oscillatory behavior if data points are not well distributed.