# %%
"""File that contains all the key results of the investigation."""
import numpy as np
import src.system as sys
import src.errors as errors

# %% Task 3: Microprocessor + Ceramic Case, Natural Convection
system = sys.MicroprocessorSystem(2)

STEP_SIZE = 0.001
INITIAL_TEMP = 4200
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)

temp1 = system.mean_temp
print(temp1)

# Half the step size
STEP_SIZE = 0.0005
INITIAL_TEMP = 5300
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% Task 4: Microprocessor + Ceramic Case + Heat Sink, Natural Convection.
# Varying the number of fins with constant separation (2 mm), thickness (1 mm) and
# height (30 mm)


# 10 fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 28e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 450
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 450
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)
# %% 12 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 34e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 350
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 550
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average temperature for 12 fins:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 14 Fins

SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 300
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 500
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 16 Fins

SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 46e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 200
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 400
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 18 Fins

SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 52e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 200
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 400
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 20 Fins

SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 58e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 200
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 400
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% Changing fin height for 14 fins at a constant thickness (1 mm) and separation
# (2 mm)

# No fins (0 mm height)

SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 0

STEP_SIZE = 0.001
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 15 mm
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 15e-3

STEP_SIZE = 0.001
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 30 mm
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 45 mm
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 45e-3

STEP_SIZE = 0.001
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 60 mm
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 60e-3

STEP_SIZE = 0.001
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% Varying separation
# 1 mm separation
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 30e-3

BASE_WIDTH = 27e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 3 mm separation
SEPARATION = 3e-3
WIDTH = 1e-3
HEIGHT = 30e-3

BASE_WIDTH = 53e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 4 mm separation
SEPARATION = 4e-3
WIDTH = 1e-3
HEIGHT = 30e-3

STEP_SIZE = 0.001
BASE_WIDTH = 66e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 5 mm separation

SEPARATION = 5e-3
WIDTH = 1e-3
HEIGHT = 30e-3
STEP_SIZE = 0.001
BASE_WIDTH = 79e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 6 mm separation

SEPARATION = 6e-3
WIDTH = 1e-3
HEIGHT = 30e-3
STEP_SIZE = 0.001
BASE_WIDTH = 92e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 7 mm separation

SEPARATION = 7e-3
WIDTH = 1e-3
HEIGHT = 30e-3
STEP_SIZE = 0.001
BASE_WIDTH = 105e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.001  # h
INITIAL_TEMP = 150
STOPPING_CONDITION = 1e-7
MAX_ITERS = 1000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.0005  # h/2
INITIAL_TEMP = 350
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% Forced Convection

# 14 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3
BASE_WIDTH = 40e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 18 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3
BASE_WIDTH = 52e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 22 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3
BASE_WIDTH = 64e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 26 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3
BASE_WIDTH = 76e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 30 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3
BASE_WIDTH = 88e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 34 Fins
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 30e-3
BASE_WIDTH = 100e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 22 Fins and 45 mm fin height
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 45e-3
BASE_WIDTH = 64e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)
# %% 30 Fins and 45 mm fin height
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 45e-3
BASE_WIDTH = 88e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 30 Fins and 60 mm fin height
SEPARATION = 2e-3
WIDTH = 1e-3
HEIGHT = 60e-3
BASE_WIDTH = 88e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 30 Fins and 60 mm fin height, 1mm fin separation

SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 60e-3
BASE_WIDTH = 87e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% Same height and width to attempt to optimise heat dissipation while keeping
# footprint minimal.
# 14 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 27e-3
BASE_WIDTH = 27e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 18 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 35e-3
BASE_WIDTH = 35e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 22 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 43e-3
BASE_WIDTH = 43e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)
# %% 25 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 49e-3
BASE_WIDTH = 49e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 24 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 47e-3
BASE_WIDTH = 47e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %% 25 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 49e-3
BASE_WIDTH = 49e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)


# %% 30 Fins
SEPARATION = 1e-3
WIDTH = 1e-3
HEIGHT = 59e-3
BASE_WIDTH = 59e-3
system = sys.MicroprocessorSystem(
    3, base_width=BASE_WIDTH, fin_height=HEIGHT, fin_width=WIDTH, fin_spacing=SEPARATION
)
system.plot()

STEP_SIZE = 0.0005  # h
INITIAL_TEMP = 40
STOPPING_CONDITION = 1e-7
MAX_ITERS = 10000000

system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp1 = system.mean_temp
print(temp1)

STEP_SIZE = 0.00025  # h/2
INITIAL_TEMP = 40
system.solve_system(INITIAL_TEMP, STEP_SIZE, STOPPING_CONDITION, MAX_ITERS, forced=True)
temp2 = system.mean_temp
print(temp2)

# Richardson extrapolation
print("Average Temperature:")
print(errors.extrapolate(temp1, temp2))
print("Uncertainty:")
print(temp2 - temp1)

# %%
