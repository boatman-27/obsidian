Gaussian elimination is a fundamental algorithm in linear algebra used to solve systems of linear equations, find the rank of a matrix, and compute the inverse of an invertible matrix. This method systematically reduces a given matrix to row-echelon form using elementary row operations.

## Basics of Gaussian Elimination
Gaussian elimination involves two major steps:

1. **Forward Elimination**: Transform the matrix into an upper triangular matrix (row-echelon form).
2. **Back Substitution**: Solve the system of equations by back-substituting values from the upper triangular matrix.

### Elementary Row Operations
Gaussian elimination relies on three types of row operations:

1. **Row Swapping**: Interchanging two rows.
2. **Row Scaling**: Multiplying a row by a non-zero scalar.
3. **Row Replacement**: Adding or subtracting a multiple of one row to another row.

These operations preserve the solution set of the system.

---

## Steps for Gaussian Elimination
Consider a system of linear equations represented in matrix form as $A \mathbf{x} = \mathbf{b}$, where $A$ is the coefficient matrix, $\mathbf{x}$ is the vector of variables, and  $\mathbf{b}$ is the vector of constants.

### Step 1: Form the Augmented Matrix
Combine the coefficient matrix $A$ and the constant vector $\mathbf{b}$ into an augmented matrix:
$$
[A | \mathbf{b}]
$$

### Step 2: Forward Elimination
1. **Pivot Selection**: Choose the first non-zero entry in the first column as the pivot. If the pivot is zero, swap rows to bring a non-zero pivot to the top.
2. **Eliminate Below Pivot**: For each row below the pivot, subtract an appropriate multiple of the pivot row to make all entries below the pivot zero.
3. **Repeat for Submatrices**: Move to the next column and repeat the process for the submatrix.

At the end of forward elimination, the matrix will be in upper triangular form.

### Step 3: Back Substitution
1. Start from the last row of the upper triangular matrix.
2. Solve for the variable corresponding to the last column.
3. Substitute the value into the rows above to solve for remaining variables.

---

## Example: Solving a System of Linear Equations
Solve the system of equations:
$$
\begin{aligned}
2x + y - z &= 8, \\
x - y + z &= 3, \\
3x + y + 2z &= 14.
\end{aligned}
$$

### Step 1: Form the Augmented Matrix
$$
\begin{bmatrix}
2 & 1 & -1 & | & 8 \\
1 & -1 & 1 & | & 3 \\
3 & 1 & 2 & | & 14
\end{bmatrix}
$$

### Step 2: Forward Elimination
1. **Eliminate Below First Pivot**:
   - Multiply the first row by $\frac{1}{2}$ and subtract from the second row and place the result in the second row.
   - Multiply the first row by $\frac{3}{2}$ and subtract from the third row and place the result in the third row.

$$
\begin{bmatrix}
2 & 1 & -1 & | & 8 \\
0 & -1.5 & 1.5 & | & -1 \\
0 & -0.5 & 3.5 & | & 2
\end{bmatrix}
$$

2. **Eliminate Below Second Pivot**:
   - Scale the second row.
   - Eliminate the third-row entry in the second column.

$$
\begin{bmatrix}
2 & 1 & -1 & | & 8 \\
0 & -1.5 & 1.5 & | & -1 \\
0 & 0 & 4 & | & 3
\end{bmatrix}
$$

### Step 3: Back Substitution
1. Solve the third row: $z = \frac{3}{4}$.
2. Substitute $z$ into the second row to solve for $y$.
3. Substitute $y$ and $z$ into the first row to solve for $x$.

---

## Applications of Gaussian Elimination
1. **Solving Linear Systems**: Quickly finds solutions to $A \mathbf{x} = \mathbf{b}$.
2. **Matrix Inversion**: By augmenting $A$ with the identity matrix and reducing, we can find $A^{-1}$.
3. **Rank Determination**: Identifying the rank of $A$ by the number of non-zero rows in row-echelon form.

---

## Limitations and Considerations
1. **Numerical Stability**: Pivoting strategies, such as partial or complete pivoting, can improve numerical stability.
2. **Computational Complexity**: Gaussian elimination has a complexity of $O(n^3)$ for $n \times n$ matrices.
3. **Ill-Conditioned Systems**: Small errors in input can lead to significant errors in output for poorly conditioned matrices.

---

Gaussian elimination remains a cornerstone of computational linear algebra due to its simplicity and broad applicability. Mastery of this algorithm is essential for solving practical problems in engineering, physics, computer science, and other fields.
