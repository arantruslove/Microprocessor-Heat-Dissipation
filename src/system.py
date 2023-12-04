"""Contains classes that correspond to the different objects and their properties."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


class Object:
    def __init__(
        self,
        bottom_left: tuple,
        width,
        height,
        thermal_conductivity,
        thermal_output,
        colour="grey",
    ):
        """
        Initialising the object with its defining proprties.
        - width: in m
        - height in m
        - bottom_left: absolute coordinate of the bottom left of the object in m
        - thermal_conductivity in W/mK
        - thermal_output in W/m^3
        """
        self.width = width
        self.height = height
        self.bl = bottom_left
        self.k = thermal_conductivity
        self.power = thermal_output
        self.colour = colour


class MicroprocessorSystem:
    def __init__(self, scenario: int):
        if scenario > 3:
            raise RuntimeError("There are only 4 physical scenarios")

        if scenario == 1:
            """Microprocessor alone."""
            processor = Object((0, 0), 14e-3, 1e-3, 150, 5e8, colour="orange")
            self.objects = [processor]

        if scenario == 2:
            """Microprocessor and ceramic case."""
            processor = Object((0, 0), 14e-3, 1e-3, 150, 5e8, colour="orange")
            ceramic_case = Object((-3e-3, 1e-3), 20e-3, 2e-3, 230, 0, colour="grey")
            self.objects = [processor, ceramic_case]

        if scenario == 3:
            """Microprocessor, ceramic case and heat sink."""
            processor = Object((0, 0), 14e-3, 1e-3, 150, 5e8, colour="orange")
            ceramic_case = Object((-3e-3, 1e-3), 20e-3, 2e-3, 230, 0, colour="grey")

    def plot(self, step_size=None):
        """
        Plots the grid with the optional argument of providing a step size which
        plots the position of the mesh points using lines instead of scatter points.
        """
        fig, ax = plt.subplots()
        max_width = 0
        max_height = 0

        # Find the maximum width and height to set the plot limits
        for obj in self.objects:
            if obj.bl[0] + obj.width > max_width:
                max_width = obj.bl[0] + obj.width
            if obj.bl[1] + obj.height > max_height:
                max_height = obj.bl[1] + obj.height

        # Determine the minimum bounds to cover the negative direction
        min_width = min(obj.bl[0] for obj in self.objects)
        min_height = min(obj.bl[1] for obj in self.objects)

        # Set plot limits based on the objects and grid
        ax.set_xlim(min_width - 0.001, max_width + 0.001)
        ax.set_ylim(min_height - 0.001, max_height + 0.001)

        # Define the grid range and spacing
        if step_size:
            # Define the grid lines
            grid_x = np.arange(min_width, max_width + step_size, step_size)
            grid_y = np.arange(min_height, max_height + step_size, step_size)

            # Draw grid lines instead of scatter
            ax.vlines(
                grid_x,
                min_height - step_size,
                max_height + step_size,
                colors="red",
                linestyles="solid",
                linewidth=0.5,
                zorder=1,
            )
            ax.hlines(
                grid_y,
                min_width - step_size,
                max_width + step_size,
                colors="red",
                linestyles="solid",
                linewidth=0.5,
                zorder=1,
            )

        # Set the aspect ratio to equal to maintain the scale of the plot
        ax.set_aspect("equal", adjustable="box")

        ax.set_title("Microprocessor System")
        ax.set_xlabel("Width (m)")
        ax.set_ylabel("Height (m)")

        for obj in self.objects:
            # Create a rectangle patch with a semi-transparent color and add it to the
            # plot
            rect = patches.Rectangle(
                obj.bl,
                obj.width,
                obj.height,
                linewidth=1,
                edgecolor=obj.colour,
                facecolor=obj.colour,
                alpha=0.5,
                zorder=2,  # Ensure the objects are plotted above the grid
            )
            ax.add_patch(rect)

        plt.show()
