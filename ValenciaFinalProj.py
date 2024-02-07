# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
from sympy import *
import sympy as sy
import math
y = input("Type your function here: ")

x = sy.Symbol('x')

der = sy.diff(y, x)
der_format = sy.printing.latex(der)
der_format1 = der_format.replace('*', '')
print(der_format1)
