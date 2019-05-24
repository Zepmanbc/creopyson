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


def create_instance(client, instance, current_file=None):
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
        "function": "add_inst",
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


def create_inst():
    pass


def delete_inst():
    pass


def delete():
    pass


def exists():
    pass


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

