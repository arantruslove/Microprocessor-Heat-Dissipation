# %%
import matplotlib.pyplot as plt


def plot(xdata, ydata, y_errors, xlabel, horizontal_line=0):
    """
    Plots a graph of the data points with y error. Option to include a vertical
    dotted line.
    """

    # Adjust the figure size
    plt.figure(figsize=(8, 6))

    # Plotting with error bars
    plt.errorbar(
        xdata,
        ydata,
        yerr=y_errors,
        fmt="o",
        linestyle="None",
        ecolor="orange",
        elinewidth=2,
        capsize=5,
        capthick=2,
        label="Temperature with error bars",
        markersize=10,
    )

    if horizontal_line:
        plt.axhline(
            y=horizontal_line,
            linestyle="dashed",
            color="red",
            label="Maximum acceptable temperature",
        )

    plt.ylabel(r"Temperature ($^\circ$C)", fontsize=16)
    plt.xlabel(xlabel, fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.legend(loc="upper right", fontsize=16)

    plt.grid(True, linestyle="--", linewidth=0.5, color="grey")
    plt.show()


# %% Varying number of fins (natural dissipation)
n_fins = [10, 12, 14, 16, 18, 20]
temps = [800, 700, 650, 600, 550, 520]
errors = [200, 200, 180, 160, 150, 140]

plot(n_fins, temps, errors, "Number of fins")

# %% Varying fin height (natural dissipation)
fin_height = [0, 15, 30, 45, 60]
temps = [3500, 900, 650, 510, 430]
errors = [500, 300, 180, 140, 120]

plot(fin_height, temps, errors, "Fin height (mm)")

# %% Varying separation (natural dissipation)

# All same temperature (with respect to error) except 7 mm separation which was 660
# degrees celcius rather than 650

# %% Equal sink width and fin height

sink_width = [27, 35, 43, 47, 49, 55, 59]
temps = [109, 88, 77, 74, 72, 71, 69]
errors = [15, 11, 9, 8, 7, 6, 6]

plot(
    sink_width, temps, errors, "Heat sink width and fin height (mm)", horizontal_line=80
)

# %%
