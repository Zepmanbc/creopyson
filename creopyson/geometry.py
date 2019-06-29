"""Geometry module."""


def bound_box(client, file_=None):
    """Get the bounding box for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name.
            Defaults is current active model.

    Returns:
        (dict):
            xmin (float): Minimum X-coordinate of model.
            xmax (float): Maximum X-coordinate of model.
            ymin (float): Minimum Y-coordinate of model.
            ymax (float): Maximum Y-coordinate of model
            zmin (float): Minimum Z-coordinate of model.
            zmax (float): Maximum Z-coordinate of model

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("geometry", "bound_box", data)


def get_edges(client, surface_ids, file_=None):
    """Get the list of edges for a model for given surfaces.

    Args:
        client (obj):
            creopyson Client.
        surface_ids (list:int):
            List of surface IDs.
        `file_` (str, optional):
            File name.
            Defaults is current active model

    Returns:
        (list:dict):
            surface_id (int):
                Surface ID.
            traversal (string):
                Traversal type. Valid values: internal, external.
            edglist (list:dict):
                Information about an edge.
                    edgeid (integer):
                        Edge ID.
                    length (float):
                        Edge length.
                    start (list:dict):
                        A 3D coordinate.
                            x (float):
                                X-coordinate.
                            y (float):
                                Y-coordinate.
                            z (float):
                                Z-coordinate.
                    end (list:dict):
                        A 3D coordinate.
                            x (float):
                                X-coordinate.
                            y (float):
                                Y-coordinate.
                            z (float):
                                Z-coordinate.

    """
    data = {"surface_ids": surface_ids}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("geometry", "get_edges", data, "contourlist")


def get_surfaces(client, file_=None):
    """Get the list of surfaces for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name.
            Defaults is current active model

    Returns:
        (list:dict):
            surface_id (int):
                Surface ID.
            area (float):
                Surface area
            min_extent (list:dict):
                A 3D coordinate.
                    x (float):
                        X-coordinate.
                    y (float):
                        Y-coordinate.
                    z (float):
                        Z-coordinate.
            max_extent (list:dict):
                A 3D coordinate.
                    x (float):
                        X-coordinate.
                    y (float):
                        Y-coordinate.
                    z (float):
                        Z-coordinate.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post(
        "geometry", "get_surfaces", data, "contourlist")
