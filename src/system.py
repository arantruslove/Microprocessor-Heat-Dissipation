"""Contains classes that correspond to the different objects and their properties."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


# Functions
def determine_extremes(objects):
    "Determines the global extreme values from a system of objects."
    xmin, xmax, ymin, ymax = (
        objects[0].xmin,
        objects[0].xmax,
        objects[0].ymin,
        objects[0].ymax,
    )

    for obj in objects:
        if obj.xmin < xmin:
            xmin = obj.xmin
        if obj.xmax > xmax:
            xmax = obj.xmax
        if obj.ymin < ymin:
            ymin = obj.ymin
        if obj.ymax > ymax:
            ymax = obj.ymax

    return xmin, xmax, ymin, ymax


def all_object_bnds(objects, step_size: float) -> list[dict]:
    """
    Converts between distance bounds to indices of all the objects in the list.
    - xmin
    - xmax
    - ymin
    - ymax
    """
    xmin, xmax, ymin, ymax = determine_extremes(objects)
    origin = (xmin, ymin)
    all_bounds = []
    for obj in objects:
        extremes = {}
        extremes["xmin"] = round((obj.xmin - origin[0]) / step_size)
        extremes["xmax"] = round((obj.xmax - origin[0]) / step_size)
        extremes["ymin"] = round((obj.ymin - origin[1]) / step_size)
        extremes["ymax"] = round((obj.ymax - origin[1]) / step_size)
        all_bounds.append(extremes)
    return all_bounds


def create_mesh(objects, step_size):
    """Generates a mesh of zeros that overlays the complete system of objects."""

    xmin, xmax, ymin, ymax = determine_extremes(objects)
    x_values = np.arange(xmin, xmax + step_size, step_size)
    y_values = np.arange(ymin, ymax + step_size, step_size)
    width = x_values.size
    height = y_values.size
    return np.zeros((width, height))


def add_operation_numbers(binary_mesh: np.ndarray) -> np.ndarray:
    """
    Converts a binary mesh representing the shape of the system to a mesh that
    contains different numbers based on which type of operation should be carried out.
    Operation table:

    0: No operation (air)
    1: Interior point
    2: Left boundary
    3: Right boundary
    4: Bottom boundary
    5: Top boundary
    6: Bottom-left corner
    7: Bottom-right corner
    8: Top-left corner
    9: Top-right corner
    """
    operation_mesh = binary_mesh.copy()
    width = len(operation_mesh)
    height = len(operation_mesh[0])

    for i in range(len(operation_mesh)):
        for j in range(len(operation_mesh[0])):
            if operation_mesh[i][j] == 1:
                # Boundary checks
                is_left = i == 0
                is_right = i == width - 1
                is_bottom = j == 0
                is_top = j == height - 1

                if i != 0:
                    is_left = operation_mesh[i - 1][j] == 0
                if i != width - 1:
                    is_right = operation_mesh[i + 1][j] == 0
                if j != 0:
                    is_bottom = operation_mesh[i][j - 1] == 0
                if j != height - 1:
                    is_top = operation_mesh[i][j + 1] == 0

                # Bottom-left corner
                if is_bottom and is_left:
                    operation_mesh[i][j] = 6

                # Bottom-right corner
                elif is_bottom and is_right:
                    operation_mesh[i][j] = 7

                # Top-left corner
                elif is_top and is_left:
                    operation_mesh[i][j] = 8

                # Top-right corner
                elif is_top and is_right:
                    operation_mesh[i][j] = 9

                # Left boundary
                elif is_left:
                    operation_mesh[i][j] = 2

                # Right boundary
                elif is_right:
                    operation_mesh[i][j] = 3

                # Bottom boundary
                elif is_bottom:
                    operation_mesh[i][j] = 4

                # Top boundary
                elif is_top:
                    operation_mesh[i][j] = 5

    return operation_mesh


# Classes
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
        self.xmin = bottom_left[0]
        self.xmax = bottom_left[0] + width
        self.ymin = bottom_left[1]
        self.ymax = bottom_left[1] + height
        self.k = thermal_conductivity
        self.power = thermal_output
        self.colour = colour


class MicroprocessorSystem:
    def __init__(self, scenario: int):
        self.temps = [[]]

        if scenario > 3:
            raise RuntimeError("There are only 4 physical scenarios")

        if scenario == 1:
            """Microprocessor alone."""
            processor = Object((0, 0), 14e-3, 1e-3, 150, 5e8, colour="black")
            self.objects = [processor]

        if scenario == 2:
            """Microprocessor and ceramic case."""
            processor = Object((0, 0), 14e-3, 1e-3, 150, 5e8, colour="black")
            ceramic_case = Object((-3e-3, 1e-3), 20e-3, 2e-3, 230, 0, colour="orange")
            self.objects = [processor, ceramic_case]

        if scenario == 3:
            """Microprocessor, ceramic case and heat sink."""
            processor = Object((0, 0), 14e-3, 1e-3, 150, 5e8, colour="black")
            ceramic_case = Object((-3e-3, 1e-3), 20e-3, 2e-3, 230, 0, colour="orange")

    def example_meshes(self, step_size):
        """
        Generates the example meshes that will be used for temperature, thermal output
        and thermal conductivity for the entire system.
        """
        # Initialising meshes
        base = create_mesh(self.objects, step_size)
        binary_mesh = base.copy()  # Binary mask of combined system objects
        power_outputs = base.copy()
        thermal_conductivities = base.copy()

        # Determining bounds
        bounds = all_object_bnds(self.objects, step_size)

        # Populating power outputs and thermal conductivities with values
        for i in range(len(self.objects)):
            xmin = bounds[i]["xmin"]
            xmax = bounds[i]["xmax"]
            ymin = bounds[i]["ymin"]
            ymax = bounds[i]["ymax"]
            binary_mesh[xmin : xmax + 1, ymin : ymax + 1] = 1
            power_outputs[xmin : xmax + 1, ymin : ymax + 1] = self.objects[i].power
            thermal_conductivities[xmin : xmax + 1, ymin : ymax + 1] = self.objects[i].k

        operation_mesh = add_operation_numbers(binary_mesh)

        return (
            np.flipud(operation_mesh.T),
            np.flipud(power_outputs.T),
            np.flipud(thermal_conductivities.T),
        )

    def determine_edges(self, step_size):
        """Determines the edge positions indices of the combined systems."""
        bounds = all_object_bnds(self.objects, step_size)

        edges = []
        for bound in bounds:
            xmin, xmax, ymin, ymax = (
                bound["xmin"],
                bound["xmax"],
                bound["ymin"],
                bound["ymax"],
            )

            left_edge = ((xmin, ymin), (xmin, ymax))
            right_edge = ((xmax, ymin), (xmax, ymax))
            bottom_edge = ((xmin, ymin), (xmax, ymin))
            top_edge = ((xmin, ymax), (xmax, ymax))
            edges += [left_edge, right_edge, bottom_edge, top_edge]

        return edges

    def solve_system(self):
        """
        Solves the Poisson heat equation of the microprocessor system by using the
        Jacobi method.
        """

    def plot(self, step_size=None):
        """
        Plots the grid with the optional argument of providing a step size which
        plots the position of the mesh points using lines instead of scatter points.
        """
        fig, ax = plt.subplots()

        # Assuming determine_extremes is a function that returns the extreme points
        xmin, xmax, ymin, ymax = determine_extremes(self.objects)

        # Set plot limits based on the objects and grid
        ax.set_xlim(xmin - 0.001, xmax + 0.001)
        ax.set_ylim(ymin - 0.001, ymax + 0.001)

        # Define the grid range and spacing
        if step_size:
            # Define the grid lines starting from (xmin, ymin)
            grid_x = np.arange(xmin, xmax + step_size, step_size)
            grid_y = np.arange(ymin, ymax + step_size, step_size)

            # Draw grid lines
            ax.vlines(
                grid_x,
                ymin,
                ymax,
                colors="red",
                linestyles="solid",
                linewidth=0.5,
                zorder=1,
            )
            ax.hlines(
                grid_y,
                xmin,
                xmax,
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
            width = obj.xmax - obj.xmin
            height = obj.ymax - obj.ymin
            rect = patches.Rectangle(
                (obj.xmin, obj.ymin),
                width,
                height,
                linewidth=1,
                edgecolor=obj.colour,
                facecolor=obj.colour,
                alpha=0.5,
                zorder=2,  # Ensure the objects are plotted above the grid
            )
            ax.add_patch(rect)

        plt.show()
