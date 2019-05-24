"""Layer module."""

from .core import creoson_post


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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "layer",
        "function": "delete",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean): Whether the layer exists on the model.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "exists",
        "data": {}
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]
    else:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict):
            name (str):
                Layer name.
            status (str): Layer status.
                Valid values: BLANK, DISPLAY, HIDDEN, NORMAL.
            ID (int):
                Layer ID.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "exists",
        "data": {}
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    status, data = creoson_post(client, request)
    if not status:
        return data["layers"]
    else:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "exists",
        "data": {}
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if show_:
        request["data"]["show"] = show_
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)
