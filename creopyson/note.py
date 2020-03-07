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

    Values will automatically be returned Base64-encoded if they are strings
    which contain Creo Symbols or other non-ASCII data.

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
            file (str):
                File name.
            name (str):
                Note name.
            encoded (boolean):
                Value is Base64-encoded.
            url (str):
                "Note URL, if there is one.
            location (obj:JLPoint):
                Note location in Drawing Units (drawing notes only)

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
    get_expanded=None,
    select=False
):
    """Get a list of notes from one or more models.

    Values will automatically be returned Base64-encoded if they are strings
    which contain Creo Symbols or other non-ASCII data.

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
        select (boolean, optional):
            If true, the notes that are found will be selected in Creo.
            Defaults is False.

    Returns:
        (list:dict):
            name (str): Note name.
            value (str): Note text with parameters not expanded.
            value_expanded (str): Note text with parameters expanded.
            encoded (boolean): Value is Base64-encoded.
            location (jlpoint): 3D coordinate dict.

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
        data["get_expanded"] = True
    if value:
        data["value"] = value
    if select:
        data["select"] = True
    return client._creoson_post("note", "list", data, "itemlist")


def set_(client, name, file_=None, encoded=None, value=None):
    r"""Set the text of a model or drawing note.

    The location parameter can used to position a new note, or to change the
    position of an existing note. If the text contains Creo Symbols or other
    non-ASCII text, you must Base64-encode the value and set encoded to true
    You may be able to avoid Base64-encoding symbols by using Unicode for the
    binary characters, for example including \\u0001#\\u0002 in the value to
    insert a plus/minus symbol. Embed newlines in the value for line breaks.

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
            Defaults to None: clears the note if missing.

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
