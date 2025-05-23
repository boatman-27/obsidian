Numerical differentiation is a fundamental technique in numerical analysis that approximates the derivative of a function using discrete data points. This approach is particularly useful when analytical differentiation is impractical or when dealing with empirical data. Numerical differentiation is widely applied in physics, engineering, machine learning, and scientific computing.

## Finite Difference Approximations

Finite difference methods estimate derivatives using function values at discrete points. Common finite difference formulas include:

### Forward Difference Formula
The forward difference formula estimates the first derivative of a function $f(x)$ at a point $x$ using a small step size $h$:

$$ 
f'(x) \approx \frac{f(x+h) - f(x)}{h}.
$$
This method is simple but introduces an error proportional to $h$, making it less accurate for large step sizes.

### Backward Difference Formula
The backward difference formula uses a previous point to approximate the derivative:
$$
 f'(x) \approx \frac{f(x) - f(x-h)}{h}.
$$
Like the forward difference, this method has a first-order error term proportional to $h$.

### Central Difference Formula
The central difference method improves accuracy by averaging forward and backward differences:
$$
 f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}.
$$
This method has an error term proportional to $h^2$, making it significantly more accurate than forward or backward differences.


### Construction

Let's say we have a function $f(x) = x^2 - 4x + 5$, after differentiation we get $f'(x) = 2x -4$. if we want the value of the derivative at $x = 2$ we get $f'(2) = 2(2) - 4 = 0$. 

Another way to find the value of the derivative is to find the slope. 
$$
slope = \frac{y_2 - y_1}{x_2 - x_1}
$$
$x_2 - x_1$ can be rewritten as $h$ or the step-size. $y_2$ can be rewritten as $f(x + h)$ and $y_1$ can be rewritten as $f(x)$. Giving:
$$
f'(x) \approx \frac{f(x+h) - f(x)}{h}.
$$


This can be proved by using limits and by substituting $x+h$ in the $f(x)$ and finding the limit as $h \to 0$. 

We compute the derivative using the definition:
$$
\lim_{h \to 0} \frac{((x+h)^2 -4(x+h) +5) - (x^2 - 4x + 5)}{h}
$$
Expanding and simplifying:
$$
\lim_{h \to 0} \frac{x^2 +2xh +h^2 -4x -4h + 5 -x^2  + 4x -5 }{h}
$$
$$
\lim_{h \to 0} \frac{2xh + h^2 - 4h}{h}
$$
$$
\lim_{h \to 0} (2x + h - 4) = 2x - 4.
$$
Thus, the derivative of $f(x)$ is $f'(x) = 2x - 4$.
## Higher-Order Derivatives

Finite difference methods can be extended to approximate higher-order derivatives. For example, the second derivative can be approximated using the central difference method:
$$
 f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}.
$$
This is useful in solving differential equations and analyzing curvature in data.

## Error Analysis

The accuracy of numerical differentiation depends on the choice of step size $h$. A smaller $h$ reduces truncation error but increases rounding error due to floating-point precision limitations. To balance these errors, adaptive step-size techniques or Richardson extrapolation can be employed.

## Applications

Numerical differentiation is used in:
- **Physics and Engineering**: Estimating rates of change in experimental data.
- **Scientific Computing**: Solving differential equations and optimization problems.
- **Machine Learning**: Computing gradients for training neural networks.

