One of the greatest shortcomings of Newton's Method is that it requires the derivative $f'(x)$ of the function $f(x)$ whose root we are trying to find, which is not always possible or "easy" to find. 

The secant method replaces the derivative evaluation in Newton's Method with a **finite difference approximation** based on the two most recent iterates.

Geometrically, instead of drawing a tangent to $f(x)$ at the current iterate $x_n$, you draw a straight line (secant) through the two points $(x_n, f(x_n))$ and $(x_{n-1}, f(x_{n-1}))$. The next iterate $x_{n+1}$ is again the intersection of this secant with the $x$-axis.

The iteration requires two starting values, $x_0$ and $x_1$.

The subsequent iterates are given by:

$$s_n = \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$


$$x_{n+1} = x_n - \frac{f(x_n)}{s_n}$$


Giving the formula:
$$
x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})}
$$

It should be clear that the slope of the secant $s_n$ approximates $f'(x_n)$ in Newton's Method.

## Convergence Properties

The convergence properties of the secant method are similar to those of Newton's Method. Assuming $f'(x)$ and $f''(x)$ are continuous, it can be shown that:

$$e_{n+1} = \frac{1}{2}\frac{f''(\xi)f'(\xi_n)f'(\xi_{n-1})}{f'(\xi)^3} e_n e_{n-1}$$

where $\xi_n$, $\xi_{n-1}$ are points between $x_n$, $x_{n-1}$, and $x^*$; $\xi$ is a point in the interval in $x$ corresponding to the interval in $y$ spanned by $f(x_{n-1})$, $f(x_n)$, and 0.

This is not quadratic convergence, but it is **superlinear convergence**. It can be shown that:

$$e_{n+1} = O(e^{\varphi n})$$

where $\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.6$ is the golden ratio. In other words, when $x_n$ gets close to $x^*$, the number of correct digits is multiplied by $\varphi$ with each iteration. That's almost as fast as Newton's Method! It is a great deal faster than bisection.

## Practical Considerations

Typically, the secant method is very popular because although the convergence rate is not as fast as that of Newton's Method (and so you need a few more iterations to reach a given accuracy), a secant iteration is usually much cheaper than a Newton iteration. This means that ultimately the secant method is actually faster than Newton's Method to find a root to a given accuracy.


```cpp
pair<double, int> secantMethod(double firstGuess, double secondGuess, double tolerance, int maxIterations = 50) {
    // Set precision for floating point numbers
    cout << setprecision(6) << fixed;
    // Print table headers
    cout << setw(10) << "Iteration" 
         << setw(15) << "x(n-1)" 
         << setw(15) << "xn"
         << setw(25) << "x(n+1)" 
         << setw(25) << "f(x(n+1))"
         << setw(15) << "Error" << endl;

    // Print the line separator
    cout << string(105, '-') << endl;

    double fFirstGuess = f(firstGuess); // f(xn-1)
    double fSecondGuess = f(secondGuess); //f(xn)
    int stepCounter = 1;

    // Compute the first new guess
    double newGuess = secondGuess - (fSecondGuess * ((secondGuess - firstGuess) / (fSecondGuess - fFirstGuess)));
    double fNewGuess = f(newGuess);
    double error = abs(newGuess - secondGuess);
    
    while (stepCounter <= maxIterations && (error >= tolerance)) {
        // Print current iteration values
        cout << setw(10) << stepCounter
             << setw(15) << firstGuess
             << setw(15) << secondGuess
             << setw(25) << newGuess
             << setw(25) << f(newGuess)
             << setw(15) << error << endl;
        
        if (abs(fNewGuess) <= tolerance || fNewGuess == 0.0) {
            // root found
            break;
        }

        // Update guesses
        firstGuess = secondGuess;
        secondGuess = newGuess;
        fFirstGuess = f(firstGuess);
        fSecondGuess = f(secondGuess);

        // Compute the new guess
        newGuess = secondGuess - (fSecondGuess * ((secondGuess - firstGuess) / (fSecondGuess - fFirstGuess)));
        fNewGuess = f(newGuess);
        error = abs(newGuess - secondGuess);
        stepCounter++;
    }

    // Print the final iteration's values
    // cout << setw(10) << stepCounter
    //      << setw(15) << firstGuess
    //      << setw(15) << secondGuess
    //      << setw(25) << newGuess
    //      << setw(25) << f(newGuess)
    //      << setw(15) << error << endl;

    return {newGuess, stepCounter};

}
```