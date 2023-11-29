"""Utility functions."""


def euclidean_norm(array):
    """Determines the Euclidean norm of a vector."""
    norm = 0
    for i in range(len(array)):
        norm += array[i] ** 2

    return norm**0.5
