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
        "command": "interface",
        "function": "export_program",
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
        return data
    else:
        raise Warning(data)
    # TODO only 1 entry for name/names


# def list_detail():
#     pass


def set_(client, name, value, current_file=None):
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "set",
        "data": {
            "name": name,
            "value": value,
            "encoded": False
        }
    }
    if current_file:
        request["data"]["file"] = current_file
        requests.post(client.server, data=json.dumps(request))


# def show():
#     pass


# def user_select():
#     pass
