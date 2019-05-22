"""Feature module."""

from .core import creoson_post


def delete(
    client,
    current_file=None,
    name=None,
    names=None,
    status=None,
    type_=None,
    clip=None
):
    """Delete one or more features that match criteria.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name (wildcards allowed: True).
            Defaults is current active model.
        name (str, optional):
            Feature name; only used if names is not given
            (wildcards allowed: True).
            Defaults to None.
        names (list:str, optional):
            List of feature names.
            Defaults to None: The name parameter is used;
            if both are empty, then all features may be deleted.
        status (str, optional):
            Feature status pattern (wildcards allowed: True).
            Defaults: All feature statuses.
            Valid values: ACTIVE, INACTIVE, FAMILY_TABLE_SUPPRESSED,
            SIMP_REP_SUPPRESSED, PROGRAM_SUPPRESSED, SUPPRESSED, UNREGENERATED
        `type_` (str, optional):
            Feature type pattern (wildcards allowed: True).
            Defaults: All feature types.
        clip (boolean, optional):
            Whether to clip-delete ANY features from this feature through
            the end of the structure.
            Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "feature",
        "function": "delete",
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if names:
        request["data"]["names"] = names
    if status:
        request["data"]["status"] = status
    if type_:
        request["data"]["type"] = type_
    if clip:
        request["data"]["clip"] = clip
    status_, data = creoson_post(client, request)
    if not status_:
        return data["exists"]
    else:
        raise Warning(data)


def delete_param(client, name=None, current_file=None, param=None):
    """Delete a feature parameter.

    Args:
        client (obj):
            creopyson Client.
        name (str, optional):
            Parameter name (wildcards allowed: True).
            Defaults: All parameter names.
        current_file (str, optional):
            Model name. Defaults is current active model.
        param (str, optional):
            Parameter name (wildcards allowed: True).
            Defaults: All parameter names.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "feature",
        "function": "delete_param",
    }
    if current_file:
        request["data"]["file"] = current_file
    if name:
        request["data"]["name"] = name
    if param:
        request["data"]["param"] = param
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]
    else:
        raise Warning(data)


def list_(
    client,
    current_file=None,
    name=None,
    type_=None,
    no_datum=None,
    inc_unnamed=None,
    no_comp=None,
    param=None,
    params=None,
    value=None,
    encoded=None
):
    """List feature parameters that match criteria.

    Will only list parameters on visible features.
    Args:
        client (obj): creopyson Client.
        current_file (str, optional):
            File name. Defaults is the currently active model.
        name ([str, optional):
            Feature name (wildcards allowed: True).
            Defaults: All features are listed.
        type_ (str, optional):
            Feature type patter (wildcards allowed: True).
            Defaults: All feature types.
        no_datum (boolean, optional):
            Whether to exclude datum-type features from the list;
            these are COORD_SYS, CURVE, DATUM_AXIS, DATUM_PLANE, DATUM_POINT,
            DATUM_QUILT, and DATUM_SURFACE features.
            Defaults is False.
        inc_unnamed (boolean, optional):
            Whether to include unnamed features in the list.
            Defaults is False.
        no_comp (boolean, optional):
            Whether to include component-type features in the list.
            Defaults is False.
        param (string, optional):
            Parameter name; only used if params is not given.
            (wildcards allowed: True)
        params (list:str, optional):
            List of parameter names.
            Defaults: The param parameter is used; if both are empty,
            then all parameters are listed.
        value (str, optional):
            Parameter value filter (wildcards allowed: True).
            Defaults is no filter.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded.
            Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:dict): List of parameter information.
            name (str):
                Parameter nam.
            value (depends on data type):
                Parameter value.
            type (string):
                Data type. Valid values: STRING, DOUBLE, INTEGER, BOOL, NOTE.
            designate (boolean):
                Value is designated.
            encoded (boolean):
                Value is Base64-encoded.
            owner_name (str):
                Owner Name.
            owner_id (int):
                Owner ID.
            owner_type (str):
                Owner type.

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
    if type_:
        request["data"]["type"] = type_
    if no_datum:
        request["data"]["no_datum"] = no_datum
    if inc_unnamed:
        request["data"]["inc_unnamed"] = inc_unnamed
    if no_comp:
        request["data"]["no_comp"] = no_comp
    if param:
        request["data"]["param"] = param
    if params:
        request["data"]["params"] = params
    if value:
        request["data"]["value"] = value
    if encoded:
        request["data"]["encoded"] = encoded
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)
    # TODO: param/params



# def param_exist():
#     pass


# def rename():
#     pass


# def resume():
#     valid_values = ["ACTIVE", "INACTIVE", "FAMILY_TABLE_SUPPRESSED", \
# "SIMP_REP_SUPPRESSED", "PROGRAM_SUPPRESSED", "SUPPRESSED", "UNREGENERATED"]
#     pass


# def set_param():
#     pass


# def suppress():
#     pass


# def user_select_csys():
#     pass
