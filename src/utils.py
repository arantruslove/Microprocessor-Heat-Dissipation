import numpy as np


def make_subgrids(grid: np.ndarray, n):
    """Splits a numpy array in the x direction into n subgrids"""
    length = len(grid)

    if n > length:
        raise RuntimeError(
            "Matrix size is too small for this operation. Matrix size: {}, n: {}".format(
                length, n
            )
        )

    width = int(length / n)  # Subgrid width

    xmin = 0
    subgrids = []
    for i in range(n - 1):
        xmax = (i + 1) * width
        subgrids.append(grid[xmin:xmax])
        xmin = xmax

    # Append the remaining grid
    subgrids.append(grid[xmin:])

    return subgrids
