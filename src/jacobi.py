import numpy as np
from typing import Callable


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


def next_interior(
    t_left,
    t_right,
    t_btm,
    t_top,
    k_left,
    k_right,
    k_btm,
    k_top,
    power,
    step_size,
):
    """
    Operation: 1
    Finds the next iteration of an interior point.
    """
    k_tot = k_left + k_right + k_btm + k_top

    return (1 / k_tot) * (
        k_left * t_left
        + k_right * t_right
        + k_btm * t_btm
        + k_top * t_top
        + step_size**2 * power
    )


def next_left(
    t_centre,
    t_right,
    t_btm,
    t_top,
    k_centre,
    k_right,
    k_btm,
    k_top,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 2
    Finds the next iteration of a point on a left boundary.
    """
    k_tot = k_centre + k_right + k_btm + k_top

    return (1 / k_tot) * (
        (k_centre + k_right) * t_right
        + k_btm * t_btm
        + k_top * t_top
        + step_size**2 * power
        - 2 * step_size * boundary(t_centre)
    )


def next_right(
    t_centre,
    t_left,
    t_btm,
    t_top,
    k_centre,
    k_left,
    k_btm,
    k_top,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 3
    Finds the next iteration of a point on a right boundary.
    """
    k_tot = k_centre + k_left + k_btm + k_top

    return (1 / k_tot) * (
        (k_centre + k_left) * t_left
        + k_btm * t_btm
        + k_top * t_top
        + step_size**2 * power
        - 2 * step_size * boundary(t_centre)
    )


def next_btm(
    t_centre,
    t_left,
    t_right,
    t_top,
    k_centre,
    k_left,
    k_right,
    k_top,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 4
    Finds the next iteration of a point on a bottom boundary.
    """
    k_tot = k_centre + k_left + k_right + k_top

    return (1 / k_tot) * (
        k_left * t_left
        + k_right * t_right
        + (k_centre + k_top) * t_top
        + step_size**2 * power
        - 2 * step_size * boundary(t_centre)
    )


def next_top(
    t_centre,
    t_left,
    t_right,
    t_btm,
    k_centre,
    k_left,
    k_right,
    k_btm,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 5
    Finds the next iteration of a point on a top boundary.
    """
    k_tot = k_centre + k_left + k_right + k_btm

    return (1 / k_tot) * (
        k_left * t_left
        + k_right * t_right
        + (k_centre + k_btm) * t_btm
        + step_size**2 * power
        - 2 * step_size * boundary(t_centre)
    )


def next_btm_left(
    t_centre,
    t_right,
    t_top,
    k_centre,
    k_right,
    k_top,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 6
    Finds the next iteration of a point on a bottom-left corner.
    """
    k_tot = 2 * k_centre + k_right + k_top

    return (1 / k_tot) * (
        (k_centre + k_right) * t_right
        + (k_centre + k_top) * t_top
        + step_size**2 * power
        - 4 * step_size * boundary(t_centre)
    )


def next_btm_right(
    t_centre,
    t_left,
    t_top,
    k_centre,
    k_left,
    k_top,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 7
    Finds the next iteration of a point on a bottom-right corner.
    """
    k_tot = 2 * k_centre + k_left + k_top

    return (1 / k_tot) * (
        (k_centre + k_left) * t_left
        + (k_centre + k_top) * t_top
        + step_size**2 * power
        - 4 * step_size * boundary(t_centre)
    )


def next_top_left(
    t_centre,
    t_right,
    t_btm,
    k_centre,
    k_right,
    k_btm,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 8
    Finds the next iteration of a point on a top-left corner.
    """
    k_tot = 2 * k_centre + k_right + k_btm

    return (1 / k_tot) * (
        (k_centre + k_right) * t_right
        + (k_centre + k_btm) * t_btm
        + step_size**2 * power
        - 4 * step_size * boundary(t_centre)
    )


def next_top_right(
    t_centre,
    t_left,
    t_btm,
    k_centre,
    k_left,
    k_btm,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 8
    Finds the next iteration of a point on a top-right corner.
    """
    k_tot = 2 * k_centre + k_left + k_btm

    return (1 / k_tot) * (
        (k_centre + k_left) * t_left
        + (k_centre + k_btm) * t_btm
        + step_size**2 * power
        - 4 * step_size * boundary(t_centre)
    )


def jacobi_poisson_iteration(
    old: np.ndarray,
    op_mask: np.ndarray,
    pow_mask: np.ndarray,
    k_centre: np.ndarray,
    k_left: np.ndarray,
    k_right: np.ndarray,
    k_btm: np.ndarray,
    k_top: np.ndarray,
    boundary: Callable,
    step_size,
):
    """
    Given the old iteration of the solution, finds the next solution with constant
    Neumann boundary conditions applied (heat flux as a result of contact with
    air).
    """
    # Shifted temperature values left, right, bottom and top
    t_left = np.roll(old, 1, axis=0)
    t_right = np.roll(old, -1, axis=0)
    t_btm = np.roll(old, 1, axis=1)
    t_top = np.roll(old, -1, axis=1)

    new = old.copy()
    # Interior point
    new[op_mask == 1] = next_interior(
        t_left[op_mask == 1],
        t_right[op_mask == 1],
        t_btm[op_mask == 1],
        t_top[op_mask == 1],
        k_left[op_mask == 1],
        k_right[op_mask == 1],
        k_btm[op_mask == 1],
        k_top[op_mask == 1],
        pow_mask[op_mask == 1],
        step_size,
    )

    # Left boundary
    new[op_mask == 2] = next_left(
        old[op_mask == 2],
        t_right[op_mask == 2],
        t_btm[op_mask == 2],
        t_top[op_mask == 2],
        k_centre[op_mask == 2],
        k_right[op_mask == 2],
        k_btm[op_mask == 2],
        k_top[op_mask == 2],
        pow_mask[op_mask == 2],
        boundary,
        step_size,
    )

    # Right boundary
    new[op_mask == 3] = next_right(
        old[op_mask == 3],
        t_left[op_mask == 3],
        t_btm[op_mask == 3],
        t_top[op_mask == 3],
        k_centre[op_mask == 3],
        k_left[op_mask == 3],
        k_btm[op_mask == 3],
        k_top[op_mask == 3],
        pow_mask[op_mask == 3],
        boundary,
        step_size,
    )

    # Bottom boundary
    new[op_mask == 4] = next_btm(
        old[op_mask == 4],
        t_left[op_mask == 4],
        t_right[op_mask == 4],
        t_top[op_mask == 4],
        k_centre[op_mask == 4],
        k_left[op_mask == 4],
        k_right[op_mask == 4],
        k_top[op_mask == 4],
        pow_mask[op_mask == 4],
        boundary,
        step_size,
    )

    # Top boundary
    new[op_mask == 5] = next_top(
        old[op_mask == 5],
        t_left[op_mask == 5],
        t_right[op_mask == 5],
        t_btm[op_mask == 5],
        k_centre[op_mask == 5],
        k_left[op_mask == 5],
        k_right[op_mask == 5],
        k_btm[op_mask == 5],
        pow_mask[op_mask == 5],
        boundary,
        step_size,
    )

    # Bottom-left corner
    new[op_mask == 6] = next_btm_left(
        old[op_mask == 6],
        t_right[op_mask == 6],
        t_top[op_mask == 6],
        k_centre[op_mask == 6],
        k_right[op_mask == 6],
        k_top[op_mask == 6],
        pow_mask[op_mask == 6],
        boundary,
        step_size,
    )

    # Bottom-right corner
    new[op_mask == 7] = next_btm_right(
        old[op_mask == 7],
        t_left[op_mask == 7],
        t_top[op_mask == 7],
        k_centre[op_mask == 7],
        k_left[op_mask == 7],
        k_top[op_mask == 7],
        pow_mask[op_mask == 7],
        boundary,
        step_size,
    )

    # Top-left corner
    new[op_mask == 8] = next_top_left(
        old[op_mask == 8],
        t_right[op_mask == 8],
        t_btm[op_mask == 8],
        k_centre[op_mask == 8],
        k_right[op_mask == 8],
        k_btm[op_mask == 8],
        pow_mask[op_mask == 8],
        boundary,
        step_size,
    )

    # Top-right corner
    new[op_mask == 9] = next_top_right(
        old[op_mask == 9],
        t_left[op_mask == 9],
        t_btm[op_mask == 9],
        k_centre[op_mask == 9],
        k_left[op_mask == 9],
        k_btm[op_mask == 9],
        pow_mask[op_mask == 9],
        boundary,
        step_size,
    )

    return new


def jacobi_poisson_solve(
    initial_temps: np.ndarray,
    op_mask: np.ndarray,
    pow_mask: np.ndarray,
    k_mask: np.ndarray,
    step_size,
    stopping_condition,
    max_iterations,
    boundary_func: Callable,
) -> np.ndarray:
    """
    Solves the poisson equation using the jacobi method. Applies Neumann boundary
    conditions.
    """
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
        solution = jacobi_poisson_iteration(
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

        # Check for convergence
        frac_change = fractional_change(solution, old_solution)
        if frac_change < stopping_condition:
            break

    return solution
