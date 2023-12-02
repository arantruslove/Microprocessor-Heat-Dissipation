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
    t_a,
    t_surf_0,
    step_width,
    dissipation_func,
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

    # Track max iterations
    counter = 0

    t_surf = t_surf_0
    while True:
        old_solution = deepcopy(solution)

        # Determining boundary condition
        bc_adjust = -dissipation_func(t_surf, t_a) / 150

        # Calculating the next iteration
        solution = jacobi_poisson_iteration(
            old_solution, u0, source_term, bc_adjust, step_width
        )

        # Updating surface temperature
        t_surf = solution[0][0]

        # Check for max iterations
        counter += 1
        if counter > max_iterations:
            raise RuntimeError("Max iterations reached")

        # Check for convergence
        frac_change = fractional_change(solution, old_solution)

        if frac_change < stopping_condition:
            break

    return solution
