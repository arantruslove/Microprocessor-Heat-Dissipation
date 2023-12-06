# %% Initialisation
import numpy as np
import src.system as sys

# %% Testing the plotting capabilities
step_size = 0.001
basic_sys = sys.MicroprocessorSystem(1)
basic_sys.plot(step_size=step_size)

# %% Testing the example meshes
operation_mask, power_mask, conductivity_mask = basic_sys.example_masks(step_size)

# %% Determining edges of the system

edges = basic_sys.determine_edges(step_size=step_size)
print(edges)

# %% Testing the Jacobi Poisson solver
basic_sys = sys.MicroprocessorSystem(2)
temps = basic_sys.solve_system(20, 0.0001, 1e-13, 100)
temps_display = np.flipud(temps.T)

# %%
