"""Objects Module."""


def jlpoint(x, y, z):
    """Return a 3D coordinate dict.

    Args:
        x (float):
            X-coordinate.
        y (float):
            Y-coordinate.
        z (float):
            Z-coordinate.

    Returns:
        (dict): 3D coordinate object.

    """
    try:
        x, y, z = float(x), float(y), float(z)
    except ValueError:
        raise Warning("Coordonates must be numbers")
    return {
        "x": x,
        "y": y,
        "z": z
    }
