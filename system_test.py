# %% Initialisation
import numpy as np
import src.system as sys

# %% Testing the plotting capabilities
step_size = 0.001
basic_sys = sys.MicroprocessorSystem(2)
basic_sys.plot(step_size=step_size)

# %% Testing the example meshes
operation_mask, power_mask, conductivity_mask = basic_sys.example_masks(step_size)

# %% Determining edges of the system

edges = basic_sys.determine_edges(step_size=step_size)
print(edges)

# %%
