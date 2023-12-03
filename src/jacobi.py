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
    source_term,
    left_bc,
    right_bc,
    bottom_bc,
    top_bc,
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
            new[i][j] -= (step_width**2) * source_term

            # Left boundary
            if i == 0:
                new[i][j] -= 2 * old[i + 1][j] + 2 * step_width * left_bc

            # Right boundary
            elif i == width - 1:
                new[i][j] += 2 * old[i - 1][j] + 2 * step_width * right_bc

            # Horizontally interior
            else:
                new[i][j] += old[i - 1][j] + old[i + 1][j]

            # Bottom boundary
            if j == 0:
                new[i][j] -= 2 * old[i][j + 1] + 2 * step_width * bottom_bc

            # Top boundary
            elif j == height - 1:
                new[i][j] += 2 * old[i][j - 1] + 2 * step_width * top_bc

            # Vertically interior
            else:
                new[i][j] += old[i][j - 1] + old[i][j + 1]

            new[i][j] /= 4

    return new


def average_surf_temp(temperatures: np.ndarray):
    """
    Determines the average surface temperature of a material given a matrix of
    temperatures.
    """
    height = len(temperatures[0])
    width = len(temperatures)

    surface_temps = []
    # Left boundary
    for i in range(height):
        surface_temps.append(temperatures[0][i])

    # Right boundary
    for i in range(height):
        surface_temps.append(temperatures[width - 1][i])

    # Bottom boundary
    for i in range(width):
        surface_temps.append(temperatures[i][0])

    # Top boundary
    for i in range(width):
        surface_temps.append(temperatures[i][height - 1])

    average_temp = np.mean(surface_temps)
    return average_temp


def jacobi_poisson_solve(
    height,
    width,
    source_term,
    left_bc,
    right_bc,
    bottom_bc,
    top_bc,
    step_width,
    stopping_condition,
    max_iterations,
) -> np.ndarray:
    """
    Solves the poisson equation using the jacobi method. Applies Neumann boundary
    conditions.
    """

    # Initial guess
    value = source_term / 4
    solution = np.full((width, height), value)

    # Track max iterations
    counter = 0
    while True:
        old_solution = deepcopy(solution)

        # Calculating the next iteration
        solution = jacobi_poisson_iteration(
            old_solution, source_term, left_bc, right_bc, bottom_bc, top_bc, step_width
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
