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
    Solves the Poisson equation using an iterative method. Applies Neumann boundary
    conditions.
    """
    # Microprocessor index bounds
    xmin = convergence_region["xmin"]
    xmax = convergence_region["xmax"]
    ymin = convergence_region["ymin"]
    ymax = convergence_region["ymax"]

    # Determining the mask of thermal conductivities to the left, right, bottom and top
    # of their original points
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

        convergence_errors = abs(solution - old_solution)

    return solution, convergence_errors
