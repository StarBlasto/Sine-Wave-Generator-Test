# imported modules
import numpy as n
import matplotlib.pyplot as pl

# parameters
freq = 10 # frequency
dur = 0.2 # duration

# x and y values of the sine wave
# To cite my source, ChatGPT was used as a guideline for the formulas required for this sine wave
x = n.arange(0, dur, 1/500)
y = n.sin(2 * n.pi * freq * x)

# plots the wave
pl.plot(x, y)
pl.title("Sine Wave")
pl.xlabel("X - Axis")
pl.ylabel("Y - Axis")
pl.grid(True)
pl.show()