# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
import sympy as sy


def f(x): return 5*x**3 - 3*x


x = sy.Symbol('x')
der = sy.diff(f(x), x)
print(der)
