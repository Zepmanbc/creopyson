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


def get_edges(client, surface_ids, current_file=None):
    """Get the list of edges for a model for given surfaces.

    Args:
        client (obj):
            creopyson Client.
        surface_ids (list:int):
            List of surface IDs.
        current_file (str, optional):
            File name.
            Defaults is current active model

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict):
        surface_id (int): Surface ID.
        traversal (string): Traversal type. Valid values: internal, external.
        edglist (list:dict): Information about an edge.
            edgeid (integer): Edge ID.
            length (float): Edge length.
            start (list:dict): A 3D coordinate.
                x (float): X-coordinate.
                y (float): Y-coordinate.
                z (float): Z-coordinate.
            end (list:dict): A 3D coordinate.
                x (float): X-coordinate.
                y (float): Y-coordinate.
                z (float): Z-coordinate.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "geometry",
        "function": "get_edges",
        "data": {
            "surface_ids": surface_ids
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["contourlist"]
    else:
        raise Warning(data)


def get_surfaces(client, current_file=None):
    """Get the list of surfaces for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name.
            Defaults is current active model

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict):
            surface_id (int): Surface ID.
            area (float): Surface area
            min_extent (list:dict): A 3D coordinate.
                x (float): X-coordinate.
                y (float): Y-coordinate.
                z (float): Z-coordinate.
            max_extent (list:dict): A 3D coordinate.
                x (float): X-coordinate.
                y (float): Y-coordinate.
                z (float): Z-coordinate.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "geometry",
        "function": "get_surfaces",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["contourlist"]
    else:
        raise Warning(data)
