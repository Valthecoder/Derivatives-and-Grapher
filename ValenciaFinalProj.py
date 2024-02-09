# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
import sympy.core.add
from sympy import *
from scipy.misc import derivative
import sympy as sym
import math
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

x = Symbol('x')
y = input('Enter a Function : \n Reminders for input: \n (2x: Input 2*x | x²: Input x**2 | '
          'Trigo: Input cos or sin or tan(expression) | arccos: Input acos(expression)'
          'e^4x: Input exp(4*x) | '
          '\n Always follow the parentheses rule for fractions, Thank you! \n y = ')
func_y = sympify(y)
yprime = func_y.diff(x)
print("y' = ", yprime)

x, a, b, c = sym.symbols('x a b c', real=True)
yprime.subs([(x, 4), (a, 1), (b, 2), (c, 3)]).evalf()
yprime_f = sym.lambdify((x, a, b, c), yprime)
x = np.linspace(1, 2, 100)
y = yprime_f(x, a=1, b=2, c=3)
plt.plot(x, y)
plt.ylabel('$dy / dx$', fontsize=24)
plt.xlabel('$x$', fontsize=24)
plt.show()
