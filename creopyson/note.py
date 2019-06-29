"""Note module."""


def copy(client, name, to_name=None, file_=None, to_file=None):
    """Copy note to another in the same model or another model.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name to copy (wildcards allowed: True).
        to_name (str):
            Destination note.
            Defaults is the source note name
        `file_` (str, optional):
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
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if to_file:
        data["to_file"] = to_file
    return client._creoson_post("note", "copy", data)


def delete(client, name, file_=None):
    """Delete a model or drawing note.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name (wildcards allowed: True).
        `file_` (str, optional):
            Model name (wildcards allowed: True).
            Defaults is current active model.

    Returns:
        None

    """
    data = {"name": name}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("note", "delete", data)


def exists(client, file_=None, name=None):
    """Check whether note(s) exists on a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        name (str|list:str, optional):
            Note name; List of note names.
            if empty it checks for any note's existence.

    Returns:
        (boolean): Whether the note exists on the model.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if name:
        if isinstance(name, (str)):
            data["name"] = name
        elif isinstance(name, (list)):
            data["names"] = name
    return client._creoson_post("note", "exists", data, "exists")


def get(client, name, file_=None):
    """Get the text of a model or drawing note.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name.
        `file_` (str, optional):
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
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("note", "get", data)


def list_(
    client,
    file_=None,
    name=None,
    value=None,
    get_expanded=None
):
    """Get a list of notes from one or more models.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name (wildcards allows: True).
            Defaults is current active model.
        name (str|list:str, optional):
            Note name; List of note names.
            if empty all notes are listed.
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
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if name:
        if isinstance(name, (str)):
            data["name"] = name
        elif isinstance(name, (list)):
            data["names"] = name
    if get_expanded:
        data["get_expanded"] = get_expanded
    if value:
        data["value"] = value
    return client._creoson_post("note", "list", data, "itemlist")


def set_(client, name, file_=None, encoded=None, value=None):
    """Set the text of a model or drawing note.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Note name (wildcards allowed: True).
        `file_` (str, optional):
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
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if encoded:
        data["encoded"] = encoded
    if value:
        data["value"] = value
    return client._creoson_post("note", "set", data)
