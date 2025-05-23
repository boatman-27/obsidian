LU factorization (or decomposition) is a method in numerical linear algebra for decomposing a square matrix $A$ into the product of two matrices:
$$
A = LU,
$$
where:
- $L$ is a lower triangular matrix with ones on the diagonal.
- $U$ is an upper triangular matrix.

LU factorization is widely used to solve systems of linear equations, compute determinants, and find matrix inverses efficiently.

---

## Steps for LU Factorization
To compute the LU factorization of a square matrix $A$, follow these steps:
1. Start with $A$ and initialize $L$ as the identity matrix and $U$ as $A$.
2. Use Gaussian elimination to reduce $A$ to an upper triangular matrix, storing the multipliers in $L$.
### Example Matrix
Consider a matrix $A$:
$$
A = \begin{bmatrix}
2 & 3 & 1 \\
4 & 7 & 3 \\
6 & 18 & 5
\end{bmatrix}.
$$
---
### Step 1: Forward Elimination
3. Divide the first row by the pivot element $a_{11}$:
   - First row remains unchanged: $\begin{bmatrix} 2 & 3 & 1 \end{bmatrix}$.
   - Eliminate below the pivot in the first column:
     $L_{21} = \frac{4}{2}, \quad L_{31} = \frac{6}{2}.$
   Update the second and third rows:
   $$
   \begin{aligned}
   R_2' &= R_2 - L_{21} R_1 = \begin{bmatrix} 0 & 1 & 1 \end{bmatrix}, \\
   R_3' &= R_3 - L_{31} R_1 = \begin{bmatrix} 0 & 12 & 2 \end{bmatrix}.
   \end{aligned}
   $$

4. Continue to the next pivot ($U_{22}$) and eliminate below:
   - $L_{32} = \frac{12}{1}$.
   - Subtract $ L_{32} \times R_2'$ from $R_3'$:
     $R_3'' = \begin{bmatrix} 0 & 0 & -10 \end{bmatrix}$.

After forward elimination:
$$
L = \begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
3 & 12 & 1
\end{bmatrix}, \quad U = \begin{bmatrix}
2 & 3 & 1 \\
0 & 1 & 1 \\
0 & 0 & -10
\end{bmatrix}.
$$

---

## Solving Systems of Equations
Given $A\mathbf{x} = \mathbf{b}$, solve using LU factorization:
5. Compute $L \mathbf{y} = \mathbf{b}$ using forward substitution.
6. Compute $U \mathbf{x} = \mathbf{y}$ using back substitution.

### Example
Solve $A\mathbf{x} = \mathbf{b}$:
$$
A = \begin{bmatrix}
2 & 3 & 1 \\
4 & 7 & 3 \\
6 & 18 & 5
\end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix}
5 \\
10 \\
15
\end{bmatrix}.
$$

7. Perform LU factorization as above.
8. Solve $L \mathbf{y} = \mathbf{b}$:
   $$
   \begin{aligned}
   y_1 &= b_1 = 5, \\
   y_2 &= b_2 - L_{21} y_1 = 10 - 2(5) = 0, \\
   y_3 &= b_3 - L_{31} y_1 - L_{32} y_2 = 15 - 3(5) - 12(0) = 0.
   \end{aligned}
   $$

   $\mathbf{y} = \begin{bmatrix} 5 \\ 0 \\ 0 \end{bmatrix}$.

9. Solve $U \mathbf{x} = \mathbf{y}$:
   $$
   \begin{aligned}
   x_3 &= \frac{y_3}{U_{33}} = \frac{0}{-10} = 0, \\
   x_2 &= \frac{y_2 - U_{23} x_3}{U_{22}} = \frac{0 - 1(0)}{1} = 0, \\
   x_1 &= \frac{y_1 - U_{12} x_2 - U_{13} x_3}{U_{11}} = \frac{5 - 3(0) - 1(0)}{2} = 2.5.
   \end{aligned}
   $$

   $\mathbf{x} = \begin{bmatrix} 2.5 \\ 0 \\ 0 \end{bmatrix}$.

---

## Applications of LU Factorization
10. **Efficient Solving**: Solve multiple systems $A \mathbf{x} = \mathbf{b}$ with different $\mathbf{b}$ values.
11. **Determinant Calculation**: $\det(A) = \prod_{i=1}^n U_{ii}$.
12. **Matrix Inversion**: Compute $A^{-1}$ by solving $A \mathbf{x}_i = \mathbf{e}_i$ for each column of the identity matrix $\mathbf{I}$.

---

## Limitations
13. **Non-Square Matrices**: LU decomposition is only directly applicable to square matrices.
14. **Pivoting**: Numerical stability may require partial or complete pivoting.
15. **Singular Matrices**: LU decomposition fails if $A$ is singular or nearly singular.

---

LU factorization is a powerful tool in numerical computation, forming the basis for solving linear systems, optimization problems, and more. Mastery of this technique is essential in fields like engineering, data science, and applied mathematics.
