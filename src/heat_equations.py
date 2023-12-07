def natural_dissipation(surface_temp):
    """
    Heat flux as a result of natural convection.
    surface_temp in units of degrees celcius.
    """
    return 1.31 * (surface_temp - 20) ** (4 / 3)


def forced_dissipation(surface_temp):
    """
    Heat flux as a result of forced convection with a windspeed of 20 degrees
    celcius.
    """
    return 125.4 * (surface_temp - 20)
