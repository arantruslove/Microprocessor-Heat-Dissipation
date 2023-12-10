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

    plt.ylabel(r"Temperature ($^\circ$C)", fontsize=16)
    plt.xlabel(xlabel, fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.legend(loc="upper right", fontsize=16)

    plt.grid(True, linestyle="--", linewidth=0.5, color="grey")
    plt.show()


# %%
xdata = [1, 2, 3, 4, 5]
ydata = [5, 4, 3, 2, 1]
y_errors = [1, 1, 1, 1, 1]

plot(xdata, ydata, y_errors, "Number of fins")

# %%
