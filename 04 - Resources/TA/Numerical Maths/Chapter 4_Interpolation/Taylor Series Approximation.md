***Taylor's Formula:*** if $f(x)$ has derivatives of all orders in an open interval *I* centered around $a$, then:
$$
f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + ... + \frac{f^{(n)}(a)}{n!}(x - a)^n + R_n(x)
$$
where
$$
R_n(x) = \frac{f^{n + 1}(c)}{(n + 1)!}(x - a)^{n + 1}
$$
for some value of $c$ between $a$ and $x$. 

In the context of **Taylor’s Formula**, $I$ is an **open interval** centered around $a$ where the function $f(x)$ has derivatives of all orders. Mathematically, if $I=(a − r, a + r)$  for some $r > 0$, then for every $x$ in $I$, the function $f(x)$ can be approximated by its Taylor polynomial with the remainder term $R_n(x)$ providing the error estimate.

The function $R_n(x)$ is called the remainder of order $n$ or the error term for the approximation of $f(x)$ by $P_n(x)$ over $I$.

#### Example
Let $f(x) = 4 + sin(2x)$. 
1. Find the linear $L(x)$ and quadratic $Q(x)$ approximation to $f(x)$ near $x = 1$.
2. Approximate the values of $f(x)$ for $x = 0.5, 0.75, 1, 1.25, 1.5$ using $L(x)$ and $Q(x)$. Compare the values of your approximations to the actual values. 

first we need to know how many times we need to differentiate, Linear means $n = 1$ and Quadratic means $n = 2$. 

**$L(X)$:**
$L(x) = f(a) + f'(a)(x - a)$

$f(a) = 4 + sin(2a)$
$f'(a) = 2cos(2a)$

near $x = 1$ means $a = 1$. 

so $L(x) = 4 + sin(2a) + 2cos(2a)(x - a)$ at $a = 1$: $L(x) = 4 + sin(2) + 2cos(2)(x - 1)$

**$Q(X)$:**
$Q(x) = L(x) + \frac{f''(a)}{2!}(x - a)^2$ or $Q(x) =  f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2$

$f''(a) = -4sin(2a)$

$Q(x) = 4 + sin(2) + 2cos(2)(x - 1) - \frac{4sin(2a)(x-a)^2}{2!}$ at $a = 1$

$Q(x) = 4 + sin(2) + 2cos(2)(x - 1) - 2sin(2)(x-1)^2$

***NOTE:*** Both functions can be simplified but **ALWAYS** use the full decimal number from the calculator. And the calculator should be in *RADIAN*. 


| x    | f(x) (Actual)              | L(x) (Linear Approx.)                        | Q(x) (Quadratic Approx.)                                           |
| ---- | -------------------------- | -------------------------------------------- | ------------------------------------------------------------------ |
| 0.5  | 4 + sin(1) ≈ 4.841470985   | 4 + sin(2) + 2cos(1)(0.5 - 1) ≈ 5.325444263  | 4 + sin(2) + 2cos(2)(0.5 - 1) - 2sin(2)(0.5 - 1)^2 ≈ 4.87079555    |
| 0.75 | 4 + sin(1.5) ≈ 4.997494987 | 4 + sin(2) + 2cos(2)(0.75 - 1) ≈ 5.117370845 | 4 + sin(2) + 2cos(2)(0.75 - 1) - 2sin(2)(0.75 - 1)^2 ≈ 5.003708667 |
| 1    | 4 + sin(2) ≈ 4.909297427   | 4 + sin(2) + 2cos(2)(1 - 1) ≈ 4.90927427     | 4 + sin(2) + 2cos(2)(1 - 1) - 2sin(2)(1 - 1)^2 ≈  4.90927427       |
| 1.25 | 4 + sin(2.5) ≈ 4.598472144 | 4 + sin(2) + 2cos(2)(1.25 - 1) ≈ 4.701224009 | 4 + sin(2) + 2cos(2)(1.25 - 1) - 2sin(2)(1.25 - 1)^2 ≈ 4.58756183  |
| 1.5  | 4 + sin(3) ≈ 4.141120008   | 4 + sin(2) + 2cos(2)(1.5 - 1) ≈ 4.49315059   | 4 + sin(2) + 2cos(2)(1.5 - 1) - 2sin(2)(1.5 - 1)^2 ≈ 4.038501877   |

