"""Note module."""

from .core import creoson_post


def copy(client, name, to_name=None, current_file=None, to_file=None):
    """Copy note to another in the same model or another model.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name to copy (wildcards allowed: True).
        to_name (str):
            Destination note.
            Defaults is the source note name
        current_file (str, optional):
            Model name (wildcards allowed: True).
            Defaults is current active model.
        to_file (str, optional):
            Destination model.
            Defaults is the source model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "note",
        "function": "copy",
        "data": {
            "name": name
        }
    }
    if to_name:
        request["data"]["to_name"] = to_name
    if current_file:
        request["data"]["file"] = current_file
    if to_file:
        request["data"]["to_file"] = to_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete(client, name, current_file=None):
    """Delete a model or drawing note.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name (wildcards allowed: True).
        current_file (str, optional):
            Model name (wildcards allowed: True).
            Defaults is current active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "note",
        "function": "delete",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def exists():
    pass


def get():
    pass


def list_():
    pass


def set_():
    pass

