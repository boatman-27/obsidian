Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

This form of analysis estimates the coefficients of the linear equation, involving one or more independent variables that best predict the value of the dependent variable. Linear regression fits a straight line or surface that minimizes the discrepancies between predicted and actual output values. There are simple linear regression calculators that use a “least squares” method to discover the best-fit line for a set of paired data.

A **Regression Line** is a straight line that describes how a variable *y* changes as a variable *x* changes. Regression lines are used to predict the value of *y* for a given value of *x*. 

![[Pasted image 20250207215348.png]]

Can be solved in 2 methods:
## 1. Method 1
$$
y = a + bx
$$
where $a$ is the *y-intercept* and $b$ is the *slope*. 

$b = \frac{SS_{xy}}{SS_{xx}}$ and $a = \bar{y} - b \cdot \bar{x}$

$SS_{xy} = \sum xy - \frac{(\sum x) (\sum y)}{n}$ and $SS_{xx} = \sum x^2 - \frac{(\sum x) ^2}{n}$

$SS$ stands for sum of squares. The least squares regression line $y = a + bx$, is also called the regression of y on x. 
$n$ is the number of given data points. 

## 2. Method 2

$$ 
y = ax + b
$$


where $a$ is the *slope* and $b$ is the *y-intercept*. 
$$
a = \frac{n \left( \sum x_i y_i \right) - \left( \sum x_i \right) \left( \sum y_i \right)}
{n \left( \sum x_i^2 \right) - \left( \sum x_i \right)^2},
\quad
b = \frac{\left( \sum x_i^2 \right) \left( \sum y_i \right) - \left( \sum x_i \right) \left( \sum x_i y_i \right)}
{n \left( \sum x_i^2 \right) - \left( \sum x_i \right)^2}
$$


***NOTE:*** **BOTH METHODS WILL GIVE ALMOST IDENTICAL RESULTS, THE ONLY DIFFERENCE CAN BE IN SOME DECIMAL PLACES** 

#### Example:
Consider the following dataset:

| x  | y  |
|----|----|
| 1  | 2  |
| 2  | 3  |
| 3  | 5  |
| 4  | 6  |
| 5  | 8  |
***Using Method 1***
1. Compute the necessary sums:
   $\sum x = 1+2+3+4+5 = 15$
   $\sum y = 2+3+5+6+8 = 24$
   $\sum xy = (1\cdot2) + (2\cdot3) + (3\cdot5) + (4\cdot6) + (5\cdot8) = 70$
   $\sum x^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55$
	 $n = 5$
	 
2. Compute the slope and intercept
	$SS_{xy} = \sum xy - \frac{(\sum x)(\sum y)}{n}$
	$SS_{xy} = 70 - \frac{(15)(24)}{5} = 70 - \frac{360}{5} = 70 - 72 = -2$
	$SS_{xx} = \sum x^2 - \frac{(\sum x)^2}{n}$
	$SS_{xx} = 55 - \frac{(15)^2}{5} = 55 - \frac{225}{5} = 55 - 45 = 10$
	
3. Compute slope and intercept
	$b = \frac{SS_{xy}}{SS_{xx}} = \frac{-2}{10} = -0.2$
	$a = \frac{\sum y}{n} - (-0.2) \cdot \frac{\sum x}{n}$
	$a = \frac{24}{5} - (-0.2) \cdot \frac{15}{5}$
	$a = 4.8 + 0.6 = 5.4$

Thus, the regression line equation is:
$y = 5.4 - 0.2x$

***Using Method 2***
4. Compute the necessary sums:
   $\sum x = 1+2+3+4+5 = 15$
   $\sum y = 2+3+5+6+8 = 24$
   $\sum xy = (1\cdot2) + (2\cdot3) + (3\cdot5) + (4\cdot6) + (5\cdot8) = 70$
   $\sum x^2 = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55$
	 $n = 5$

5. Compute slope and intercept:
   $a = \frac{n \sum xy - (\sum x)(\sum y)}{n \sum x^2 - (\sum x)^2}$
   $a = \frac{5(70) - (15)(24)}{5(55) - (15)^2} = \frac{350 - 360}{275 - 225} = \frac{-10}{50} = -0.2$
   $b = \frac{(\sum x^2)(\sum y) - (\sum x)(\sum xy)}{n(\sum x^2) - (\sum x)^2}$
   $b = \frac{(55)(24) - (15)(70)}{5(55) - (15)^2} = \frac{1320 - 1050}{275 - 225} = \frac{270}{50} = 5.4$

Thus, the regression line equation is:
$y = -0.2x + 5.4$

### Correlation Coefficient
Usually denoted $r$, The correlation coefficient is a number between $-1$ and $1$ that measures how closely the data follow the regression line. 

$$
r = \frac{\frac{1}{n} \sum xy - \bar{x} \bar{y}}{S_x S_y}
$$
where
$$
S_x = \sqrt{\frac{1}{n} (\sum x^2) - (\bar{x})^2}
$$
$$
S_y = \sqrt{\frac{1}{n} (\sum y^2) - (\bar{y})^2}
$$
![[Pasted image 20250207223220.png]]

Rule of thumb for interpreting values of $r$:
- if $|r| \leqslant 0.25$, conclude no linear correlation
- $0.25 < |r| \leqslant 0.5$, conclude weak (positive, negative) linear correlation
- $0.5 < |r| \leqslant 0.75$, conclude moderate (positive, negative) linear correlation
- $|r| > 0.75$, conclude strong (positive, negative) linear correlation

