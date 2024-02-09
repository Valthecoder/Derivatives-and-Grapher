# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
from sympy import *
import sympy as smp
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative
x, a, b, c = smp.symbols('x a b c', real=True)
func_y = input("Enter a Function: \n")

print(func_y)

dydx = smp.diff(func_y, x)
print("dy/dx or y'=", dydx)
dydx.subs([(x, 4), (a, 1), (b, 2), (c, 3)]).evalf()
dydx_f = smp.lambdify((x, a, b, c), dydx)
x = np.linspace(1, 2, 100)
y = dydx_f(x, a=1, b=2, c=3)
plt.plot(x, y)
plt.ylabel('$dy / dx$', fontsize=24)
plt.xlabel('$x$', fontsize=24)
plt.show()
