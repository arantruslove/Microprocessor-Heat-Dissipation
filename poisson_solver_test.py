# %%
import numpy as np
import src.poisson_solver as ps

"""Testing the Poisson Solver module."""

# %% Testing the initialisation of the stiffness matrix with the PoissonSolver class

height = 5
width = 2
step_size = 0.1
source_terms = np.array([1, 2, 3, 4])

poisson_system = ps.PoissonSolver(height, width, step_size, source_terms)

print(poisson_system.stiffness_matrix)

# %%
