def natural_dissipation(surface_temp):
    """
    Heat flux as a result of natural convection.
    surface_temp in units of degrees celcius.
    """
    return 1.31 * (surface_temp - 20) ** (4 / 3)


def forced_dissipation(surface_temp, ambient_temp, wind_speed):
    """Heat dissipation rate as a result of forced convection."""
    return (11.4 + 5.7 * wind_speed) * (surface_temp - ambient_temp)
