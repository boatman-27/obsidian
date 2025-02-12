## Introduction
Linear spline interpolation is a method used to approximate a function by connecting given data points with linear segments. It is one of the simplest forms of spline interpolation and is particularly useful when a smooth curve is not required but a piecewise linear approximation is sufficient.

## Definition
Given a set of data points:
$$
(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)
$$
where  $x_0 < x_1 < ... < x_n$, the linear spline is a piecewise linear function that interpolates between each pair of adjacent points.

## Construction
For each interval $[x_i, x_{i+1}]$, the linear spline $S_i(x)$ is defined as:
$$
S_i(x) = y_i + m_i (x - x_i), \quad x \in [x_i, x_{i+1}]
$$
where $m_i$ is the slope of the line segment between $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$, given by:
$$
m_i = \frac{y_{i+1} - y_i}{x_{i+1} - x_i}
$$

## Properties
1. **Continuity**: The linear spline function is continuous across the entire domain.
2. **Piecewise Linearity**: Each segment is a straight line.
3. **No Smoothness Guarantee**: The first derivative is not necessarily continuous at the data points.
4. **Efficient Computation**: Only requires simple slope calculations and linear interpolation.

## Algorithm
1. Given a set of data points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, sort them if necessary.
2. For each interval $[x_i, x_{i+1}]$:
   - Compute the slope $m_i$.
   - Use the formula $S_i(x) = y_i + m_i (x - x_i)$ to find the interpolated value for any $x$ within the interval.
3. Repeat the process for all intervals.

## Example
Given the data points:
$$
(1, 2), (3, 4), (5, 6)
$$
We compute the slopes:
$$
m_0 = \frac{4 - 2}{3 - 1} = 1, \quad m_1 = \frac{6 - 4}{5 - 3} = 1
$$
The piecewise functions are:
$$
S_0(x) = 2 + 1(x - 1), \quad x \in [1,3]
$$
$$
S_1(x) = 4 + 1(x - 3), \quad x \in [3,5]
$$

## Applications
- Used in numerical analysis for approximating functions.
- Helps in data visualization where a rough estimate is needed.
- Used in engineering and physics for simple approximations.

## Limitations
- Does not ensure smoothness at the data points.
- Not suitable for functions requiring higher-order continuity.
- Can lead to large errors if data points are sparsely distributed.