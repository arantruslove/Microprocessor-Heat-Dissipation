# %% Initialisation
import cProfile
import numpy as np
import src.system as sys

# %% Testing the plotting capabilities
step_size = 0.0005
base_width = 16e-3
fin_height = 30e-3
fin_width = 1e-3
fin_spacing = 2e-3
basic_sys = sys.MicroprocessorSystem(
    2,
    base_width=base_width,
    fin_height=fin_height,
    fin_width=fin_width,
    fin_spacing=fin_spacing,
)
basic_sys.plot(step_size=step_size)
cProfile.run("basic_sys.solve_system(2500, step_size, 1e-7, 100000)", "profile_out")

# %%
print(basic_sys.average_processor_temp(step_size))
basic_sys.contour()

# %% Testing the example meshes
operation_mask, power_mask, conductivity_mask = basic_sys.example_masks(step_size)


# %% Profiling the operation
basic_sys = sys.MicroprocessorSystem(2)
cProfile.run("basic_sys.solve_system(3333, 0.0001, 1e-9, 10000)", "profile_out")

# %%
import pstats

p = pstats.Stats("profile_out")
p.sort_stats("cumulative").print_stats(30)
