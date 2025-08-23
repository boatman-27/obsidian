---
tags:
  - maths
  - random
date: 2025-05-09T22:57:00
---
## Table of Contents

1. [Introduction](#introduction)
2. [Eigenvalues and Eigenvectors](#eigenvalues-and-eigenvectors)
    - [Definition](#definition)
    - [Geometric Interpretation](#geometric-interpretation)
    - [Algebraic Computation](#algebraic-computation)
3. [Diagonalization of a Matrix](#diagonalization-of-a-matrix)
    - [Definition](#definition-of-diagonalization)
    - [Diagonalizability Conditions](#diagonalizability-conditions)
    - [Procedure to Diagonalize](#procedure-to-diagonalize)
4. [Example: Diagonalizing a Matrix](#example-diagonalizing-a-matrix)
5. [Conclusion](#conclusion)

---

## Introduction

Eigenvalues and eigenvectors are fundamental concepts in linear algebra that appear in many areas of mathematics, physics, engineering, and data science. They help understand the structure of a linear transformation and simplify computations, especially in the context of matrix powers, differential equations, and systems modeling.

---

## Eigenvalues and Eigenvectors

### Definition

Let $A$ be a square matrix of order $n \times n$. A non-zero vector $\vec{v} \in \mathbb{R}^n$ is called an **eigenvector** of $A$ if there exists a scalar $\lambda \in \mathbb{R}$ (or $\mathbb{C}$) such that:

$$
A\vec{v} = \lambda \vec{v}
$$

The scalar $\lambda$ is called the **eigenvalue** corresponding to the eigenvector $\vec{v}$.

$\lambda$ is an *eigenvalue* of $A$ if there is a **non-zero** vector $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ with 
$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \ \cdot \ 

\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \ = \ \lambda \ \cdot \ \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$


$\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ is an Eigenvector of $A$ corresponding to the *Eigenvalue* $\lambda$, any vector $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$ is an *Eigenvector* of $A$ corresponding to $\lambda$ if $\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \neq \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ and 

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix} \ \cdot \ 

\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \ = \ \lambda \ \cdot \ \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
$$

---

### Geometric Interpretation

An eigenvector $\vec{v}$ of a transformation matrix $A$ is a direction in which the transformation only **scales** the vector, not rotate or change its direction. The **eigenvalue** tells us the factor by which the vector is stretched or compressed.

---

### Algebraic Computation

To compute eigenvalues:

1. Start with the **eigenvalue equation**:

$$
A\vec{v} = \lambda \vec{v} \Rightarrow (A - \lambda I)\vec{v} = 0
$$

2. For a **non-trivial solution**, $\vec{v} \neq 0$, we need:

$$
\det(A - \lambda I) = 0
$$

This determinant gives a **characteristic polynomial**, whose roots are the eigenvalues.

3. Once eigenvalues $\lambda_1, \lambda_2, \ldots$ are found, substitute them into $(A - \lambda I)\vec{v} = 0$ to find the **corresponding eigenvectors**.

---

## Diagonalization of a Matrix

### Definition of Diagonalization

A matrix $A \in \mathbb{R}^{n \times n}$ is **diagonalizable** if there exists an invertible matrix $P$ and a diagonal matrix $D$ such that:

$$
A = P D P^{-1}
$$

Equivalently, $D = P^{-1} A P$.

Here, $D$ contains the eigenvalues of $A$ on its diagonal, and the columns of $P$ are the eigenvectors corresponding to these eigenvalues.

---

### Diagonalizability Conditions

A matrix $A$ is diagonalizable if and only if:

- It has **n linearly independent eigenvectors**, or
- The **algebraic multiplicity** of each eigenvalue equals its **geometric multiplicity**.

Diagonalizable matrices include:
- Symmetric matrices (over $\mathbb{R}$)
- Matrices with distinct eigenvalues

---

### Procedure to Diagonalize

1. Compute the eigenvalues $\lambda_i$ by solving $\det(A - \lambda I) = 0$
2. Find the eigenvectors $\vec{v}_i$ for each \lambda_i$
3. Form matrix P$ whose columns are the eigenvectors
4. Form diagonal matrix D$ with eigenvalues on the diagonal
5. Verify: A = P D P^{-1}$

---

## Example: Diagonalizing a Matrix

Let’s diagonalize the matrix:

$$
A = \begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}
$$

### Step 1: Find Eigenvalues

Compute the characteristic polynomial:

$$
\det(A - \lambda I) = \begin{vmatrix}
4 - \lambda & 1 \\
2 & 3 - \lambda
\end{vmatrix} = (4 - \lambda)(3 - \lambda) - 2
$$

$$
= \lambda^2 - 7\lambda + 10
$$

Solve:

$$
\lambda^2 - 7\lambda + 10 = 0 \Rightarrow (\lambda - 5)(\lambda - 2) = 0
$$

So, eigenvalues: \lambda_1 = 5$, \lambda_2 = 2$

---

### Step 2: Find Eigenvectors

#### For $\lambda = 5$:

$$
(A - 5I) = \begin{bmatrix}
-1 & 1 \\
2 & -2
\end{bmatrix}
\Rightarrow \text{Row reduce} \Rightarrow \vec{v}_1 = \begin{bmatrix}1 \\ 1\end{bmatrix}
$$

#### For $\lambda = 2$:

$$
(A - 2I) = \begin{bmatrix}
2 & 1 \\
2 & 1
\end{bmatrix}
\Rightarrow \text{Row reduce} \Rightarrow \vec{v}_2 = \begin{bmatrix}-1 \\ 2\end{bmatrix}
$$

---

### Step 3: Form Matrices $P$ and $D$

$$
P = \begin{bmatrix}
1 & -1 \\
1 & 2
\end{bmatrix}, \quad
D = \begin{bmatrix}
5 & 0 \\
0 & 2
\end{bmatrix}
$$

### Step 4: Verify $A = P D P^{-1}$

Compute $P^{-1}$:

$$
\text{det}(P) = (1)(2) - (-1)(1) = 2 + 1 = 3
$$

$$
P^{-1} = \frac{1}{3} \begin{bmatrix}
2 & 1 \\
-1 & 1
\end{bmatrix}
$$

Now compute:

$$
P D P^{-1} = \begin{bmatrix}
1 & -1 \\
1 & 2
\end{bmatrix}
\begin{bmatrix}
5 & 0 \\
0 & 2
\end{bmatrix}
\frac{1}{3} \begin{bmatrix}
2 & 1 \\
-1 & 1
\end{bmatrix}
= A
$$

Hence, $A$ is diagonalizable.

---

## Conclusion

Understanding eigenvalues and eigenvectors gives deep insight into the structure of a matrix and its transformation properties. Diagonalizing a matrix simplifies computations such as powers of matrices and solutions to systems of differential equations. Not all matrices are diagonalizable, but when they are, it’s often very useful to do so.

---
