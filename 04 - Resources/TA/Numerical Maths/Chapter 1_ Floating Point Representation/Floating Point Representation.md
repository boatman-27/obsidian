---
tags:
  - numerical
  - maths
date: 2025-02-07T21:10:00
Pqs: "[[Chapter_1_PQs.pdf]]"
Sols: "[[Chapter_1_Solutions.pdf]]"
---

#### This Chapter covers three main parts:
1. Converting from decimal to binary representation (32 and 64 bit IEEE-754 Representation) and vice versa.
2. Floating point rounding errors (Absolute and Relative errors), Conditioning of a problem (well/ill Conditioned)
3. Arithmetic Operations on Binary numbers

## Converting to and from IEEE-754 Representation
Before diving into the converting process, we need to understand the floating point representation of a number in any base. its given by a the formula:

$$
		x = (-1)^S * m * B^e
$$

Where:
S: *Sign (1 negative, 0 positive)*
m: *Mantissa or significand*
e: *Exponent*
B: *Base (can be base 2, 10, 8 16)*

#### IEEE-754 can either be Single or Double precision. 
Single precision numbers are made up of 32 bits, while Double precision numbers are made up of 64 bits.

##### Single Precision:
- 1 sign bit (1, 0)
- 8 Exponent bits
- 23 Mantissa Bits

##### Double Precision
- 1 sign bit (1, 0)
- 11 Exponent bits
- 52 Mantissa Bits

#### Decimal to Binary Conversion
- ##### Whole numbers
	1. Keep dividing by 2 till zero
	2. only divide the whole number by 2. 
	3. when dividing, if the result has a decimal part then put 1, else put 0. 
	4. go from bottom to top

- ##### Fractions
	1. Multiply the fractional part by 2 till one. 
	2. the binary representation is the whole numbers from top to bottom. 

- ##### Whole numbers + Fractions

Converting 89<sub>(10)</sub> to binary<sub>(2)</sub>

![[Pasted image 20250117234332.png]]


Converting 0.625<sub>(10)</sub> to binary<sub>(2)</sub>:

![[Pasted image 20250117234621.png]]


#### Converting Floating Point Decimal to binary 32 floating point format
1. Determine the sign of the decimal number
2. Convert the integral portion to binary
3. convert the fractional portion to binary
4. Normalize the Value of (2 + 3) by adjusting the exponent
5. Add bias to the exponent from step 4 to get the Biased Exponent E
6. Convert E to binary
7. Determine the final bits of the mantissa
8. Put it all together

**Normalization** is the process of moving the decimal point to the left or the right till a number in the format: 
$$
 1.xxxxxx... * 2 ^ e
 $$

