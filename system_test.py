# %% Initialisation
import src.system as sys

# %% Testing the plotting capabilities
basic_sys = sys.MicroprocessorSystem(2)

basic_sys.plot(step_size=0.0002)

mesh = basic_sys.create_mesh(0.0002)

# %%
