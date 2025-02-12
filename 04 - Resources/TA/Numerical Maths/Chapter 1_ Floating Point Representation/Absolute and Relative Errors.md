## Error Definitions

### Absolute Error
The **absolute error** is the absolute value of the difference between the number \( x \) and its finite representation \( fl(x) \).

$$
\text{a.e.} = |x - fl(x)|
$$

#### Key Points
- The absolute error represents the magnitude of the deviation without considering the relative scale of $x$.
- It is often used when comparing measurements or when $x$ has a fixed and well-understood range.
- Absolute error is expressed in the same units as $x$.

---

### Relative Error
The **relative error** is the ratio of the absolute error and the number $x$:

$$
\text{r.e.} = \frac{|x - fl(x)|}{|x|} \geq 0
$$

### Key Points
- Relative error expresses the error as a proportion of the actual value, making it dimensionless.
- It allows for easier comparison of errors across different scales.
- Often represented as a percentage:

$$
\text{Percentage Relative Error} = \frac{|x - fl(x)|}{|x|} \times 100\%
$$

---

### General Notes
- The **absolute error** is strongly dependent on the magnitude of $x$.
- The absolute error can be **misleading** unless it is stated what it is an error of.
- The **relative error** is a measure of the number of significant digits of $x$ that are correct.
- Relative error is meaningful even when $x$ is not precisely known, as it can convey a percentage deviation.

---

## Practical Applications
- **Science and Engineering**: Estimating precision and accuracy in experiments or calculations.
- **Computing**: Assessing floating-point representation errors in numerical computations.
- **Statistics**: Understanding measurement errors in data collection.

---

## Useful Resources
- [Absolute and Relative Error on Wikipedia](https://en.wikipedia.org/wiki/Approximation_error)
- [Error Analysis in Numerical Methods](https://mathworld.wolfram.com/ErrorAnalysis.html)
- [Absolute vs Relative Error](https://www.britannica.com/science/measurement-system/Accuracy-precision-and-error)
- [Significant Figures and Rounding](https://www.nist.gov/pml/weights-and-measures/significant-figures-and-rounding)

---