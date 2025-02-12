## Introduction

In numerical mathematics, the **conditioning of a problem** refers to its sensitivity to small changes in input. A problem is said to be well-conditioned if small changes in the input lead to proportionally small changes in the output. Conversely, a problem is ill-conditioned if small changes in the input result in disproportionately large changes in the output.

The conditioning of a problem is an inherent property of the problem itself and is independent of the numerical method used to solve it.

---

## Key Concepts

1. **Well-Conditioned Problem**  
   A problem is well-conditioned if:  
   $$
   \frac{\Delta \text{output}}{\text{output}} \approx \frac{\Delta \text{input}}{\text{input}}
   $$

2. **Ill-Conditioned Problem**  
   A problem is ill-conditioned if:  
   $$
   \frac{\Delta \text{output}}{\text{output}} \gg \frac{\Delta \text{input}}{\text{input}}
   $$

3. **Condition Number**  
   The condition number, $\kappa$, quantifies the conditioning of a problem. For a function $f(x)$, the condition number is defined as:  
   $$
   \kappa = \left| \frac{x}{f(x)} \cdot f'(x) \right|
   $$  
   where $f'(x)$ is the derivative of $f(x)$.

   - If $kappa$ is close to 1, the problem is well-conditioned.
   - If $kappa$ is very large, the problem is ill-conditioned.

---

## Examples

### Example 1: Function Evaluation
Consider the function $f(x) = x^2$ at $x = 2$
#### Step 1: Find the Derivative
$f'(x) = 2x$

#### Step 2: Calculate the Condition Number
$$
\kappa = \left| \frac{x}{f(x)} \cdot f'(x) \right| = \left| \frac{2}{2^2} \cdot 2 \cdot 2 \right| = \left| \frac{2}{4} \cdot 4 \right| = 2
$$

#### Interpretation
The condition number $kappa = 2$ indicates that the function is well-conditioned, as small changes in $x$ lead to small proportional changes in $f(x)$.

---

### Example 2: Solving a System of Linear Equations
Solve the system of equations:  
$$
Ax = b, \quad \text{where } A = \begin{bmatrix} 1 & 2 \\ 2 & 3.999 \end{bmatrix}, \quad b = \begin{bmatrix} 3 \\ 7 \end{bmatrix}
$$

#### Step 1: Compute the Condition Number of \( A \)
The condition number for a matrix is given by:
$$
\kappa(A) = \|A\| \cdot \|A^{-1}\|
$$

Using a matrix norm:
$$
\|A\| = \max_{\text{column sums}} = 5.999, \quad A^{-1} = \begin{bmatrix} -2000 & 1000 \\ 1000 & -500 \end{bmatrix}, \quad \|A^{-1}\| = 2500
$$

$$
\kappa(A) = 5.999 \cdot 2500 \approx 14997.5
$$

#### Interpretation
The very large condition number indicates that the system is ill-conditioned, meaning small changes in $b$ or $A$ can cause large changes in the solution.

---

### Example 3: Ill-Conditioned Roots of a Quadratic Equation
Solve the quadratic equation $x^2 - 1000x + 1 = 0$.

#### Step 1: Roots Using the Quadratic Formula
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{1000 \pm \sqrt{1000^2 - 4 \cdot 1 \cdot 1}}{2}
$$

$$
x_1 \approx 999.999, \quad x_2 \approx 0.001
$$

#### Step 2: Conditioning Analysis
The roots x<sub>1</sub> and x<sub>2</sub> are very sensitive to small changes in $a, b$ or $c$. For example, a tiny change in $b$ from 1000 to 999.9999 results in significant changes in the roots.

#### Interpretation
This problem is ill-conditioned, especially for the root $x_2$.

---

## Practical Insights

- The condition number helps determine the reliability of numerical solutions.
- Ill-conditioned problems may require higher precision or reformulation to achieve accurate results.
- The condition number should be analyzed before solving problems in sensitive applications, such as engineering or finance.

---

## Additional Resources

- [Condition Number on Wikipedia](https://en.wikipedia.org/wiki/Condition_number)