import numpy as np
from . import jacobi as jc


def assemble_stiffness_matrix(height, width):
    """
    Creates the stiffness matrix for the Poisson equation solution prior to the
    boundary conditions being applied.
    """

    matrix_size = height * width
    matrix = np.zeros((matrix_size, matrix_size))

    for i in range(matrix_size):
        matrix[i][i] = -4  # Diagonal elements

        if i % height != 0:
            # Left of diagonal, except for left boundary
            matrix[i][i - 1] = 1

        if (i + 1) % height != 0:
            # Right of diagonal, except for right boundary
            matrix[i][i + 1] = 1

        if i - height >= 0:
            # Above diagonal
            matrix[i][i - height] = 1

        if i + height < matrix_size:
            # Below diagonal
            matrix[i][i + height] = 1

    return matrix


class PoissonSolver:
    def __init__(self, height, width, step_size, source_terms: np.ndarray):
        print(len(source_terms))
        print(height * width)

        if len(source_terms) != height * width:
            raise RuntimeError(
                "Length of source_terms should be equal to height of the "
                "matrix multiplied by width of the matrix"
            )

        self.height = height
        self.width = width
        self.step_size = step_size
        self.stiffness_matrix = assemble_stiffness_matrix(height, width)
        self.load_vector = source_terms * step_size**2
