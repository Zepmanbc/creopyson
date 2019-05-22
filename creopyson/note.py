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


def exists(client, current_file=None, name=None, names=None):
    """Check whether note(s) exists on a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            Note name; only used if names is not given. Defaults to None.
        names (list:str, optional):
            List of note names.
            Defaults to None. The name parameter is used;
            if both are empty, then it checks for any note's existence.

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean): Whether the note exists on the model.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "note",
        "function": "exists",
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]
    else:
        raise Warning(data)
    # TODO: group name/names


def get(client, name, current_file=None):
    """Get the text of a model or drawing note.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name.
        current_file (str, optional):
            Model name.
            Defaults is current active model or drawing.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            file (str): File name.
            name (str): Note name.
            encoded (boolean): Value is Base64-encoded.
            url (str): "Note URL, if there is one.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "note",
        "function": "get",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def list_(
    client,
    current_file=None,
    name=None,
    names=None,
    value=None,
    get_expanded=None
):
    """Get a list of notes from one or more models.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name (wildcards allows: True).
            Defaults is current active model.
        name (str, optional):
            Note name; only used if names is not given. Defaults to None.
        names (list:str, optional):
            List of notes names.
            Defaults to None. The name parameter is used;
            if both are empty, then all notes are listed.
        value (str, optional):
            Parameter value filter (wildcards allows: True).
            Defaults is `no filter`.
        get_expanded (boolean, optional):
            Whether to return text with parameter values replaced.
            Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict):
            name (str): Note name.
            value (str): Note text with parameters not expanded.
            value_expanded (str): Note text with parameters expanded.
            encoded (boolean): Value is Base64-encoded.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "note",
        "function": "list",
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    if get_expanded:
        request["data"]["get_expanded"] = get_expanded
    if value:
        request["data"]["value"] = value
    status, data = creoson_post(client, request)
    if not status:
        return data["itemlist"]
    else:
        raise Warning(data)
    # TODO: group name/names


def set_():
    pass

