import numpy as np
import scipy as sp
from copy import deepcopy


def fractional_change(current_array, previous_array):
    """
    Determines the fractional change of two vectors, comparing their norms. Used
    when comparing to the stopping condition.
    """
    numerator = np.linalg.norm(current_array) - np.linalg.norm(previous_array)
    denominator = np.linalg.norm(previous_array)

    return abs(numerator / denominator)


def jacobi_poisson_iteration(
    old: np.ndarray,
    u0: np.ndarray,
    source_term,
    bc_adjust,
    step_width,
):
    """
    Given the old iteration solutution, finds the next iteration solution with
    constant Neumann boundary conditions applied (heat flux as a result of contact with
    air).
    """

    # Create a copy with the same shape as the old solution but with zeros
    new = np.zeros_like(old)

    width = len(old)
    height = len(old[0])
    for i in range(width):
        for j in range(height):
            new[i][j] += (step_width**2) * source_term

            # Left boundary
            if i == 0:
                new[i][j] += 2 * old[i + 1][j] + 2 * step_width * bc_adjust

            # Right boundary
            elif i == width - 1:
                new[i][j] += 2 * old[i - 1][j] + 2 * step_width * bc_adjust

            # Horizontally interior
            else:
                new[i][j] += old[i - 1][j] + old[i + 1][j]

            # Bottom boundary
            if j == 0:
                new[i][j] += 2 * old[i][j + 1] + 2 * step_width * bc_adjust

            # Top boundary
            elif j == height - 1:
                new[i][j] += 2 * old[i][j - 1] + 2 * step_width * bc_adjust

            # Vertically interior
            else:
                new[i][j] += old[i][j - 1] + old[i][j + 1]

            new[i][j] /= 4
            new[i][j] += u0[i][j]

    return new


def jacobi_poisson_solve(
    height,
    width,
    source_term,
    bc_adjust,
    step_width,
    stopping_condition,
    max_iterations,
) -> np.ndarray:
    """
    Solves the poisson equation using the jacobi method. Applies Neumann boundary
    conditions.
    """

    # Initial guess
    row = [source_term / 4] * height
    u0 = np.array([row] * width)
    solution = np.array([row] * width)
    print(u0)

    # Track max iterations
    counter = 0

    while True:
        old_solution = deepcopy(solution)

        # Calculating the next iteration
        solution = jacobi_poisson_iteration(
            old_solution, u0, source_term, bc_adjust, step_width
        )

        # Check for max iterations
        counter += 1
        if counter > max_iterations:
            raise RuntimeError("Max iterations reached")

        # Check for convergence
        frac_change = fractional_change(solution, old_solution)

        if frac_change < stopping_condition:
            break

    return solution
