```python
from manim import *
import math

class ClassActivity(ThreeDScene):
	def construct(self):
	
		# Larger axis range for better fitting
		axes = ThreeDAxes(
			x_range=[-10, 10, 1],
			y_range=[-10, 10, 1],
			z_range=[-10, 10, 1],
			x_length=7,
			y_length=7,
			z_length=7,
			axis_config={"include_tip": False}
		)
		
		# Adjust camera for a better view
		self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES, distance=12)
		
		labels = axes.get_axis_labels(
			MathTex("x").scale(0.7).rotate(PI / 2, axis=RIGHT).shift(RIGHT * 3.5),
			MathTex("y").scale(0.7).rotate(PI / 2, axis=UP).shift(UP * 3.5),
			MathTex("z").scale(0.7).shift(OUT * 3.5)
		)
		
		self.play(Write(axes), run_time = 2)
		self.play(Write(labels), run_time = 2)
		
		# Question 21
		math_text = MathTex(r"x = tcos(t), y = t, z = tsin(t)", font_size=24).to_corner(UL)
		self.add_fixed_in_frame_mobjects(math_text) # Keep text fixed in the frame
		self.play(Write(math_text)) # Animate the writing
		self.wait(1)
		
		parametric_curve = ParametricFunction(
			lambda t: axes.c2p(t * math.cos(t), t, t * math.sin(t)),
			color=GREEN,
			t_range=[0, 20], # Extend helix length
		)
		
		self.play(Create(parametric_curve, run_time=5))
		self.wait(4)
		
		self.play(FadeOut(math_text))
		self.wait(1)
		
		self.play(FadeOut(parametric_curve))
		self.wait(1)	  
		
		# Question 22
		math_text = MathTex(r"x = cos(t), y = sin(t), z = \frac{1}{1 + t^2}", font_size=24).to_corner(UL)
		self.add_fixed_in_frame_mobjects(math_text) # Keep text fixed in the frame
		self.play(Write(math_text)) # Animate the writing
		self.wait(1)
		
		parametric_curve = ParametricFunction(
			lambda t: axes.c2p(math.cos(t), math.sin(t), 1 / (1 + pow(t, 2))),
			color=GREEN,
			t_range=[-20, 20], # Extend helix length
		)
		
		self.play(Create(parametric_curve, run_time=5))
		self.wait(4)
		
		self.play(FadeOut(math_text))
		self.wait(1)
		
		self.play(FadeOut(parametric_curve))
		self.wait(1)
		
		# Question 23
		math_text = MathTex(r"x = t, y = \frac{1}{1 + t^2}, z = t^2", font_size=24).to_corner(UL)
		self.add_fixed_in_frame_mobjects(math_text) # Keep text fixed in the frame
		self.play(Write(math_text)) # Animate the writing
		self.wait(1)
		
		parametric_curve = ParametricFunction(
			lambda t: axes.c2p(t, 1 / (1 + pow(t, 2)), pow(t, 2)),
			color=GREEN,
			t_range=[-10, 10], # Extend helix length
		)
		
		self.play(Create(parametric_curve, run_time=5))
		self.wait(4)
		
		self.play(FadeOut(math_text))
		self.wait(1)
		
		self.play(FadeOut(parametric_curve))
		self.wait(1)
		
		# Question 24
		math_text = MathTex(r"x = cos(t), y = sin(t), z = cos(2t)", font_size=24).to_corner(UL)
		self.add_fixed_in_frame_mobjects(math_text) # Keep text fixed in the frame
		self.play(Write(math_text)) # Animate the writing
		self.wait(1)
		
		parametric_curve = ParametricFunction(
			lambda t: axes.c2p(math.cos(t), math.sin(t), math.cos(2 * t)),
			color=GREEN,
			t_range=[-20, 20], # Extend helix length
		)
		
		self.play(Create(parametric_curve, run_time=5))
		self.wait(4)
		
		self.play(FadeOut(math_text)
		self.wait(1)
		
		self.play(FadeOut(parametric_curve))
		self.wait(1)
		
		# Question 25
		math_text = MathTex(r"x = cos(8t), y = sin(8t), z = e^{0.8t}", font_size=24).to_corner(UL)
		self.add_fixed_in_frame_mobjects(math_text) # Keep text fixed in the frame
		self.play(Write(math_text)) # Animate the writing
		self.wait(1)
		
		parametric_curve = ParametricFunction(
			lambda t: axes.c2p(math.cos(8 * t), math.sin(8 * t), math.exp(0.8 * t)),
			color=GREEN,
			t_range=[0, 20], # Extend helix length
		)
		
		self.play(Create(parametric_curve, run_time=5))
		self.wait(4)
		
		self.play(FadeOut(math_text))
		self.wait(1)
		
		self.play(FadeOut(parametric_curve))
		self.wait(1)
		
		# Question 26
		math_text = MathTex(r"x = cos(t)^2, y = sin(t)^2, z = t", font_size=24).to_corner(UL)
		self.add_fixed_in_frame_mobjects(math_text) # Keep text fixed in the frame
		self.play(Write(math_text)) # Animate the writing
		self.wait(1)
		
		  
		
		parametric_curve = ParametricFunction(
			lambda t: axes.c2p(pow(math.cos(t), 2), pow(math.sin(t), 2), t),
			color=GREEN,
			t_range=[0, 20], # Extend helix length
		)
			
		self.play(Create(parametric_curve, run_time=5))
		self.wait(4)
		
		self.play(FadeOut(math_text))	
		self.wait(1)
	
		self.play(FadeOut(parametric_curve))
		self.wait(1)
```