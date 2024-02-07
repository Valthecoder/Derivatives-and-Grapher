# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
import sympy as sy
import numpy as np
from scipy.misc import derivative
import sympy as smp
x = smp.Symbol('x')
y = smp.sin(x) * smp.exp(-smp.cos(x)) * x**5 \
            / (smp.sin(10*x**2)+4)


der = smp.diff(y, x)
print(der)
