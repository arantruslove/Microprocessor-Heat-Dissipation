import numpy as np
from uncertainties import ufloat


def mean_value(grid: np.ndarray, convergence_errors: np.ndarray):
    """
    Determines the mean value of the grid and determines the associated convergence
    uncertainty.
    """

    # Combining grid values with errors
    values = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            error = convergence_errors[i][j]
            values.append(ufloat(val, error))

    # Determining the mean (with uncertainty)
    sum = 0
    for elem in values:
        sum += elem

    return sum / len(values)


def extrapolate(val, half_val):
    """
    Use Richardson extrapolation to determine an estimate for the exact value. val
    and half_val are solutions at an arbitrary step size and half that step size
    respectively.
    """
    return (4 * half_val - val) / 3
