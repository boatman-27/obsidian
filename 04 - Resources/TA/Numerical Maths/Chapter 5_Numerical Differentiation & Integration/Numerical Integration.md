Numerical integration is a fundamental technique in numerical analysis used to approximate definite integrals when analytical solutions are difficult or impossible to obtain. Two widely used methods are Simpson's Rule and the Trapezoidal Rule. These methods are essential in physics, engineering, and scientific computing.

## The Trapezoidal Rule

The Trapezoidal Rule approximates the integral of a function $f(x)$ over an interval $[a, b]$ by dividing the region into small trapezoids and summing their areas.

### Formula

The Trapezoidal Rule for a single interval is given by:
$$
 \int_a^b f(x) dx \approx \frac{h}{2} \left[ f(a) + f(b) \right],
$$
where $h = b - a$ is the width of the interval.

For better accuracy, the interval $[a, b]$ is divided into $n$ subintervals of equal width $h = \frac{b-a}{n}$, giving:
$$
 \int_a^b f(x) dx \approx \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{n-1} f(x_i) + f(x_n) \right],
$$
where $x_i = a + i h$ are the subdivision points.

### Example

Consider the integral:
$$
 \int_0^1 x^2 dx.
$$
Using the Trapezoidal Rule with $n = 4$:

1. Divide $[0,1]$ into 4 subintervals with $h = 0.25$.
2. Compute function values:
   - $f(0) = 0^2 = 0$
   - $f(0.25) = (0.25)^2 = 0.0625$
   - $f(0.5) = (0.5)^2 = 0.25$
   - $f(0.75) = (0.75)^2 = 0.5625$
   - $f(1) = 1^2 = 1$
3. Apply the formula:
$$
 I \approx \frac{0.25}{2} [0 + 2(0.0625 + 0.25 + 0.5625) + 1] = 0.328125.
$$
The exact integral is $\frac{1}{3} \approx 0.3333$, showing a small error.

## Simpson's Rule

Simpson's Rule provides a more accurate approximation by using parabolic interpolation instead of linear segments. It is particularly effective for smooth functions.

### Formula

For an even number of subintervals $n$, Simpson's Rule is given by:
$$
 \int_a^b f(x) dx \approx \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1, \text{ odd }}^{n-1} f(x_i) + 2 \sum_{i=2, \text{ even }}^{n-2} f(x_i) + f(x_n) \right],
$$
where $h = \frac{b-a}{n}$ and $x_i = a + i h$.

### Example

Consider the same integral:
$$
 \int_0^1 x^2 dx.
$$
Using Simpson's Rule with $n = 4$:

4. Compute function values:
   - $f(0) = 0^2 = 0$
   - $f(0.25) = 0.0625$
   - $f(0.5) = 0.25$
   - $f(0.75) = 0.5625$
   - $f(1) = 1$
5. Apply the formula:
$$
 I \approx \frac{0.25}{3} [0 + 4(0.0625 + 0.5625) + 2(0.25) + 1] = 0.3333.
$$
This matches the exact integral, demonstrating Simpson’s superior accuracy.

