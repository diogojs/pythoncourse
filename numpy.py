# Section 1 - Numpy

# Final Exercise - Solving Linear Algebra
# Word problem

import numpy as np

A = np.array([[1, 1], [1.5, 4]])
b = np.array([2200, 5050])
X = np.linalg.solve(A, b)

print(X)
