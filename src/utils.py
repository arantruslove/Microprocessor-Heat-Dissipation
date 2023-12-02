"""Utility functions."""
import numpy as np


def euclidean_norm(array: np.ndarray):
    """Determines the Euclidean norm of a vector."""
    norm = 0
    for num in np.nditer(array):
        norm += num**2

    return norm**0.5
