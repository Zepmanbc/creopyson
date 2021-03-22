"""Parameter module."""


def copy(client, name, to_name, file_=None, to_file=None, designate=None):
    """Copy parameter to another in the same model or another model.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Parameter name to copy (wildcards allowed: True).
        to_name (str):
            Destination parameter.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        to_file (str, optional):
            Destination model (wildcards allowed: True).
            Defaults is the source model.
        designate (boolean, optional):
            Set copied parameter to be designated/not designated,
            blank=do not set. Defaults is `blank`.

    Returns:
        None

    """
    data = {
        "name": name,
        "to_name": to_name,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if to_file:
        data["to_file"] = to_file
    if designate:
        data["designate"] = designate
    return client._creoson_post("parameter", "copy", data)


def delete(client, name, file_=None):
    """Delete a parameter.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Parameter name (wildcards allowed: True).
        `file_` (str, optional):
            Model name. Defaults is current active model.

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
    return client._creoson_post("parameter", "delete", data)


def exists(client, name=None, file_=None):
    """Check whether parameter(s) exists on a model.

    Args:
        client (obj):
            creopyson Client.
        name (str|list:str, optional):
            Parameter name; List of parameter names.
            if empty it checks for any parameter's existence.
        `file_` (str, optional):
            Model name. Defaults is current active model.

    Returns:
        (boolean): Whether the parameter exists on the model.

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
    return client._creoson_post("parameter", "exists", data, "exists")


def list_(client, name=None, file_=None, encoded=None, value=None):
    """Get a list of parameters from one or more models.

    Args:
        client (obj):
            creopyson Client.
        name (str|list:str, optional):
            Parameter name; List of parameter names.
            if empty it checks for any parameter's existence.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded. Defaults is False.
        value (str, optional):
            Parameter value filter. Defaults is `no filter`.

    Returns:
        (list:dict):
            name (str): Parameter name.
            type (str): Parameter type.
            value (various): Parameter value # TODO
            designate (boolean): Whether the parameter is designated.
            description (str): Description.
            encoded (boolean): Whether the parameter is encoded.
            owner_name (str): File name.

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
    if encoded:
        data["encoded"] = encoded
    if value:
        data["value"] = value
    return client._creoson_post("parameter", "list", data, "paramlist")


def set_(
    client,
    name,
    value=None,
    file_=None,
    type_=None,
    encoded=None,
    designate=None,
    description=None,
    no_create=None,
):
    """Set the value of a parameter.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Parameter name (wildcards allowed: True).
        value (depends on data type, optional):
            Parameter value. Defaults to None.
            Clears the parameter value if missing.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        `type_` (str, optional):
            Data type. Defaults is `STRING`.
            Valid values: STRING, DOUBLE, INTEGER, BOOL, NOTE.
        encoded (boolean, optional):
            Whether the value is Base64-encoded. Defaults is False.
        designate (boolean, optional):
            Set parameter to be designated/not designated, blank=do not set.
            Defaults is `blank`.
        description (str, optional):
            Parameter description.
            If missing, leaves the current description in place.
        no_create (boolean, optional):
            If parameter does not already exist, do not create it.
            Defaults is False.

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
    if type_:
        data["type"] = type_
    if encoded:
        data["encoded"] = encoded
    if value:
        data["value"] = value
    if designate:
        data["designate"] = designate
    if description:
        data["description"] = description
    if no_create:
        data["no_create"] = no_create
    return client._creoson_post("parameter", "set", data)


def set_designated(
    client,
    name,
    designate,
    file_=None,
):
    """Set the designated state of a parameter.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Parameter name (wildcards allowed: True).
        designate (boolean):
            Set parameter to be designated/not designated.
        `file_` (str, optional):
            Model name. Defaults is current active model.

    Returns:
        None

    """
    data = {
        "name": name,
        "designate": designate,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("parameter", "set_designated", data)
