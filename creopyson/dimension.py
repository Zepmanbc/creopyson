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


def list_(
    client,
    current_file=None,
    name=None,
    names=None,
    dim_type=None,
    encoded=None
):
    """Get a list of dimensions from a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            Dimension name; only used if names is not given.
            Defaults: The name parameter is used; if both are empty,
            then all dimensions are listed.
        names (list:str, optional):
            List of dimension names. Defaults to None.
        dim_type (str, optional):
            Dimension type filter. Defaults is `no filter`.
            Valid values: linear, radial, diameter, angular.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict): List of dimension information.
            name (str):
                Dimension name
            value (str|float):
                Dimension value; if encoded is True it is a str,
                if encoded is False it is a float.
            encoded (boolean):
                Whether the returned value is Base64-encoded.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "list",
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    if dim_type:
        request["data"]["dim_type"] = dim_type
    if encoded:
        request["data"]["encoded"] = encoded
    status, data = creoson_post(client, request)
    if not status:
        return data["dimlist"]
    else:
        raise Warning(data)
    # TODO only 1 entry for name/names


def list_detail(
    client,
    current_file=None,
    name=None,
    names=None,
    dim_type=None,
    encoded=None
):
    """Get a list of dimension details from a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            Dimension name; only used if names is not given.
            Defaults: The name parameter is used; if both are empty,
            then all dimensions are listed.
        names (list:str, optional):
            List of dimension names. Defaults to None.
        dim_type (str, optional):
            Dimension type filter. Defaults is `no filter`.
            Valid values: linear, radial, diameter, angular.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict): List of dimension information.
            name (str):
                Dimension name
            value (str|float):
                Dimension value; if encoded is True it is a str,
                if encoded is False it is a float.
            encoded (boolean):
                Whether the returned value is Base64-encoded.
            sheet (int):
                Sheet number.
            view_name (str):
                View name.
            dim_type (str):
                Dimension type.
                Valid values: linear, radial, diameter, angular.
            text (str):
                dimension text.
            location (dict): Coordonates location.
                x (float): X coordonate location.
                y (float): Y coordonate location.
                z (float): Z coordonate location.
            tolerance_type (str):
                Tolerance type, if not specified not returned.
                Valid values: plus_minus (TODO complete list).
            tol_plus (float):
                Plus tolerance value.
                if tolerance_type not specified not returned.
            tol_minus (float):
                Minus tolerance value.
                if tolerance_type not specified not returned.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "list_detail",
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    if dim_type:
        request["data"]["dim_type"] = dim_type
    if encoded:
        request["data"]["encoded"] = encoded
    status, data = creoson_post(client, request)
    if not status:
        return data["dimlist"]
    else:
        raise Warning(data)


def set_(client, name, current_file=None, encoded=None, value=None,):
    """Set a dimension value.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Dimension name.
        current_file (str, optional):
            Model name. Defaults is current active model.
        encoded (boolean, optional):
            Whether the value is Base64-encoded.
            Defaults is False.
        value (str|float, optional):
            Dimension value.
            Defaults to None, clears the dimension value if missing.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "set",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if encoded:
        request["data"]["encoded"] = encoded
    if value:
        request["data"]["value"] = value
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def show(client, name, current_file=None, assembly=None, path=None):
    """Display or hide a dimension in Creo.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Dimension name.
        current_file (str, optional):
            Model name. Defaults is current active model.
        assembly (str, optional):
            Assembly name; only used if path is given.
            Defaults is the currently active model.
        path (list:int, optional):
            Path to occurrence of the model within the assembly;
            the dimension will only be shown for that occurrence.
            Defaults: all occurrences of the component are affected.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "show",
        "data": {
            "name": name
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if assembly:
        request["data"]["assembly"] = assembly
    if path:
        request["data"]["path"] = path
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


# def user_select():
#     pass
