## Introduction
Quadratic spline interpolation is a method used to approximate a function by connecting given data points with piecewise quadratic polynomials. It provides a smoother approximation compared to linear splines by ensuring continuity in both function values and first derivatives at the data points.
## Definition
Given a set of data points:
$$
(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)
$$
where $x_0 < x_1 < ... < x_n$, the quadratic spline consists of piecewise quadratic functions $Q_i(x)$ defined in each interval $[x_i, x_{i+1}]$.

## Construction
For each interval $[x_i, x_{i+1}]$, the quadratic spline $Q_i(x)$ is given by:
$$
Q_i(x) = f(x_i) + z_i (x - x_i) + \frac{z_{i+1} - z_i}{2(x_{i+1} - x_i)} (x - x_i)^2
$$
where $z_i$ values are computed recursively as:
$$
\begin{cases}
z_0 = 0 & \text{(if we assume } f''(x_0) = 0\text{)} \\
z_{i+1} = -z_i + 2 \left( \frac{f(x_{i+1}) - f(x_i)}{x_{i+1} - x_i} \right) & \text{for } i = 0,1, ..., n
\end{cases}
$$

## Algorithm
1. Given the data points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, sort them if necessary.
2. Compute $z_i$ values recursively using the given formula.
3. Construct the piecewise quadratic splines using the equation for $Q_i(x)$.

## Example
Given the data points:

$$
(1, 2), (3, 4), (5, 6)
$$

We compute $z_0, z_1,$ and $z_2$ using the recursive formula and substitute them into $Q_i(x)$ for each interval.
$$
\begin{aligned}
&\text{Given that } z_o \text{ is always } = 0, \text{ all we have to do is find the values of } z_1 \text{ and } z_2. \\ \\
&\text{At } i = 0, \\
&z_{0 + 1} = -0 + 2\left(\frac{4-2}{3-1}\right) = 2 \\ \\
&\text{At } i = 1, \\
&z_{1 + 1} = -2 + 2\left(\frac{6-4}{5-3}\right) = 0 \\
&\text{Moving on, we need to find an equation for each interval using: } \\
&Q_i(x) = f(x_i) + z_i (x - x_i) + \frac{z_{i+1} - z_i}{2(x_{i+1} - x_i)} (x - x_i)^2 \\
&\text{At } i = 0, \\
&Q_0(x) = 2 + 0(x - 1) + \frac{2 - 0}{2(3-1)}(x-1)^2 = 2 + \frac{(x-1)^2}{2} \\ \\
&\text{At } i = 1, \\
&Q_1(x) = 4 + 2(x - 3) + \frac{0 - 2}{2(5-3)}(x-3)^2 = 4 + 2(x-3)  - \frac{(x-3)^2}{2} \\ \\

&Q(x) = 
\begin{cases}
2 + \frac{(x-1)^2}{2}, &x \in [1,3] \\
4 + 2(x-3)  - \frac{(x-3)^2}{2}, &x \in [3,5]
\end{cases}
\end{aligned}
$$

  
## Properties
- **Continuity:** The quadratic spline is continuous across the domain.
- **Smoothness:** The first derivative is continuous at internal points.
- **More Accurate than Linear Spline:** Provides a better approximation than linear interpolation.

## Applications
- Used in numerical analysis for approximating functions.
- Commonly used in data fitting where smooth interpolation is required.
- Applied in engineering and physics for curve fitting.
## Limitations
- More computationally intensive than linear splines.
- Second derivatives are not necessarily continuous.
- Can still exhibit large errors if data points are sparse.