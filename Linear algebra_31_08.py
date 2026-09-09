#consider 2 equation: 3x=5y+10 and 4x-2y=7 .
# find the value of x and y using numpy package.

import numpy as np

# Coefficients of x and y
A = np.array([[3, -5],
              [4, -2]])

# Constants
B = np.array([10, 7])

# Solve equations
x, y = np.linalg.solve(A, B)

print("x =", x)
print("y =", y)