import numpy as np
import scipy as sp
from . import utils


def diagonal_inverse(matrix):
    """Calculates the inverse of a diagonal matrix."""
    inverse = np.zeros((len(matrix), len(matrix)))

    for i in range(len(matrix)):
        inverse[i][i] = 1 / matrix[i][i]

    return inverse


def decompose(matrix):
    """Decomposes a matrix into the sum of diagonal, lower and upper matrices."""

    diagonal = np.zeros((len(matrix), len(matrix)))
    lower = np.zeros((len(matrix), len(matrix)))
    upper = np.zeros((len(matrix), len(matrix)))

    # Diagonal matrix
    for i in range(len(matrix)):
        diagonal[i][i] = matrix[i][i]

    # Lower matrix
    for i in range(len(matrix)):
        for j in range(i):
            lower[i][j] = matrix[i][j]

    # Upper matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            upper[i][j] = matrix[i][j]

    return diagonal, lower, upper


def fractional_change(current_array, previous_array):
    """
    Determines the fractional change of two vectors, comparing their norms. Used
    when comparing to the stopping condition.
    """
    numerator = utils.euclidean_norm(current_array) - utils.euclidean_norm(
        previous_array
    )
    denominator = utils.euclidean_norm(previous_array)

    return abs(numerator / denominator)


def jacobi_method(matrix, constants, stopping_condition, max_iterations):
    # Decompose the matrix
    diagonal, lower, upper = decompose(matrix)

    # Determine the inverse of the diagonal
    inverse = diagonal_inverse(diagonal)

    solution = np.zeros(len(matrix))

    # Setting a counter for max iterations
    counter = 0
    while True:
        old_solution = solution

        # Determining the next iteration of the solution
        first_term = np.dot(inverse, constants)
        intermediate = np.dot(inverse, lower + upper)
        second_term = np.dot(intermediate, old_solution)
        solution = first_term - second_term

        counter += 1
        if counter > max_iterations:
            raise RuntimeError("Maximum iterations reached")

        # Check for convergence and max iterations
        frac_change = fractional_change(solution, old_solution)
        if frac_change < stopping_condition:
            break

    return solution
