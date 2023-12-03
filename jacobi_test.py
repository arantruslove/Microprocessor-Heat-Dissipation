# %%
import numpy as np
import scipy as sp
import src.heat_equations as he
import src.jacobi as jc

"""Testing the Jacobi module."""

# %% Testing a single iteration of a 3x3 grid to see if it is working as expected

THERMAL_CONDUCTIVITY = 150
STEP_WIDTH = 1  # in m
SOURCE_TERM = 5e8 / 150
MESH_HEIGHT = 3
MESH_WIDTH = 3
neumann_bc = (
    -he.natural_dissipation(100000, 20) / THERMAL_CONDUCTIVITY  # Gradient at boundary
)
print(neumann_bc)

row = [SOURCE_TERM / 4] * MESH_HEIGHT
solution = np.array([row] * MESH_WIDTH)

result = jc.jacobi_poisson_iteration(solution, SOURCE_TERM, neumann_bc, STEP_WIDTH)

print(result)

# %% Testing the Jacobi method Poisson equation solver

THERMAL_CONDUCTIVITY = 150
HEIGHT = 1e-3  # in m
WIDTH = 14e-3  # in m
STEP_WIDTH = 1e-6  # in m
SOURCE_TERM = 5e8 / 150
T_SURF_0 = 50
T_A = 20

mesh_height = round(HEIGHT / STEP_WIDTH)
mesh_width = round(WIDTH / STEP_WIDTH)

temperatures = jc.jacobi_poisson_solve(
    mesh_height,
    mesh_width,
    SOURCE_TERM,
    T_A,
    T_SURF_0,
    STEP_WIDTH,
    he.natural_dissipation,
    1e-5,
    100000,
)

print(temperatures)

# %%
