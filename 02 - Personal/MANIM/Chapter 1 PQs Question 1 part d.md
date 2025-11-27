```python
from manim import *
import math

class Question1D(Scene):
	def construct(self):

		# Create axes
		axes = Axes(
			x_range=[-6, 6, 1], y_range=[-6, 6, 1], x_length=14, y_length=7, tips=False
		)
		
		axes.add_coordinates()
		self.play(Write(axes))

  

	# Question 1 d), Equation a
	math_text = MathTex(r"x = t^4 - t + 1, y = t^2", font_size=24).to_edge(UL)
	self.play(Write(math_text))
	
	# Parametric function mapped to the axes coordinate system
	parametric_curve = ParametricFunction(
		lambda t: axes.c2p(
			pow(t, 4) - t + 1, pow(t, 2) # Scaled x = sin(t) # y = cos(t)
		),
		t_range=[-12, 12], # Extended range
		color=BLUE,
	)
	
	  
	
	# Animate curve creation
	self.play(Create(parametric_curve, run_time=5))
	self.wait(1)
	
	self.wait(4)
	
	self.play(FadeOut(math_text))
	self.wait(1)
	
	self.play(FadeOut(parametric_curve))
	self.wait(1)
	
	# Question 1 d), Equation b
	math_text = MathTex(r"x = t^2 - 2t, y = \sqrt{t}", font_size=24).to_edge(UL)
	self.play(Write(math_text))
	  
	# Parametric function mapped to the axes coordinate system
	parametric_curve = ParametricFunction(
		lambda t: axes.c2p(
			pow(t, 2) - 2 * t, pow(t, 0.5) 
		),
		t_range=[0, 12], # Extended range
		color=BLUE,
	)
	
	# Animate curve creation
	self.play(Create(parametric_curve, run_time=5))
	self.wait(1)
	  
	self.wait(4)
	
	self.play(FadeOut(math_text))
	self.wait(1)
	
	self.play(FadeOut(parametric_curve))
	self.wait(1)
	
	# Question 1 d), Equation c
	math_text = MathTex(
		r"x = \sin(2t), y = sin(t + sin(2t))", font_size=24
	).to_edge(UL)
	self.play(Write(math_text))
	
	# Parametric function mapped to the axes coordinate system	
	parametric_curve = ParametricFunction(
		lambda t: axes.c2p(
			math.sin(2 * t),
			math.sin(t + math.sin(2 * t)),
		),
		t_range=[-12 * TAU, 12 * TAU], # Extended range	
		color=BLUE,
	)
		
	# Animate curve creation
	self.play(Create(parametric_curve, run_time=5))
	self.wait(1)
	
	self.wait(4)
	  
	self.play(FadeOut(math_text))
	self.wait(1)
	
	self.play(FadeOut(parametric_curve))
	self.wait(1)
	
	  
	
	# Question 1 d), Equation d
	math_text = MathTex(
		r"x = t + sin(4t), y = t^2 + cos(3t)", font_size=24
	).to_edge(UL)
	self.play(Write(math_text))
	
	# Parametric function mapped to the axes coordinate system
	parametric_curve = ParametricFunction(
		lambda t: axes.c2p(
			t + math.sin(4 * t), 
			pow(t, 2) + math.cos(3 * t),
		),
		t_range=[-12 * TAU, 12 * TAU], # Extended range
		color=BLUE,
	)
	
	  
	
	# Animate curve creation
	
	self.play(Create(parametric_curve, run_time=5))
	self.wait(1)
	
	self.wait(4)
  	
	self.play(FadeOut(math_text))	
	self.wait(1)
	
	self.play(FadeOut(parametric_curve))
	self.wait(1)
	
	# Question 1 d), Equation f
	math_text = MathTex(
		r"x = \frac{\sin(2t)}{4 + t^2}, y = \frac{\sin(2t)}{4 + t^2}", font_size=24
	).to_edge(UL)
	self.play(Write(math_text))
	
	# Parametric function mapped to the axes coordinate system
	parametric_curve = ParametricFunction(
		lambda t: axes.c2p(
			math.sin(2 * t) / (4 + pow(t, 2)), 
			math.cos(2 * t) / (4 + pow(t, 2)),
		),
		t_range=[-12 * TAU, 12 * TAU], # Extended range
		color=BLUE,
	)
	
	# Animate curve creation
	self.play(Create(parametric_curve, run_time=5))
	self.wait(1)
	
	self.wait(4)
	self.play(FadeOut(math_text))
	
	self.wait(1)
	
	self.play(FadeOut(parametric_curve))
	self.wait(1)
```


94292215