"""Parameter module."""

from .core import creoson_post


def copy(
    client,
    name,
    to_name,
    current_file=None,
    to_file=None,
    designate=None
):
    """Copy parameter to another in the same model or another model.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Parameter name to copy (wildcards allowed: True).
        to_name (str):
            Destination parameter.
        current_file (str, optional):
            Model name. Defaults is current active model.
        to_file (str, optional):
            Destination model (wildcards allowed: True).
            Defaults is the source model.
        designate (boolean, optional):
            Set copied parameter to be designated/not designated,
            blank=do not set. Defaults is `blank`.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "copy",
        "data": {
            "name": name,
            "to_name": to_name,
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if to_file:
        request["data"]["to_file"] = to_file
    if designate:
        request["data"]["designate"] = designate
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def delete():
    pass


def exists():
    pass


def list_():
    pass


def set_():
    pass
