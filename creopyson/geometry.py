"""Name module."""

from .core import creoson_post


def bound_box(client, current_file=None):
    """Get the bounding box for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name.
            Defaults is current active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            xmin (float): Minimum X-coordinate of model.
            xmax (float): Maximum X-coordinate of model.
            ymin (float): Minimum Y-coordinate of model.
            ymax (float): Maximum Y-coordinate of model
            zmin (float): Minimum Z-coordinate of model.
            zmax (float): Maximum Z-coordinate of model

    """
    request = {
        "sessionId": client.sessionId,
        "command": "geometry",
        "function": "bound_box",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


# def get_edges():
#     pass


# def get_surfaces():
#     pass
