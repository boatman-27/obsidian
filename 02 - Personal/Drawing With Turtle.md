## Butterfly function
$$
r = e^{\sin\theta} - 2\cos(4\theta) + \left(\sin\left(\frac{2\theta - \pi}{24}\right)\right)^{5}
$$

``` python
import turtle
import math


colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up the screen
turtle.setup(width=800, height=800)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
  
# Define the polar equation
def polar_to_cartesian(theta):
	r = math.exp(math.sin(theta)) - 2 * math.cos(4 * theta) + (math.sin((2 * theta - math.pi) / 24)) ** 5
	x = r * math.cos(theta) * 100
	y = r * math.sin(theta) * 100	
	return x, y

  

# Draw the graph
turtle.penup()
for theta in range(0, 3600 * len(colors)):
	theta_rad = math.radians(theta / 10)
	x, y = polar_to_cartesian(theta_rad)
	turtle.goto(x, y)
	turtle.pendown()

	# Change color every 3600 steps (2π radians)
	if theta % 3600 == 0:
	turtle.color(colors[(theta // 3600) % len(colors)])

turtle.done()
```


---

## Infinity
```python
import turtle
import math
  
SCALE = 100

def topRight(multiplier: int):

	for i in range(0, 201):
		x = i / 100
	try:
		y = math.sqrt(x ** 2 - x ** 4)
		turtle.goto(x * SCALE * (multiplier + 1), y * SCALE * (multiplier + 1))
		turtle.pendown()
	except ValueError:
		continue

  

def bottomRight(multiplier: int):

	for i in range(201, 0, -1):
		x = i / 100
	try:
		y = -math.sqrt(x ** 2 - x ** 4)
		turtle.goto(x * SCALE * (multiplier + 1), y * SCALE * (multiplier + 1))
		turtle.pendown()
	except ValueError:
		continue

def topLeft(multiplier: int):

	for i in range(0, 201):
		x = -i / 100
	try:
		y = math.sqrt(x ** 2 - x ** 4)
		turtle.goto(x * SCALE * (multiplier + 1), y * SCALE * (multiplier + 1))
		turtle.pendown()
	except ValueError:
		continue

def bottomLeft(multiplier: int):
	for i in range(201, 0, -1):
		x = -i / 100
	try:
		y = -math.sqrt(x ** 2 - x ** 4)
		turtle.goto(x * SCALE * (multiplier + 1), y * SCALE * (multiplier + 1))
		turtle.pendown()
	except ValueError:
		continue

# Colors for the curve
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up the screen
turtle.setup(width=900, height=900)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()

for i in range(0, len(colors)):
	turtle.color(colors[i])
	topRight(i)
	bottomRight(i)
	topLeft(i)
	bottomLeft(i)
	
turtle.done()
```

---
## Spiral
$$
r = \frac{1}{\theta + 1}$$

```python
import turtle
import math

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up the screen
turtle.setup(width=800, height=800)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
  
# Define the polar equation
def polar_to_cartesian(theta):
	r = 1 / (theta + 1)
	x = r * math.cos(theta) * 100
	y = r * math.sin(theta) * 100	
	return x, y

  

# Draw the graph
turtle.penup()
for theta in range(0, 3600 * len(colors)):
	theta_rad = math.radians(theta / 10)
	x, y = polar_to_cartesian(theta_rad)
	turtle.goto(x, y)
	turtle.pendown()

	# Change color every 3600 steps (2π radians)
	if theta % 3600 == 0:
	turtle.color(colors[(theta // 3600) % len(colors)])

turtle.done()
```

---

## Cardioid ("heart-shaped" ish)

$$
r = 1 + sin(-\theta)
$$

```python
import turtle
import math

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set up the screen
turtle.setup(width=800, height=800)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
  
# Define the polar equation
def polar_to_cartesian(theta):
	r = 1 + math.sin(-theta)
	x = r * math.cos(theta) * 100
	y = r * math.sin(theta) * 100	
	return x, y

  

# Draw the graph
turtle.penup()
for theta in range(0, 3600 * len(colors)):
	theta_rad = math.radians(theta / 10)
	x, y = polar_to_cartesian(theta_rad)
	turtle.goto(x, y)
	turtle.pendown()

	# Change color every 3600 steps (2π radians)
	if theta % 3600 == 0:
	turtle.color(colors[(theta // 3600) % len(colors)])

turtle.done()

```

--- 

