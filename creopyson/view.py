"""View module."""


def activate(client, name, current_file=None):
    """Activate a model view.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            View name.
        current_file (str, optional):
            Model name. Defaults is current active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "view",
        "function": "activate",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = client.creoson_post(request)
    if status:
        raise Warning(data)


def list_exploded(client, current_file=None, name=None):
    """List views that match criteria and are exploded.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            View name (wildcards allowed: True).
            Defaults is None: all views are listed.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str): List of view names.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "view",
        "function": "list_exploded",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = client.creoson_post(request)
    if not status:
        return data["viewlist"]
    else:
        raise Warning(data)


def list_(client, current_file=None, name=None):
    """List views that match criteria.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            View name (wildcards allowed: True).
            Defaults is None: all views are listed.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str): List of view names.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "view",
        "function": "list",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = client.creoson_post(request)
    if not status:
        return data["viewlist"]
    else:
        raise Warning(data)
    # TODO: group with list_exploded?


def save(client, name, current_file=None):
    """Save a model's current orientation as a new view.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            View name.
        current_file (str, optional):
            Model name. Defaults is current active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "view",
        "function": "save",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = client.creoson_post(request)
    if status:
        raise Warning(data)
