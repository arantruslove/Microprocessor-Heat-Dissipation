# %%
import numpy as np

import src.poisson_solver as ps
import src.heat_equations as he

"""Testing the Poisson Solver module."""

# %% Testing the initialisation of the stiffness matrix with the PoissonSolver class

height = 3
width = 3
step_size = 1
source_terms = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])

poisson_system = ps.PoissonSolver(height, width, step_size, source_terms)
print(poisson_system.stiffness_matrix)

# %% Applying Nuemann boundary conditions

boundary_gradients = np.array([1, 1, 1])

poisson_system.apply_neumann(boundary_gradients, "left")
poisson_system.apply_neumann(boundary_gradients, "right")
poisson_system.apply_neumann(boundary_gradients, "bottom")
poisson_system.apply_neumann(boundary_gradients, "top")

print(poisson_system.stiffness_matrix)
print(poisson_system.load_vector)

# %% Testing the physical situation of just the microprocessor suspended in air

# Constants
PROCESSOR_HEIGHT = 0.001  # In m
PROCESSOR_WIDTH = 0.014  # In m
STEP_SIZE = 0.0002  # In m
SURFACE_TEMP = 20  # In degrees Celsius
AMBIENT_TEMP = 20  # In degrees Celsius
THERMAL_CONDUCTIVITY = 150  # W/mK
THERMAL_OUTPUT = 5e8  # W/m^3

source_term = -THERMAL_OUTPUT / THERMAL_CONDUCTIVITY  # -q/k
boundary_gradient = (
    -he.natural_dissipation(SURFACE_TEMP, AMBIENT_TEMP) / THERMAL_CONDUCTIVITY
)

matrix_height = round(PROCESSOR_HEIGHT / STEP_SIZE)
matrix_width = round(PROCESSOR_WIDTH / STEP_SIZE)

source_terms = [source_term] * (matrix_height * matrix_width)
# Assuming PoissonSolver is a class you have defined in Python
poisson_system = ps.PoissonSolver(
    matrix_height, matrix_width, STEP_SIZE, np.array(source_terms)
)

print(f"Matrix Height: {matrix_height}")
print(f"Matrix Width: {matrix_width}")

# Applying boundary conditions
horizontal_boundary = [boundary_gradient] * matrix_width
poisson_system.apply_neumann(horizontal_boundary, "bottom")
poisson_system.apply_neumann(horizontal_boundary, "top")

vertical_boundary = [boundary_gradient] * matrix_height
poisson_system.apply_neumann(vertical_boundary, "left")
poisson_system.apply_neumann(vertical_boundary, "right")

# Solving the system with LU decomposition
# Assuming solveSystemJacobi is a method you've defined
temperatures = poisson_system.solve_system_jacobi(1e-5, 100000)
# temperatures = poisson_system.auto_solve()
print(temperatures)
print("Finished")

# %%
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_array = np.zeros_like(array)
print(new_array)

# %%
