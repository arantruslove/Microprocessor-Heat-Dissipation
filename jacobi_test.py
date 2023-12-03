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
# %% Single iteration of test case 1

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
MAX_ITERATIONS = 100000

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

# %% Test Case 2 for a single iteration
HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 6
x_dir_bcs = np.array([0, 4, 8, 12, 16, 20, 24, 28, 32, 36])
y_dir_bcs = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-10
MAX_ITERATIONS = 10000

prev_iteration = np.full((WIDTH, HEIGHT), 0)


for i in range(100):
    prev_iteration = jc.jacobi_poisson_iteration(
        prev_iteration,
        SOURCE_TERM,
        x_dir_bcs,
        x_dir_bcs,
        y_dir_bcs,
        y_dir_bcs,
        STEP_WIDTH,
    )

iteration = prev_iteration

iteration_2d = iteration.reshape((WIDTH, HEIGHT))

# Create the DataFrame from the 2D array
# Here, you can define your own row and column labels if needed
df_iteration = pd.DataFrame(
    iteration_2d, columns=np.arange(WIDTH), index=np.arange(HEIGHT)
)

print(df_iteration)

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

HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 0
left_bcs = np.full(HEIGHT, 0)
right_bcs = np.full(HEIGHT, 18)
bottom_bcs = np.full(WIDTH, 0)
top_bcs = np.full(WIDTH, -18)
T_GUESS = 0
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-10
MAX_ITERATIONS = 1000000

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

solutions = np.flip(solutions, axis=1)

# %% Test Case 3 for a single iteration
HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 0
left_bcs = np.full(HEIGHT, 0)
right_bcs = np.full(HEIGHT, 18)
bottom_bcs = np.full(WIDTH, 0)
top_bcs = np.full(WIDTH, -18)
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-10
MAX_ITERATIONS = 10000

prev_iteration = np.full((WIDTH, HEIGHT), 0)


for i in range(1):
    prev_iteration = jc.jacobi_poisson_iteration(
        prev_iteration,
        SOURCE_TERM,
        bcs,
        bcs,
        -bcs,
        -bcs,
        STEP_WIDTH,
    )

iteration = prev_iteration


# %% Testing a single iteration of a 10x10 grid to see if it is working as expected

HEIGHT = 10
WIDTH = 10
SOURCE_TERM = 0
left_bcs = np.full(HEIGHT, 2)
right_bcs = np.full(HEIGHT, 2)
bottom_bcs = np.full(WIDTH, 3)
top_bcs = np.full(WIDTH, 3)
STEP_WIDTH = 1
STOPPING_CONDITION = 1e-10
MAX_ITERATIONS = 10000

prev_iteration = np.full((WIDTH, HEIGHT), 1)

iteration = jc.jacobi_poisson_iteration(
    prev_iteration,
    SOURCE_TERM,
    left_bcs,
    right_bcs,
    bottom_bcs,
    top_bcs,
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
STEP_WIDTH = 2e-4  # in m
SOURCE_TERM = -5e8 / 150
T_A = 20
T_GUESS = 7000

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
    5e-8,
    1000,
    jc.natural_bcs,
)

print(temperatures)

# %%
