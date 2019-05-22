"""Server module."""

from .core import creoson_post


def pwd(client):
    """Return the server's execution directory.

    Args:
        client (obj):
            creopyson Client.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): Full name of working directory.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "server",
        "function": "pwd",
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["dirname"]
    else:
        raise Warning(data)
