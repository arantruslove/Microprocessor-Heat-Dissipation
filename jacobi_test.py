# %%
import numpy as np
import scipy as sp
import pandas as pd
import src.heat_equations as he
import src.jacobi as jc

"""Testing the Jacobi module."""

# %% Sanity check
# Define the dimensions of the DataFrame
width = 10  # Width of the grid
height = 10  # Height of the gri

# Create a grid of x and y values
x_values = np.arange(0, width)
y_values = np.arange(0, height)
X, Y = np.meshgrid(x_values, y_values, indexing="ij")

# Evaluate the function u(x, y) = 2x + 3y + 5
U = 2 * X + 3 * Y + 5

# Create the DataFrame
df = pd.DataFrame(U, columns=y_values, index=x_values)

# Visualize the DataFrame
print(df)

# %% Solving the above with my functions

HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 0
LEFT_BC = 2
RIGHT_BC = 2
BOTTOM_BC = 3
TOP_BC = 3
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-15
MAX_ITERATIONS = 10000

solutions = jc.jacobi_poisson_solve(
    HEIGHT,
    WIDTH,
    SOURCE_TERM,
    LEFT_BC,
    RIGHT_BC,
    BOTTOM_BC,
    TOP_BC,
    STEP_WIDTH,
    STOPPING_CONDITION,
    MAX_ITERATIONS,
)

offset = 5 - solutions[0][0]
solutions += offset

solutions_2d = solutions.reshape((10, 10))

# Create the DataFrame from the 2D array
# Here, you can define your own row and column labels if needed
df_solutions = pd.DataFrame(solutions_2d, columns=np.arange(10), index=np.arange(10))

print(df_solutions)
# %% Testing a single iteration of a 10x10 grid to see if it is working as expected

HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 0
LEFT_BC = 2
RIGHT_BC = 2
BOTTOM_BC = 3
TOP_BC = 3
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-10
MAX_ITERATIONS = 10000

prev_iteration = np.full((WIDTH, HEIGHT), 1)

iteration = jc.jacobi_poisson_iteration(
    prev_iteration,
    SOURCE_TERM,
    LEFT_BC,
    RIGHT_BC,
    BOTTOM_BC,
    TOP_BC,
    STEP_WIDTH,
)
iteration_2d = iteration.reshape((WIDTH, HEIGHT))

# Create the DataFrame from the 2D array
# Here, you can define your own row and column labels if needed
df_iteration = pd.DataFrame(
    iteration_2d, columns=np.arange(WIDTH), index=np.arange(HEIGHT)
)

print(df_iteration)

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
