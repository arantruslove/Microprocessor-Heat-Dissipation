import numpy as np
from copy import deepcopy
import src.heat_equations as he


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


def natural_bcs(temperatures: np.ndarray):
    """
    Determines the Neumann boundary conditions for each of the sides of the
    boundaries. Uses ambient temperature at 20 degrees celcius and 150 W/mK for thermal
    conductivity.
    """
    ambient = 20
    left_bcs = he.natural_dissipation(temperatures[0], ambient) / 150
    right_bcs = -he.natural_dissipation(temperatures[-1], ambient) / 150
    bottom_bcs = he.natural_dissipation(temperatures[:, 0], ambient) / 150
    top_bcs = -he.natural_dissipation(temperatures[:, -1], ambient) / 150

    return left_bcs, right_bcs, bottom_bcs, top_bcs


def jacobi_poisson_iteration(
    old: np.ndarray,
    source_term,
    left_bcs: np.ndarray,
    right_bcs: np.ndarray,
    bottom_bcs: np.ndarray,
    top_bcs: np.ndarray,
    step_width,
):
    """
    Given the old iteration solutution, finds the next iteration solution with
    constant Neumann boundary conditions applied (heat flux as a result of contact with
    air).
    """

    # Create a copy with the same shape as the old solution but with zeros
    new = np.zeros_like(old, dtype=float)

    width = len(old)
    height = len(old[0])
    for i in range(width):
        for j in range(height):
            new[i][j] -= (step_width**2) * source_term

            # Left boundary
            if i == 0:
                new[i][j] += 2 * old[i + 1][j] - 2 * step_width * left_bcs[j]

            # Right boundary
            elif i == width - 1:
                new[i][j] += 2 * old[i - 1][j] + 2 * step_width * right_bcs[j]

            # Horizontally interior
            else:
                new[i][j] += old[i - 1][j] + old[i + 1][j]

            # Bottom boundary
            if j == 0:
                new[i][j] += 2 * old[i][j + 1] - 2 * step_width * bottom_bcs[i]

            # Top boundary
            elif j == height - 1:
                new[i][j] += 2 * old[i][j - 1] + 2 * step_width * top_bcs[i]

            # Vertically interior
            else:
                new[i][j] += old[i][j - 1] + old[i][j + 1]

            new[i][j] /= 4

    return new


def jacobi_poisson_solve(
    height,
    width,
    source_term,
    left_bcs,
    right_bcs,
    bottom_bcs,
    top_bcs,
    t_guess,
    step_width,
    stopping_condition,
    max_iterations,
    bc_update_func=None,
) -> np.ndarray:
    """
    Solves the poisson equation using the jacobi method. Applies Neumann boundary
    conditions.
    """

    # Initial guess
    solution = np.full((width, height), t_guess)

    # Track max iterations
    counter = 0
    while True:
        old_solution = deepcopy(solution)

        # Calculating the next iteration
        solution = jacobi_poisson_iteration(
            old_solution,
            source_term,
            left_bcs,
            right_bcs,
            bottom_bcs,
            top_bcs,
            step_width,
        )

        print(np.mean(solution))

        # Update boundary conditions based off the new temperatures
        if bc_update_func:
            left_bcs, right_bcs, bottom_bcs, top_bcs = bc_update_func(solution)

        counter += 1
        if counter > max_iterations:
            print("Max iterations reached")
            break

        # Check for convergence
        frac_change = fractional_change(solution, old_solution)
        if frac_change < stopping_condition:
            break

    return solution
