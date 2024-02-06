# Think of a nice and cool program in the Google
# Try Derivatives and Graph Plotting
# Credits the source
# Create some adjustments or new in the program
# Done
# Imports
import sympy as sy

x = sy.Symbol('x')


y = 5*x**3 - 3*x


der = sy.diff(y, x)
der_format = sy.printing.latex(der)
der_format1 = der_format.replace('*', '')
print(der_format1)
print(type)

