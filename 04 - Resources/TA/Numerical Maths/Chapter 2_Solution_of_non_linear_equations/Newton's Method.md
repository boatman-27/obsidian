The method works by supposing a guess $x_n$ for a root $x_*$, and our plan is to find a tangent line to $y = f(x)$ at $x = x_n$ and follow it down until it crosses the $x$-axis; that crossing point is called $x_{n+1}$. 

This leads to the iteration 
$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Often $x_{n+1}$ will be closer to $x_*$ than $x_n$ was. This process will be repeated until we are close enough to $x_*$ *($i.e.$, $f(x_{n+1}$ should be close to zero)*. 

The generalization of the above description of Newton’s method is the only viable general-purpose method to solve systems of nonlinear equations. 

---
## Drawbacks

As a general-purpose algorithm for finding zeros of functions, Newton's method has three serious drawbacks:
- The function \(f(x)\) must be smooth.
- The derivative \(f'(x)\) must be computed and *NOT* equal to $0$.

If $f(x)$ is not smooth, then $f'(x)$ doesn't exist, and Newton's method is not defined. 

Computing $f'(x)$ may be problematic. However, the computation of $f'(x)$ can be done using Numerical Differentiation (will be covered in Chapter 5).

---
## Local Convergence and Quadratic Convergence

Local convergence refers to how quickly Newton's method converges to the actual root of the function when you start the iterations from an initial guess that is "close enough" to the root. In simpler terms, it describes how fast the algorithm gets closer to the solution as you iterate, given that the starting point is sufficiently close to the true root.

### Error Behavior

In Newton's method, we start with an initial guess $x_0$, and each subsequent iteration generates a better approximation $x_{n+1}$ to the true root $x_*$. The difference between the current guess and the true root is called the **error**:

$$
e_n = x_* - x_n
$$

where $x_n$ is the approximation at the $n$-th iteration.

The central idea of **local convergence** is how the error behaves as the number of iterations increases. The error shrinks as we approach the true root, and ideally, it should shrink very quickly.

### Quadratic Convergence

The key feature of Newton's method is its **quadratic convergence** (when the method is working properly and the starting guess is close enough to the true root). This means that the error decreases approximately as the **square** of the previous error, i.e.,

$$
e_{n+1} = \frac{1}{2} \frac{f''(\xi)}{f'(x_n)} e_n^2
$$

where $x_i$ is some point between $x_n$ and $x_*$, and $e_n$ is the error at the $n$-th iteration.

This equation shows that the error at the next iteration $e_{n+1}$ is proportional to the square of the error at the current iteration $e_n$. Hence, once you're close enough to the true root, the approximation improves rapidly, with the error shrinking very quickly (much faster than linear methods like bisection).

### Implications of Quadratic Convergence

Quadratic convergence implies that as the method iterates, the number of correct digits in the approximation doubles with each iteration. This is extremely efficient because with each iteration, the approximation gets much more accurate. For example:
- After the first iteration, you might have 1 correct digit.
- After the second iteration, you might have 2 correct digits.
- After the third iteration, you might have 4 correct digits, and so on.

This is a huge advantage over methods with **linear convergence**, like bisection, where the error decreases in a linear fashion ($i.e.$, it improves by a fixed amount each time, leading to much slower convergence).

### Conditions for Quadratic Convergence

For quadratic convergence to happen, certain conditions must be satisfied:
1. **Smoothness of the function**: The function $f(x)$ must be smooth enough that its derivative $f'(x)$ and second derivative $f''(x)$ exist and are continuous. If the function is not smooth or its derivatives are not continuous, Newton's method may fail or converge slowly.
2. **Initial guess proximity to the root**: The starting point $x_0$ must be close enough to the true root $x_*$. If the initial guess is too far from the root, Newton's method may not converge at all or may even diverge.
3. **Derivative is non-zero**: The derivative $f'(x)$ must not be zero at the root. If $f'(x)$ is zero or very close to zero, the method becomes undefined, and the tangent line doesn’t provide useful information for finding the next approximation.

### When Newton's Method Fails

Although quadratic convergence is fast, Newton's method can fail or behave unpredictably in certain situations:
- **If the initial guess is too far from the root**, the method might **diverge** or get stuck in an oscillating pattern.
- If $f'(x_n)$ is very small (close to zero), the method might produce large, unstable steps, leading to poor convergence.
- If the function is not smooth or has discontinuities or sharp corners, the method may not work well.


This is what makes Newton's method powerful and efficient for solving nonlinear equations when these conditions are met.

```cpp
pair<double, int> newtonsMethod(double initialGuess, double tolerance, int maxIterations = 50) {
    // Set precision for floating point numbers
    cout << setprecision(6) << fixed;

    // Print table headers
    cout << setw(10) << "Iteration"
         << setw(20) << "x(n)"
         << setw(20) << "f(xn)" 
         << setw(20) << "f'(xn)"
         << setw(20) << "x(n+1)" 
         << setw(15) << "Error" << endl;

    // Print the line separator
    cout << string(105, '-') << endl;
    double fInitialGuess = f(initialGuess);
    double dInitialGuess = fPrime(initialGuess);
    int stepCounter = 1;

    // Compute the first new guess
    double newGuess = initialGuess - (fInitialGuess / dInitialGuess);
    double error = abs(initialGuess - newGuess);
    
    while (stepCounter <= maxIterations && (error >= tolerance)) {
        // Print current iteration's values
        cout << setw(10) << stepCounter
             << setw(20) << initialGuess
             << setw(20) << fInitialGuess
             << setw(20) << dInitialGuess
             << setw(20) << newGuess
             << setw(15) << error << endl;

        if (abs(fInitialGuess) <= tolerance || fInitialGuess == 0.0) {
            // root found
            cout << fInitialGuess << " is a root." << endl;
            break;
        } 

        // Update Guesses
        initialGuess = newGuess;
        fInitialGuess = f(initialGuess);
        dInitialGuess = fPrime(initialGuess);

        // Checking for Math error (division by zero)
        if (dInitialGuess == 0) {
            cout << "Mathematical Error: can't divide by zero." << endl;
            break;
        }
        // Compute the new guess
        newGuess = initialGuess - (fInitialGuess / dInitialGuess);
        error = abs(initialGuess - newGuess);
        stepCounter++;

    }

    // Print the final iteration's values
    cout << setw(10) << stepCounter
         << setw(20) << fInitialGuess
         << setw(20) << dInitialGuess
         << setw(20) << newGuess
         << setw(15) << error << endl;

    return {newGuess, stepCounter};
}
```