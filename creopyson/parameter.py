"""Parameter module."""


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
    status, data = client.creoson_post(request)
    if not status:
        return data
    else:
        raise Warning(data)


def delete(client, name, current_file=None):
    """Delete a parameter.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Parameter name (wildcards allowed: True).
        current_file (str, optional):
            Model name. Defaults is current active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "delete",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = client.creoson_post(request)
    if status:
        raise Warning(data)


def exists(client, current_file=None, name=None, names=None):
    """Check whether parameter(s) exists on a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            Parameter name; only used if names is not given. Defaults to None.
        names (list:str, optional):
            List of parameter names.
            Defaults to None. The name parameter is used;
            if both are empty, then it checks for any parameter's existence.

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean): Whether the parameter exists on the model.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "exists",
        "data": {}
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    status, data = client.creoson_post(request)
    if not status:
        return data["exists"]
    else:
        raise Warning(data)
    # TODO: group name/names


def list_(
    client,
    current_file=None,
    name=None,
    names=None,
    encoded=None,
    value=None
):
    """Get a list of parameters from one or more models.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            Parameter name; only used if names is not given. Defaults to None.
        names (list:str, optional):
            List of parameter names.
            Defaults to None. The name parameter is used;
            if both are empty, then it checks for any parameter's existence.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded. Defaults is False.
        value (str, optional):
            Parameter value filter. Defaults is `no filter`.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict):
            name (str): Parameter name.
            type (str): Parameter type.
            value (various): Parameter value # TODO
            designate (boolean): Whether the parameter is designated.
            encoded (boolean): Whether the parameter is encoded.
            owner_name (str): File name.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "list",
        "data": {}
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    if encoded:
        request["data"]["encoded"] = encoded
    if value:
        request["data"]["value"] = value
    status, data = client.creoson_post(request)
    if not status:
        return data["paramlist"]
    else:
        raise Warning(data)


def set_(
    client,
    name,
    value=None,
    current_file=None,
    type_=None,
    encoded=None,
    designate=None,
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
        current_file (str, optional):
            Model name. Defaults is current active model.
        `type_` (str, optional):
            Data type. Defaults is `STRING`.
            Valid values: STRING, DOUBLE, INTEGER, BOOL, NOTE.
        encoded (boolean, optional):
            Whether the value is Base64-encoded. Defaults is False.
        designate (boolean, optional):
            Set parameter to be designated/not designated, blank=do not set.
            Defaults is `blank`.
        no_create (boolean, optional):
            If parameter does not already exist, do not create it.
            Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "parameter",
        "function": "lisetst",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if type_:
        request["data"]["type"] = type_
    if encoded:
        request["data"]["encoded"] = encoded
    if value:
        request["data"]["value"] = value
    if designate:
        request["data"]["designate"] = designate
    if no_create:
        request["data"]["no_create"] = no_create
    status, data = client.creoson_post(request)
    if status:
        raise Warning(data)