From the table, we observe that increasing the number of derivatives used in the approximation improves accuracy. The quadratic approximation $Q(x)$ provides a closer estimate to the actual function values compared to the linear approximation $L(x)$, particularly as $x$ moves further from $x=1$. This shows the importance of higher-order terms in Taylor series expansions for more precise function approximations.


### The Remainder Estimation Theorem
If there is a positive constant $M$ such that $f^{(n+1)}(t) ≤M$ for all $t$ between $x$ and $a$, inclusive, then the remainder term $R_n(x)$ in Taylor’s Theorem satisfies the inequality
$$
|R_n(x)| \leqslant M\frac{|x−a|^{n+1}}{(n+ 1)!}
$$


where
$$
M = f^{(n+1)}(c)
$$

where $M$ represents the maximum possible absolute value of the derivative values.

#### Example

Approximate $f(x) = x^{\frac{2}{3}}$ at point a = 1, with a third order Taylor polynomial, and find the error associated with this approximation on $0.8 \leqslant x \leqslant 1.2$. 

$f(a) = a^{\frac{2}{3}}$

$f'(a) = \frac{2}{3}a^{-\frac{1}{3}}$

$f''(a) = -\frac{2}{9}a^{-\frac{4}{3}}$

$f'''(a) = \frac{8}{27}a^{-\frac{7}{3}}$

$T_3(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3$

$T_3(x) = 1 + \frac{2}{3}(x-1) -\frac{1}{9}(X-1)^2 + \frac{4}{81}(x-1)^3$

In order to find the error associated with the approximation, we need to use the Remainder Theorem. so we need to find $f^{n+1}(c)$ 

$f^4(c) = -\frac{56}{81}x^{-\frac{10}{3}}$

To find $M$, we need to substitute the bounds and the center point of the given interval $i.e$ $0.8, 1, 1.2$. And we choose the Maximum absolute value. 

$M(0.8) = -\frac{56}{81}(0.8)^{-\frac{10}{3}} = 1.4546$
$M(1) = -\frac{56}{81}(1)^{-\frac{10}{3}} = 0.691$
$M(1.2) = -\frac{56}{81}(1.2)^{-\frac{10}{3}} = 0.3765$

$M(0.8)$ has the bigger value. 

so...

$$
R_3(x) \leqslant \frac{|-\frac{56}{81}(0.8)^{-\frac{10}{3}}|}{4!} |0.8 - 1|^4 = 0.0000969
$$

you can also choose to approximate the value of $M$ to $1.5$ giving $R_3(x) \leqslant 0.0001$. Both are right. 


## **Derivation of the Taylor Series**
To approximate $f(x)$ near $x = a$, we can use Power series.

We know that the Power series can be defined as

  

$$

f(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + \dots

$$

  

When $x = 0$,

  

$$

f(0) = a_0

$$

  

So, differentiate the given function:

  

$$

f'(x) = a_1 + 2a_2x + 3a_3x^2 + 4a_4x^3 + \dots

$$

  

Again, when you substitute $x = 0$, we get:

  

$$

f'(0) = a_1

$$

  

Differentiate again:

  

$$

f''(x) = 2a_2 + 6a_3x + 12a_4x^2 + \dots

$$

  

Now, substituting $x=0$ in the second-order derivative:

  

$$

f''(0) = 2a_2

$$

  

Thus,

  

$$

\frac{f''(0)}{2!} = a_2

$$

  

By generalizing, we obtain:

  

$$

\frac{f^n(0)}{n!} = a_n

$$

  

Now, substituting these values into the power series, we get:

  

$$

f(x) = \sum_{n=0}^{\infty} \frac{f^n(0)}{n!} x^n

$$

  

Generalizing $f(x)$ in a more general form:

  

$$

f(x) = b + b_1 (x-a) + b_2( x-a)^2 + b_3 (x-a)^3+ \dots

$$

  

Now, when $x = a$, we get:

  

$$

b_n = \frac{f^n(a)}{n!}

$$

Thus, the **Taylor series** expansion of $f(x)$ around $x = a$ is:

$$
f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + ... + \frac{f^{(n)}(a)}{n!}(x - a)^n + R_n(x)
$$

where $R_n(x)$ is the remainder term that accounts for the error when truncating the series at $n$ terms.

## **Why Does It Work?**
The Taylor series works well for functions that are **infinitely differentiable** in an interval around $a$. The more terms we include, the better the approximation becomes. For sufficiently smooth functions, the remainder term $R_n(x)$ vanishes as $n \to \infty$, making the Taylor series an exact representation of the function.