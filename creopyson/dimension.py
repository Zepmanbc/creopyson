"""Dimension module."""


def copy(client, name, to_name, file_=None, to_file=None):
    """Copy dimension to another in the same model or another model.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Dimension name to copy.
        to_name (str):
            Destination dimension; th dimension must already exist.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        to_file (str, optional):
            Destination model. Defaults is the source model.

    Returns:
        None

    """
    data = {
        "name": name,
        "to_name": to_name
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if to_file:
        data["to_file"] = to_file
    return client._creoson_post("dimension", "copy", data)


def list_(
    client,
    name=None,
    file_=None,
    dim_type=None,
    encoded=None,
    select=False
):
    """Get a list of dimensions from a model.

    If select is true, then the current selection in Creo will be cleared even
    if no items are found.

    Args:
        client (obj):
            creopyson Client.
        name (str|list:str, optional):
            Dimension name;
            if empty then all dimensions are listed.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        dim_type (str, optional):
            Dimension type filter. Defaults is `no filter`.
            Valid values: linear, radial, diameter, angular.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded. Defaults is False.
        select (boolean, optional):
            If true, the dimensions that are found will be selected in Creo.
            Defaults is False.

    Returns:
        (list:dict): List of dimension information.
            name (str):
                Dimension name
            value (str|float):
                Dimension value; if encoded is True it is a str,
                if encoded is False it is a float.
            encoded (boolean):
                Whether the returned value is Base64-encoded.
            dwg_dim (boolean):
                Whether dimension is a drawing dimension rather than
                a model dimension.

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
    if dim_type:
        data["dim_type"] = dim_type
    if encoded:
        data["encoded"] = encoded
    if select:
        data["select"] = select
    return client._creoson_post("dimension", "list", data, "dimlist")


def list_detail(
    client,
    name=None,
    file_=None,
    dim_type=None,
    encoded=None,
    select=False
):
    """Get a list of dimension details from a model.

    Values will automatically be returned Base64-encoded if they are strings
    which contain Creo Symbols or other non-ASCII data.
    If select is true, then the current selection in Creo will be cleared
    even if no items are found.

    Args:
        client (obj):
            creopyson Client.
        name (str|list:str, optional):
            Dimension name;
            if empty then all dimensions are listed.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        dim_type (str, optional):
            Dimension type filter. Defaults is `no filter`.
            Valid values: linear, radial, diameter, angular.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded. Defaults is False.
        select (boolean, optional):
            If true, the dimensions that are found will be selected in Creo.
            Defaults is False.

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
            dwg_dim (boolean):
                Whether dimension is a drawing dimension rather than
                a model dimension.
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
    if dim_type:
        data["dim_type"] = dim_type
    if encoded:
        data["encoded"] = encoded
    if select:
        data["select"] = select
    return client._creoson_post("dimension", "list_detail", data, "dimlist")


def set_(client, name, value, file_=None, encoded=None):
    r"""Set a dimension value.

    One reason to encode values is if the value contains special characters,
    such as Creo symbols.
    You may be able to avoid Base64-encoding symbols by using Unicode for the
    binary characters, for example including \\u0001#\\u0002 in the value to
    insert a plus/minus symbol.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Dimension name.
        value (str|float):
            Dimension value.
        `file_` (string, optional):
            file name, if not set, active model is used.
        encoded (boolean, optional):
            Whether the value is Base64-encoded.
            Defaults is False.


    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    data = {
        "name": name,
        "value": value,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if encoded:
        data["encoded"] = encoded
    return client._creoson_post("dimension", "set", data)


def set_text(client, name, file_=None, text=None, encoded=False):
    """Set dimension text.

    Args:
        client (obj):
            creopyson object.
        name (str):
            Dimension name.
        `file_` (string, optional):
            file name, if not set, active model is used.
        text ([type], optional):
            Dimension text. Defaults to None, sets the dimension's text to @D.
        encoded (bool, optional):
            Whether the text value is Base64-encoded. Defaults to False.

    Returns:
        None

    """
    data = {
        "name": name,
        "encoded": encoded,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if text:
        data["text"] = text
    return client._creoson_post("dimension", "set_text", data)


def show(client, name, file_=None, assembly=None, path=None):
    """Display or hide a dimension in Creo.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Dimension name.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        assembly (str, optional):
            Assembly name; only used if path is given.
            Defaults is the currently active model.
        path (list:int, optional):
            Path to occurrence of the model within the assembly;
            the dimension will only be shown for that occurrence.
            Defaults: all occurrences of the component are affected.

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
    if assembly:
        data["assembly"] = assembly
    if path:
        data["path"] = path
    return client._creoson_post("dimension", "show", data)


def user_select(client, file_=None, maxi=None):
    """Prompt user to select one or more dimensions, and return their selections.

        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        maxi (int, optional):
            The maximum number of dimensions that the user can select.
            Defaults is `1`.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict): List of selected dimension information
            name (str):
                Dimension name
            value (str|float):
                Dimension value; if encoded is True it is a str,
                if encoded is False it is a float.
            encoded (boolean):
                Whether the returned value is Base64-encoded.
            file (str):
                File name.
            relation_id (int):
                Relation ID number.

    """
    data = {"max": 1}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if maxi:
        data["max"] = maxi
    return client._creoson_post("dimension", "user_select", data, "dimlist")
