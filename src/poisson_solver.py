import numpy as np
from typing import Callable
from . import jacobi


def fractional_change(current_array, previous_array):
    """
    Determines the fractional change of two vectors, comparing their norms. Used
    when comparing to the stopping condition.
    """
    numerator = np.linalg.norm(current_array) - np.linalg.norm(previous_array)
    denominator = np.linalg.norm(previous_array)

    return abs(numerator / denominator)


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


def poisson_solve(
    initial_temps: np.ndarray,
    op_mask: np.ndarray,
    pow_mask: np.ndarray,
    k_mask: np.ndarray,
    convergence_region: dict,
    step_size,
    stopping_condition,
    max_iterations,
    boundary_func: Callable,
) -> np.ndarray:
    """
    Solves the poisson equation using the jacobi method. Applies Neumann boundary
    conditions.
    """
    # Microprocessor index bounds
    xmin = convergence_region["xmin"]
    xmax = convergence_region["xmax"]
    ymin = convergence_region["ymin"]
    ymax = convergence_region["ymax"]

    # Determining the mask of thermal conductivities to the left, right, bottom and top
    # of their original points
    k_left = np.roll(k_mask, 1, axis=0)
    k_right = np.roll(k_mask, -1, axis=0)
    k_btm = np.roll(k_mask, 1, axis=1)
    k_top = np.roll(k_mask, -1, axis=1)

    # Setting the solution to the initial temperature distribution guess
    solution = initial_temps.copy()

    # Track max iterations
    counter = 0
    while True:
        old_solution = solution.copy()

        # Calculating the next iteration
        solution = jacobi.jacobi_poisson_iteration(
            old_solution,
            op_mask,
            pow_mask,
            k_mask,
            k_left,
            k_right,
            k_btm,
            k_top,
            boundary_func,
            step_size,
        )

        counter += 1
        if counter > max_iterations:
            print("Max iterations reached")
            break

        # Check for convergence of microprocessor temperatures
        frac_change = fractional_change(
            solution[xmin:xmax, ymin:ymax], old_solution[xmin:xmax, ymin:ymax]
        )
        if frac_change < stopping_condition:
            break

    return solution
