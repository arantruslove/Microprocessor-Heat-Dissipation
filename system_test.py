# %% Initialisation
import numpy as np
import src.system as sys

# %% Testing the plotting capabilities
step_size = 0.001
basic_sys = sys.MicroprocessorSystem(2)
basic_sys.plot(step_size=step_size)

# %% Testing the determining of bounds based off step size
bounds = basic_sys.determine_bnds(step_size)
print(bounds)

# %% Testing the example meshes
temp_mesh, power_mesh, conductivity_mesh = basic_sys.example_meshes(step_size)

# %%
