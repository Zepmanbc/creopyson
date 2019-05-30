"""Note module."""


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

    Returns:
        None

    """
    data = {"name": name}
    if to_name:
        data["to_name"] = to_name
    if current_file:
        data["file"] = current_file
    if to_file:
        data["to_file"] = to_file
    return client.creoson_post("note", "copy", data)


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

    Returns:
        None

    """
    data = {"name": name}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("note", "delete", data)


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

    Returns:
        (boolean): Whether the note exists on the model.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if names:
        data["names"] = names
    return client.creoson_post("note", "exists", data)["exists"]
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

    Returns:
        (dict):
            file (str): File name.
            name (str): Note name.
            encoded (boolean): Value is Base64-encoded.
            url (str): "Note URL, if there is one.

    """
    data = {"name": name}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("note", "get", data)


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

    Returns:
        (list:dict):
            name (str): Note name.
            value (str): Note text with parameters not expanded.
            value_expanded (str): Note text with parameters expanded.
            encoded (boolean): Value is Base64-encoded.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if names:
        data["names"] = names
    if get_expanded:
        data["get_expanded"] = get_expanded
    if value:
        data["value"] = value
    return client.creoson_post("note", "list", data)["itemlist"]
    # TODO: group name/names


def set_(client, name, current_file=None, encoded=None, value=None):
    """Set the text of a model or drawing note.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name (wildcards allowed: True).
        current_file (str, optional):
            Model name. Defaults is current active model or drawing.
        encoded (boolean, optional):
            Whether the value is Base64-encoded. Defaults is False.
        value (str, optional):
            Note text with parameters not expanded.
            Defaults to None: clears the note if missing;
            embed newlines for line breaks

    Returns:
        None

    """
    data = {"name": name}
    if current_file:
        data["file"] = current_file
    if encoded:
        data["encoded"] = encoded
    if value:
        data["value"] = value
    return client.creoson_post("note", "set", data)
