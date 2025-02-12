Lagrange interpolation is a method for constructing a polynomial that passes through a given set of points. This polynomial is known as the Lagrange interpolating polynomial. It is particularly useful in numerical analysis and approximation when given discrete data points.

## Lagrange Interpolating Polynomial Formula

Given a set of $n + 1$ distinct points:
$$(x_0, y_0), (x_1, y_1), . . ., (x_n, y_n)$$

The Lagrange interpolating polynomial is given by:
$$
P_n(x) = \sum^{n}_{i=0} y_iL_i(x)
$$
where $L_i(x)$ are the Lagrange basis polynomials defined as:
$$
L_i(x) = \prod^{n}_{j=0, j\neq i} \frac{x-x_j}{x_i - x_j}
$$
Each $L_i(x)$ is a polynomial of degree $n$ that takes the value 1 at $x_i$ at and 0 at $x_j$ all other $x_j$ (where $j \neq i$).


The simple idea is that we are trying to construct a polynomial function for each data point and then sum all these functions together to obtain the interpolating polynomial $P(x)$ . Each function should be equal to $1$ at its corresponding data point and 0 at all other given data points. This ensures that when multiplied by the -coordinate of the data point, it reproduces the same $(x,y)$ coordinate.

Each $L_i(x)$ should satisfy the condition that $L_i(x) = 1$ while being 0 at all other $x_j$ (where $j \neg i$). This can be achieved by constructing $L_i(x)$ as a product of linear terms, subtracting from $x$ all other $x_j$ values and normalising by dividing by the product of differences between $x_i$ and all other values $x_j$. This ensures that the function takes the required values at each data point.

## Properties of Lagrange Interpolation

1. **Uniqueness**: The Lagrange polynomial is the unique polynomial of degree at most that interpolates the given points.
    
2. **Explicit Formula**: The polynomial is explicitly given, meaning no system of equations needs to be solved.
    
3. **Efficiency Issues**: The formula involves products and summations, which can make it computationally expensive for large .
    
4. **Numerical Stability**: Lagrange interpolation can suffer from Runge's phenomenon (large oscillations at the edges of an interval) when using equidistant points.

#### Example
Consider the points:
$$
(1,2),(3,6), (4,5)
$$

Construct the Lagrange interpolation of first and second degrees to approximate $x = 1.5$.

#### First Degree:
first degree uses 2 points, so we choose the points that surround the point we need to approximate. so we choose $(1,2), (3,6)$

$$
P_1(x) = L_0(x)y_0 + L_1(x)y_1
$$

$$
L_0(x) \cdot y_0 = \frac{(x-3)}{(1-3)} \cdot 2
$$

$$
L_1(x) \cdot y_1 = \frac{(x-1)}{(3-1)} \cdot 6
$$

$$
P_1(x) = -(x-3) + 3(x-1)
$$

$$
P_1(1.5) = -(1.5-3) + 3(1.5-1) = 3
$$

#### Second Degree:
second degree uses 3 points, so we always choose that 2 points that surround surround the point we need to approximate and the closest point. since we only have 3 points so we use all 3 points. 

$$
P_2(x) = L_0(x)y_0 + L_1(x)y_1 + L_2(x)y_2
$$


$$
L_0(x) \cdot y_0 = \frac{(x -3)(x - 4)}{(1 - 3)(1 - 4)} = \frac{(x -3)(x - 4)}{6} \cdot 2
$$

$$
L_1(x) \cdot y_1 = \frac{(x - 1)(x - 4)}{(3 - 1)(3 - 4)} = -\frac{(x - 1)(x - 4)}{2} \cdot 6
$$

$$
L_2(x) \cdot y_2 = \frac{(x - 1)(x - 3)}{(4 - 1)(4 - 3)} = \frac{(x - 1)(x - 3)}{3} \cdot 5
$$

$$
P_2(x) = \frac{(x -3)(x - 4)}{3} - (x - 1)(x - 4) \cdot 3 + \frac{(x - 1)(x - 3)}{3} \cdot 5
$$

$$
P_2(1.5) = \frac{(1.5 -3)(1.5 - 4)}{3} - (1.5 - 1)(1.5 - 4) \cdot 3 + \frac{(1.5 - 1)(1.5 - 3)}{3} \cdot 5 = 3.75
$$
