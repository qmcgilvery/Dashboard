import numpy as np
import sympy as sp
from sympy import *
from sympy.interactive import printing

printing.init_printing(use_latex=True)

# eq1 = sp.Function('eq1')
x, y = symbols('x y')

eq1 = 2 * x + 3 * y, 13
eq2 = Eq(x - y, -1)

row1 = [2, 3, 13]
row2 = [1, -1, -2]
system = Matrix((row1, row2))
print(system)
