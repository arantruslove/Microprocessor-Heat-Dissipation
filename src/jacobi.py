import numpy as np
from typing import Callable


def next_interior(
    t_left,
    t_right,
    t_btm,
    t_top,
    k_centre,
    power,
    step_size,
):
    """
    Operation: 1
    Finds the next iteration of an interior point.
    """
    return 0.25 * (
        t_left + t_right + t_btm + t_top + (step_size**2 * power) / k_centre
    )


def next_left(
    t_centre,
    t_right,
    t_btm,
    t_top,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 2
    Finds the next iteration of a point on a left boundary.
    """
    return 0.25 * (
        2 * t_right
        + t_btm
        + t_top
        + (step_size**2 * power) / k_centre
        - 2 * step_size * boundary(t_centre) / k_centre
    )


def next_right(
    t_centre,
    t_left,
    t_btm,
    t_top,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 3
    Finds the next iteration of a point on a right boundary.
    """
    return 0.25 * (
        2 * t_left
        + t_btm
        + t_top
        + (step_size**2 * power) / k_centre
        - 2 * step_size * boundary(t_centre) / k_centre
    )


def next_btm(
    t_centre,
    t_left,
    t_right,
    t_top,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 4
    Finds the next iteration of a point on a bottom boundary.
    """
    return 0.25 * (
        t_left
        + t_right
        + 2 * t_top
        + (step_size**2 * power) / k_centre
        - 2 * step_size * boundary(t_centre) / k_centre
    )


def next_top(
    t_centre,
    t_left,
    t_right,
    t_btm,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 5
    Finds the next iteration of a point on a top boundary.
    """
    return 0.25 * (
        t_left
        + t_right
        + 2 * t_btm
        + (step_size**2 * power) / k_centre
        - 2 * step_size * boundary(t_centre) / k_centre
    )


def next_btm_left(
    t_centre,
    t_right,
    t_top,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 6
    Finds the next iteration of a point on a bottom-left corner.
    """

    return 0.25 * (
        2 * t_right
        + 2 * t_top
        + (step_size**2 * power) / k_centre
        - 4 * step_size * boundary(t_centre) / k_centre
    )


def next_btm_right(
    t_centre,
    t_left,
    t_top,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 7
    Finds the next iteration of a point on a bottom-right corner.
    """
    return 0.25 * (
        2 * t_left
        + 2 * t_top
        + (step_size**2 * power) / k_centre
        - 4 * step_size * boundary(t_centre) / k_centre
    )


def next_top_left(
    t_centre,
    t_right,
    t_btm,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 8
    Finds the next iteration of a point on a top-left corner.
    """
    return 0.25 * (
        2 * t_right
        + 2 * t_btm
        + (step_size**2 * power) / k_centre
        - 4 * step_size * boundary(t_centre) / k_centre
    )


def next_top_right(
    t_centre,
    t_left,
    t_btm,
    k_centre,
    power,
    boundary: Callable,
    step_size,
):
    """
    Operation: 9
    Finds the next iteration of a point on a top-right corner.
    """
    return 0.25 * (
        2 * t_left
        + 2 * t_btm
        + (step_size**2 * power) / k_centre
        - 4 * step_size * boundary(t_centre) / k_centre
    )


def next_interface(
    t_btm,
    t_top,
    k_btm,
    k_top,
):
    """
    Operation: 10
    Finds the next iteration of a point on a top-right corner.
    """
    return (k_btm * t_btm + k_top * t_top) / (k_btm + k_top)


def jacobi_poisson_iteration(
    old: np.ndarray,
    op_mask: np.ndarray,
    pow_mask: np.ndarray,
    k_centre: np.ndarray,
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
        k_centre[op_mask == 1],
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
        pow_mask[op_mask == 9],
        boundary,
        step_size,
    )

    # Material interface
    new[op_mask == 10] = next_interface(
        t_btm[op_mask == 10],
        t_top[op_mask == 10],
        k_btm[op_mask == 10],
        k_top[op_mask == 10],
    )

    return new
