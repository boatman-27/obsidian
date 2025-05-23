## Curves and Parametric Equations
Parametric equations describe curves in the plane by expressing coordinates as functions of a parameter $t$:
$$
\begin{aligned}
    x &= f(t), \\
    y &= g(t), \quad t \in [a, b].
\end{aligned}
$$
These equations provide a way to represent complex curves that may not be functions in the Cartesian form.

### Example
A common example is the parametric equation of a circle:
$$
\begin{aligned}
    x &= r \cos t, \\
    y &= r \sin t, \quad t \in [0, 2\pi].
\end{aligned}
$$
This represents a circle of radius $r$ centered at the origin.

---
## Length of a Curve (Arc Length)
The arc length $S$ of a curve defined parametrically by $x = f(t)$ and $y = g(t)$ over $t \in [a, b]$ is given by:
$$
S = \int_{a}^{b} \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} dt.
$$



### Example
For the curve $x = t^2, y = t^3$, the arc length from $t = 0$ to $t = 1$ is computed as:
$$
S = \int_{0}^{1} \sqrt{(2t)^2 + (3t^2)^2} dt.
$$

---
## Line Integral and Vector Integral
The line integral of a scalar function $f(x, y)$ along a curve $C$ parameterized by $\mathbf{r}(t) = (x(t), y(t))$ is:
$$
\int_C f(x, y) ds = \int_a^b f(x(t), y(t)) \sqrt{\left( \frac{dx}{dt} \right)^2 + \left( \frac{dy}{dt} \right)^2} dt.
$$

For a vector field $\mathbf{F} = (P, Q)$, the vector line integral is:
$$
\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \left[ P(x, y) \frac{dx}{dt} + Q(x, y) \frac{dy}{dt} \right] dt.
$$

### Example
For $\mathbf{F} = (y, -x)$ and the curve parameterized by $x = \cos t, y = \sin t$, $t \in [0, 2\pi]$, we compute:
$$
\int_C (y dx - x dy).
$$

This integral represents the circulation of $\mathbf{F}$ along the curve.

---

$$
\sqrt{t}
$$