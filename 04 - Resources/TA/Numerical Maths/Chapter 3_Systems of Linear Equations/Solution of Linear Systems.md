---
tags:
  - numerical
  - maths
date: 2025-02-07T16:45:00
Pqs: "[[Chapter_3_PQs.pdf]]"
Sols: "[[chapter_3_solutions.pdf]]"
---

## Gaussian Elimination 

[[Gaussian Elimination]] is a method for solving linear systems by reducing the augmented matrix of the system to a simpler form (typically row echelon form) through a sequence of row operations. This process involves:

1. **Forward Elimination**:
   - Transform the system into an upper triangular matrix.
   - Use row operations to eliminate the variables below the pivot positions.

2. **Backward Substitution**:
   - Solve for the variables starting from the last row (where only one variable remains) and substitute back to find other variables.

### Key Points:
- Gaussian Elimination is deterministic and provides an exact solution (if no rounding errors occur in numerical computations).
- The method is sensitive to numerical stability, and partial pivoting is often used to improve accuracy.

### Steps in Gaussian Elimination:
1. Identify the pivot element in the current column.
2. Swap rows (if necessary) to position the largest absolute value as the pivot.
3. Scale and subtract rows to create zeros below the pivot.
4. Repeat for subsequent rows and columns.
5. Perform back-substitution to solve for unknowns.

---

## LU Factorization

[[LU Factorization]] (or LU Decomposition) is an alternative method for solving linear systems by decomposing the coefficient matrix \( A \) into two triangular matrices:

$$
A = L \cdot U
$$

Where:
- $L$ is a lower triangular matrix (with ones on the diagonal).
- $U$ is an upper triangular matrix.

### Procedure:
1. **Decomposition**:
   - Factorize \( A \) into \( L \) and \( U \) using a series of Gaussian elimination steps without back-substitution.

2. **Solving**:
   - Solve $L \cdot y = b$ (forward substitution) to find $y$.
   - Solve $U \cdot x = y$ (backward substitution) to find $x$.

### Key Points:
- LU Factorization is particularly efficient for solving multiple systems with the same coefficient matrix but different right-hand sides.
- The factorization requires fewer computations compared to solving each system independently.

---

Both methods form the basis for many numerical techniques used in computational linear algebra. Their application depends on the specific requirements of stability, efficiency, and problem characteristics.
