'''Define 2(A,B) matrices of 3*3 order using numpy arrays.
Perform the following oprtn in the matrices:
1. Find out the inverse of matrix A.
2. Find out the determinant of matrix B.
3. Print the result of (A.A^-1)

'''

import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

B = np.array([[2, 1, 3],
              [1, 2, 4],
              [3, 1, 2]])

# 1. Inverse of matrix A
A_inv = np.linalg.inv(A)
print("Inverse of Matrix A:")
print(A_inv)

# 2. Determinant of matrix B
det_B = np.linalg.det(B)
print("\nDeterminant of Matrix B:")
print(det_B)

# 3. Multiply A with its inverse
result = np.dot(A, A_inv)
print("\nA * A^-1:")
print(result)