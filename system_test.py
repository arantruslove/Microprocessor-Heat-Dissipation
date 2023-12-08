# %% Initialisation
import cProfile
import numpy as np
import src.system as sys

# %% Testing the plotting capabilities
step_size = 0.001
base_width = 34e-3
fin_height = 30e-3
fin_width = 1e-3
fin_spacing = 2e-3
basic_sys = sys.MicroprocessorSystem(
    1,
    base_width=base_width,
    fin_height=fin_height,
    fin_width=fin_width,
    fin_spacing=fin_spacing,
)
basic_sys.plot(step_size=step_size)

basic_sys.solve_system(30, step_size, 1e-6, 0)


# %% Testing the example meshes
operation_mask, power_mask, conductivity_mask = basic_sys.example_masks(step_size)

# %% Testing the Jacobi Poisson solver
step_size = 0.0005
base_width = 10e-3
fin_height = 30e-3
fin_width = 1e-3
fin_spacing = 2e-3

basic_sys = sys.MicroprocessorSystem(
    3,
    base_width=base_width,
    fin_height=fin_height,
    fin_width=fin_width,
    fin_spacing=fin_spacing,
)

# Plotting
basic_sys.plot(step_size=step_size)

# Solving
basic_sys.solve_system(100, step_size, 1e-7, 1000000, forced=True)
average_temp = basic_sys.average_processor_temp(step_size)
print(average_temp)


# %% Profiling the operation
basic_sys = sys.MicroprocessorSystem(2)
cProfile.run("basic_sys.solve_system(3333, 0.0001, 1e-9, 10000)", "profile_out")

# %%
import pstats

p = pstats.Stats("profile_out")
p.sort_stats("cumulative").print_stats(30)