**Bias** is used to represent both positive and negative exponents in a way that allows for simpler encoding of floating-point numbers. For single precision, it's 127 and for double precision, it's 1023. [Learn more here](https://en.wikipedia.org/wiki/Exponent_bias)
##### NOTE
the steps to convert from decimal to single or double precision are exactly the same, the only difference is the value of the bias. 


#### Converting Floating Point Binary to decimal (Denormalisation)
1. Determine the sign (s)
2. Determine Biased Exponent E and convert it to decimal
3. Calculate the unbiased exponent $$e =  E - bias $$
4.  Determine the Mantissa and convert it to decimal
5. Sub in the formula $$ x = (-1) ^ s * ( 1 + M) * 2^e$$

## Floating Point Rounding Errors

**Conditioning**: A problem is well-conditioned if small changes in the input leads to small changes in the output, Otherwise, the problem is ill-conditioned. [[Conditioning of a problem]]

### Sources of Error

- #### Data Input
	- ##### Input Error
		The input information is rarely exact since it comes from experiments and any experiment can give results of only limited accuracy. Moreover, the quantity used can be represented in a computer for only a limited number of digits.

- #### Algorithms
	- ##### Algorithmic Errors
		If direct algorithms based on finite sequences of operations are used, errors due to limited steps don’t amplify the existing errors. But if algorithms with infinite steps are used, the algorithm has to be stopped after a finite number of steps.

- #### Computations
	- ##### Computational Errors
		Even when elementary operations, such as multiplication or division, are used, the number of digits increases greatly so that the number cannot be held fully in a register available in a given computer. In such a case, a certain number of digits must be discarded, and this again leads to error.

With the IEEE 32-bit format:
The upper bound U on the representable value of x: 
when s = 0 and $E = 254$ (or $e = 127$) and $m = 1.11111..._2$  
						$U = m . B^e = (1 + 2^{-1} * 2^{-2} * 2^{-3} * ..... * 2^{-23}) * 2^{127} = 3.4026 * 10 ^{38}$

The lower bound L on the representable value of x:
when s = 0 and $E = 1$ (or $e = -127$) and $m = 1.0000$ 
						 $L = m. B^e = (1 + 0) * 2^{-127} = 1.1755 * 10^{-38}$ 

Only the numbers between $-U$ and $-L$, 0 and between $L$ and $U$ can be represented...
when $|x| > U$, the result is an overflow;
when $|x| < L$, the result is an underflow;

### Errors in Scientific Computing 
In numerical analysis, errors are defined as follows. Assume that $x$ is some number and $x*$ is an approximation of x then [[Absolute and Relative Errors]].

## Solved Example:

### Problem
Calculate both the absolute and relative error when the real number \( x = 938 \, 756 \) is stored in 3-digit base-ten floating-point form.

---

### Solution
Reposition the decimal point so that there is one nonzero digit to the left of the decimal point:

$$
x = 938 \, 756 = 9.38756 \cdot 10^5
$$

Since we can only use 3 digits in the mantissa, the value is rounded to:

$$
x^* = 9.39 \cdot 10^5
$$

---

### Absolute Error
The absolute error is calculated as:

$$
\text{Absolute Error} = |x^* - x| = |9.39 \cdot 10^5 - 938 \, 756| = 244
$$

---

### Relative Error
The relative error is calculated as:

$$
\text{Relative Error} = \frac{|x^* - x|}{|x|} = \frac{|9.39 \cdot 10^5 - 938 \, 756|}{|938 \, 756|} \approx 2.6 \cdot 10^{-4}
$$

---

### Interpretation
- The relative error is less than $5 \cdot 10^{-4}$.
- Thus, by definition, we say that $x^* = 9.39 \cdot 10^5$ approximates $x = 938 \, 756$ to **4 significant digits**.
- Note, however, that only the first two leading digits are the same.

---

## Relative Error Bound and Significant Digits

For a number \( p \), if the relative error \( r.e. \) satisfies:

$$
r.e. = \frac{|p - p^*|}{|p|} \leq 5 \cdot 10^{-t}
$$

---

### Derivation
Taking the base-10 logarithm of both sides results in:

$$
\log_{10}(r.e.) \leq \log_{10}(5 \cdot 10^{-t})
$$

Simplifying further:

$$
\log_{10}(r.e.) \leq \log_{10} 5 - t
$$

Rearranging to solve for \( t \):

$$
t \leq \log_{10} \frac{5}{r.e.}
$$

---

### Interpretation
- The value $t$ represents the **number of significant digits** preserved in the approximation.
- A smaller relative error $r.e.$ results in a larger $t$, meaning more significant digits are accurate.
- This inequality provides a mathematical relationship between the relative error and the number of significant digits.

---

### Key Formula
To compute $t$ (the number of significant digits):

$$
t \leq \log_{10} \frac{5}{r.e.}
$$


## Arithmetic Operations on Binary Numbers

Operations can be divided into Addition & Subtraction together and multiplication on its own. 

For **Addition and subtraction**, make sure that the number is in floating point representation with the same exponent for both numbers before doing the operation. 

Addition -> $1 + 1 = 10$, $1 + 0 = 1$. 
Subtraction -> $1 - 1 = 0$, $10 - 1 = 1$, $11 - 1 = 10$, $1 - 0 = 1$.

For **Multiplication**, the exponent doesn't have to be the same, however after multiplying you have to add the exponents. 

The easiest way for multiplication is multiply like normal numbers, where you multiply and move to the left when moving to the next number. 

---

[[Resources/TA/Numerical Maths/PDFs/Chapter # 1 Practice Questions.pdf|Chapter # 1 Practice Questions]]
[[Chapter_1_Solutions.pdf]]




### Additional Links
[Binary Calculator](https://www.calculator.net/binary-calculator.html)
[Number Converter](https://www.rapidtables.com/convert/number/binary-to-decimal.html)


