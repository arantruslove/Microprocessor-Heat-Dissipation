# %% Modules
import numpy as np
import scipy as sp
import pandas as pd
import src.heat_equations as he
import src.jacobi as jc

"""Testing the Jacobi module."""

# %% Test Case 1
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

# %% Solving Test Case 1
HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 0
left_bcs = np.full(HEIGHT, 2)
right_bcs = np.full(HEIGHT, 2)
bottom_bcs = np.full(HEIGHT, 3)
top_bcs = np.full(HEIGHT, 3)
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-15
MAX_ITERATIONS = 100000
T_GUESS = 25

solutions = jc.jacobi_poisson_solve(
    HEIGHT,
    WIDTH,
    SOURCE_TERM,
    left_bcs,
    right_bcs,
    bottom_bcs,
    top_bcs,
    T_GUESS,
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

# %% Test Case 2
# Define the dimensions of the DataFrame
width = 10  # Width of the grid
height = 10  # Height of the grid

# Create a grid of x and y values
x_values = np.arange(0, width)
y_values = np.arange(height - 1, -1, -1)
X, Y = np.meshgrid(x_values, y_values, indexing="xy")

# Evaluate the function u(x, y) = 2x^2 + y^2 + 5
U = 2 * X**2 + Y**2 + 5

# Create the DataFrame
df = pd.DataFrame(U, columns=y_values)
# %% Solving Test Case 2

HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 6
left_bcs = np.full(HEIGHT, 0)
right_bcs = np.full(HEIGHT, 18)
bottom_bcs = np.full(WIDTH, 0)
top_bcs = np.full(WIDTH, 36)
T_GUESS = 0
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-10
MAX_ITERATIONS = 0

solutions = jc.jacobi_poisson_solve(
    HEIGHT,
    WIDTH,
    SOURCE_TERM,
    left_bcs,
    right_bcs,
    bottom_bcs,
    top_bcs,
    T_GUESS,
    STEP_WIDTH,
    STOPPING_CONDITION,
    MAX_ITERATIONS,
)

offset = 5 - solutions[0][0]
solutions += offset

solutions = np.flip(solutions, axis=0)


# %% Test Case 3
# Define the dimensions of the DataFrame
width = 10  # Width of the grid
height = 10  # Height of the grid

# Create a grid of x and y values
x_values = np.arange(0, width)
y_values = np.arange(height - 1, -1, -1)
X, Y = np.meshgrid(x_values, y_values, indexing="xy")

# Evaluate the function u(x, y) = 2x^2 + y^2 + 5
U = X**2 - Y**2 + 5

# Create the DataFrame
df = pd.DataFrame(U, columns=y_values, index=x_values)

# Visualize the DataFrame
print(df)
# %% Solving Test Case 3

# %% Testing the Jacobi method Poisson equation solver

THERMAL_CONDUCTIVITY = 150
HEIGHT = 1e-3  # in m
WIDTH = 14e-3  # in m
STEP_WIDTH = 2e-4  # in m
SOURCE_TERM = -5e6 / 150
T_A = 20
T_GUESS = 253

mesh_height = round(HEIGHT / STEP_WIDTH)
mesh_width = round(WIDTH / STEP_WIDTH)

grad = he.natural_dissipation(T_GUESS, T_A) / THERMAL_CONDUCTIVITY

left_bc = np.full(mesh_height, grad)
right_bc = np.full(mesh_height, -grad)
bottom_bc = np.full(mesh_width, grad)
top_bc = np.full(mesh_width, -grad)

temperatures = jc.jacobi_poisson_solve(
    mesh_height,
    mesh_width,
    SOURCE_TERM,
    left_bc,
    right_bc,
    bottom_bc,
    top_bc,
    T_GUESS,
    STEP_WIDTH,
    1e-15,
    10000,
    jc.natural_bcs,
)

print(temperatures)
