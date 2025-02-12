As mentioned in the main page of Chapter 2: [[Solution of Non-Linear Equations]], we will be interested  in solving equations of the form $f(x) = 0$, because $f(x)$ is not assumed to be linear, it could have any number of solutions, from $0 \to \inf$

In one dimension, if $f(x)$ is continuous , we can make use of the Intermediate Value Theorem [IVT](https://www.sfu.ca/math-coursenotes/Math%20157%20Course%20Notes/sec_ContinuityIVT.html#:~:text=Intermediate%20Value%20Theorem.,f(c)%3DN.) to **bracket** a root, by that i mean we can find numbers $a$ and $b$, such that $f(a)$ and $f(b)$ have different signs and the root lies somewhere in the middle. 

Then the IVT tells us that there is at least one magical value $x_∗ ∈ (a, b)$ such that $f(x_∗) = 0$.

The number $x_*$ is called a *root* or *zero* of $f(x)$.

To bisect means to divide in half. 

When picking the points $a$ and $b$, $f(a)$ and $f(b)$ should always have different signs. Once we have an interval $(a, b)$ in which we know $x_∗$ lies, a systematic way to proceed is to sample $f( \frac{a+b}{2} )$.

if $f( \frac{a+b}{2} ) = 0$ then $x_* = \frac{a+b}{2}$ and thats the root.

Otherwise, the sign of $f( \frac{a+b}{2} )$ will either agree with the sign of $f(a)$, or it will agree with the sign of $f(b)$, suppose that the sign of $f( \frac{a+b}{2} )$ and $f(a)$ agree, then we are no longer guaranteed that $x_∗ ∈ (a, \frac{a+b}{2} )$, but we are still guaranteed that $x_∗ ∈ ( \frac{a+b}{2} , b)$.

so we narrowed down the region where $x_*$ lies, and we continue to repeat by setting $\frac{a+b}{2}$ to $a$ or $b$ (depending on which $f(a)$  or $f(b)$ has a similar sign to $f( \frac{a+b}{2} )$)

Interval bisection is a slow-but-sure algorithm for finding a zero of $f(x)$, where $f(x)$ is a real-valued function of a single real variable.

We assume that we know an interval $[a, b]$ on which a continuous function $f(x)$ changes sign. However, there is likely no floating-point number (or even rational number!) where $f(x)$ is exactly $0$. 

To conclude, Our goal is to Find a (small) interval (perhaps as small as 2 successive floating-point numbers) on which $f(x)$ changes sign. However, Bisection method is **SLOW**, as it can be show that it only adds 1 bit of precision per iteration. 

Starting from 0 bits of accuracy, it always takes 52 steps to narrow the interval in which $x_∗$ lies down to 2 adjacent floating-point numbers. However, bisection is completely **Foolproof**. 

If $f(x)$ is continuous and we have a starting interval on which $f(x)$ changes sign, then bisection is guaranteed to reduce that interval to two successive floating-point numbers that bracket $x_∗$.



![[Bisection Method Definition.png]]



```CPP
pair<double, int> bisectionMethod(double firstEndpoint, double secondEndpoint, double tolerance, int maxIterations = 50) {

	// Set precision for floating point numbers
	cout << setprecision(6) << fixed;

	// Print table headers
	cout << setw(10) << "Iteration"
	<< setw(25) << "firstEndpoint (a)"
	<< setw(25) << "f(a)"
	<< setw(25) << "secondEndpoint (b)"
	<< setw(25) << "f(b)"
	<< setw(25) << "middlePoint (c)"
	<< setw(25) << "f(middlePoint)"
	<< setw(25) << "Error" << endl;
	
	// Print the line separator
	
	cout << string(185, '-') << endl;
	
	double fFirstEndpoint = f(firstEndpoint);
	double fSecondEndpoint = f(secondEndpoint);
	
	// Ensure the function values at the endpoints have opposite signs
	if (fFirstEndpoint * fSecondEndpoint >= 0) {
		cerr << "Error: The function values at the endpoints must have opposite signs.\n"
		<< "f(a) = " << fFirstEndpoint << ", f(b) = " << fSecondEndpoint << endl;
		return {0, 0};
	}
	
	  
	int stepCounter = 0;
	double middlePoint, fMiddlePoint, error, previousMiddlePoint;	
	  
	do {
		previousMiddlePoint = middlePoint;
		middlePoint = (firstEndpoint + secondEndpoint) / 2;
		fMiddlePoint = f(middlePoint);
		
		if (stepCounter > 0) {	
		error = abs(middlePoint - previousMiddlePoint);
		} else {	
		error = abs(middlePoint - firstEndpoint);
		}
		  
		// Print current iteration's values
		cout << setw(10) << stepCounter
		<< setw(25) << firstEndpoint
		<< setw(25) << fFirstEndpoint
		<< setw(25) << secondEndpoint
		<< setw(25) << fSecondEndpoint
		<< setw(25) << middlePoint
		<< setw(25) << fMiddlePoint
		<< setw(25) << error << endl;
		  
		// Check if root is found and tolerance is satisfied
		if (abs(fMiddlePoint) <= tolerance && abs(error) <= tolerance) {
			break;
	
	}
	
		// Narrow the interval
		if (fFirstEndpoint * fMiddlePoint < 0) {
			secondEndpoint = middlePoint; // Root lies in [firstEndpoint, middlePoint]
		} else {
			firstEndpoint = middlePoint; // Root lies in [middlePoint, secondEndpoint]
			fFirstEndpoint = fMiddlePoint; // Update f(a) for the new interval
		}
		stepCounter++;
	} while (stepCounter < maxIterations && abs(error) >= tolerance);

	// Return the root and the number of iterations	
	return {middlePoint, stepCounter};

}
```

