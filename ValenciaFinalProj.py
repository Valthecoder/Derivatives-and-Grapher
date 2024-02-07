# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
import sympy as smp
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
x, a, b, c = smp.symbols('x a b c', real=True)
func_y = (smp.exp(-a*smp.sin(x**2)) * smp.sin(b**x) * smp.log(c*smp.sin(x))**2 / x)

dydx = smp.diff(func_y, x)
print(dydx)
