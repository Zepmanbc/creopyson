"""Name module."""

from .core import creoson_post


def copy(client, name, to_name, current_file=None, to_file=None):
    """Copy dimension to another in the same model or another model.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Dimension name to copy.
        to_name (str):
            Destination dimension; th dimension must already exist.
        current_file (str, optional):
            Model name. Defaults is current active model.
        to_file (str, optional):
            Destination model. Defaults is the source model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "copy",
        "data": {
            "name": name,
            "to_name": to_name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if to_file:
        request["data"]["to_file"] = to_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


# def list_():
#     pass


# def list_detail():
#     pass


def set_(client, name, value, current_file=None):
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "set",
        "data": {
            "name": name,
            "value": value,
            "encoded": False
        }
    }
    if current_file:
        request["data"]["file"] = current_file
        requests.post(client.server, data=json.dumps(request))


# def show():
#     pass


# def user_select():
#     pass
