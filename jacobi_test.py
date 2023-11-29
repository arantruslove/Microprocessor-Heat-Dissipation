# %%
import numpy as np
import src.jacobi as jc

"""Testing the Jacobi module."""

# %% Testing the inverse of a diagonal matrix
matrix = np.array([[3, 0, 0], [0, 3, 0], [0, 0, 3]])
inverse = jc.diagonal_inverse(matrix)
print(inverse)


# %% Testing the matrix decomposition

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

diagonal, lower, upper = jc.decompose(matrix)

print(diagonal)
print(lower)
print(upper)

# %% Testing matrix vector multiplication

matrix1 = np.array([[1, 2], [3, 4]])
array1 = np.array([1, 2])

result = np.dot(matrix1, array1)

print(result)

# %% Testing jacobi method

matrix = np.array([[2, 0, 1], [1, 2, 0], [0, 1, 5]])
constants = np.array([4, -3, 7])

result = jc.jacobi_method(matrix, constants, 1e-15, 10000)

print(result)
