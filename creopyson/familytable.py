"""Familytable module."""

from .core import creoson_post


def add_inst(client, instance, current_file=None):
    """Add a new instance to a family table.

    Creates a family table if one does not exist.

    Args:
        client (obj):
            creopyson Client.
        instance (string):
            New instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "familytable",
        "function": "add_inst",
        "data": {
            "instance": instance
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def create_inst(client, instance, current_file=None):
    """Create a new model from a family table row.

    Args:
        client (obj):
            creopyson Client.
        instance (string):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): New model name.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "familytable",
        "function": "create_inst",
        "data": {
            "instance": instance
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["name"]
    else:
        raise Warning(data)


def delete_inst(client, instance, current_file=None):
    """Delete an instance from a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (string):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "familytable",
        "function": "delete_inst",
        "data": {
            "instance": instance
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete(client, current_file=None):
    """Delete an entire family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name (wildcards allowed: True).
            Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "familytable",
        "function": "delete",
        "data": {}
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def exists(client, instance, current_file=None):
    """Check whether an instance exists in a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (string):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean):
            Whether the instance exists in the model's family table;
            returns false if there is no family table in the model.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "familytable",
        "function": "exists",
        "data": {
            "instance": instance
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]
    else:
        raise Warning(data)


def get_cell():
    pass


def get_header():
    pass


def get_parents():
    pass


def get_row():
    pass


def list_():
    pass


def list_tree():
    pass


def replace():
    pass


def set_cell():
    pass

