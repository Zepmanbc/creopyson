"""Layer module."""


def delete(client, name=None, current_file=None):
    """Delete one or more layers.

    Args:
        client (obj):
            creopyson Client.
        name (str, optional):
            Layer name (wildcards allowed: True).
            Defaults: All layers will be deleted.
        current_file (str, optional):
            File name (wildcards alloawed: True).
            Defaults is current active model.

    Returns:
        None

    """
    data = {"name": name}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    return client.creoson_post("layer", "delete", data)


def exists(client, name=None, current_file=None):
    """Check whether layer(s) exists on a model.

    Args:
        client (obj):
            creopyson Client.
        name (str, optional):
            Layer name (wildcards allowed: True).
            Defaults: All layers are listed.
        current_file (str, optional):
            File name.
            Defaults is current active model.

    Returns:
        (boolean): Whether the layer exists on the model.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    return client.creoson_post("layer", "exists", data)["exists"]


def list_(client, name=None, current_file=None):
    """List layers that match criteria.

    Args:
        client (obj):
            creopyson Client.
        name (str, optional):
            Layer name (wildcards allowed: True).
            Defaults: All layers are listed.
        current_file (str, optional):
            File name.
            Defaults is current active model.

    Returns:
        (list:dict):
            name (str):
                Layer name.
            status (str): Layer status.
                Valid values: BLANK, DISPLAY, HIDDEN, NORMAL.
            ID (int):
                Layer ID.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    return client.creoson_post("layer", "list", data)["layers"]


def show(client, name=None, current_file=None, show_=None):
    """how/Hide one or more layers.

    Args:
        client (obj):
            creopyson Client.
        name (str, optional):
            Layer name (wildcards allowed: True).
            Defaults: All layers are listed.
        current_file (str, optional):
            File name (wildcards allowed: True).
            Defaults is current active model.
        `show_` (boolean, optional):
            Whether to show or hide the layers.
            Defaults is True (show).

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if show_:
        data["show"] = show_
    return client.creoson_post("layer", "show", data)
