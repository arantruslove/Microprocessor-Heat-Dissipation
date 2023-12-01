import numpy as np
from . import jacobi as jc
import scipy as sp
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve


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

    def apply_neumann(self, boundary_values, side):
        """Applies Neumann boundary conditions to an edge."""
        if side == "left":
            if len(boundary_values) != self.height:
                raise RuntimeError(
                    "Size of boundary values must match the height of the region."
                )

            # Modify the stiffness matrix
            for i in range(self.height):
                self.stiffness_matrix[i][i + self.height] += 1

            # Modify the load vector
            for i in range(self.height):
                self.load_vector[i] += 2 * self.step_size * boundary_values[i]

        elif side == "right":
            if len(boundary_values) != self.height:
                raise RuntimeError(
                    "Size of boundary values must match the height of the region."
                )

            for i in range(
                len(self.stiffness_matrix) - 1,
                len(self.stiffness_matrix) - self.height - 1,
                -1,
            ):
                self.stiffness_matrix[i][i - self.height] += 1

            for i in range(self.height):
                self.load_vector[len(self.load_vector) - 1 - i] -= (
                    2 * self.step_size * boundary_values[i]
                )

        elif side == "bottom":
            if len(boundary_values) != self.width:
                raise RuntimeError(
                    "Size of boundary values must match the width of the region."
                )

            for i in range(0, len(self.stiffness_matrix), self.height):
                self.stiffness_matrix[i][i + 1] += 1

            vector_pos = 0
            for i in range(self.width):
                self.load_vector[vector_pos] += 2 * self.step_size * boundary_values[i]
                vector_pos += self.height

        elif side == "top":
            if len(boundary_values) != self.width:
                raise RuntimeError(
                    "Size of boundary values must match the width of the region."
                )

            for i in range(len(self.stiffness_matrix) - 1, 0, -self.height):
                self.stiffness_matrix[i][i - 1] += 1

            vector_pos = self.height - 1
            for i in range(self.width):
                self.load_vector[vector_pos] -= 2 * self.step_size * boundary_values[i]
                vector_pos += self.height

    def solve_system_jacobi(self, stopping_condition, max_iterations):
        """Solves the system of linear equations using the Jacobi method."""
        solutions = jc.jacobi_method(
            self.stiffness_matrix, self.load_vector, stopping_condition, max_iterations
        )

        return solutions

    def auto_solve(self):
        """
        Solves the matrix equations using scipy functions (not allowed for report
        results but used for comparison).
        """
        A = csr_matrix(self.stiffness_matrix)
        b = self.load_vector

        return spsolve(A, b)
