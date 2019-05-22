"""Name module."""

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
            Model name (wildcards alloawed: True).
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
            Defaults: All layers will be deleted.
        current_file (str, optional):
            Model name.
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


def list_():
    pass


def show():
    pass
