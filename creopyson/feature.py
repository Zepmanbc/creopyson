"""Feature module."""
STATUS_LIST = [
    "ACTIVE",
    "INACTIVE",
    "FAMILY_TABLE_SUPPRESSED",
    "SIMP_REP_SUPPRESSED",
    "PROGRAM_SUPPRESSED",
    "SUPPRESSED",
    "UNREGENERATED",
]


def delete(client, name=None, file_=None, status=None, type_=None, clip=None):
    """Delete one or more features that match criteria.

    Args:
        client (obj):
            creopyson Client.
        name (str|list:str, optional):
            Dimension name, (wildcards allowed: True);
            if empty then all features are listed.
        `file_` (str, optional):
            Model name (wildcards allowed: True).
            Defaults is current active model.
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
        ValueError: status value is incorrect.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        if isinstance(name, (str)):
            data["name"] = name
        elif isinstance(name, (list)):
            data["names"] = name
    if status in STATUS_LIST:
        data["status"] = status
    elif status is not None:
        raise ValueError(f"`{status}` is not a correct status.")
    if type_ is not None:
        data["type"] = type_
    if clip is not None:
        data["clip"] = clip
    return client._creoson_post("feature", "delete", data)


def delete_param(client, name=None, file_=None, param=None):
    """Delete a feature parameter.

    Args:
        client (obj):
            creopyson Client.
        name (str, optional):
            Parameter name (wildcards allowed: True).
            Defaults: All parameter names.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        param (str, optional):
            Parameter name (wildcards allowed: True).
            Defaults: All parameter names.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        data["name"] = name
    if param:
        data["param"] = param
    return client._creoson_post("feature", "delete_param", data)


def list_(
    client,
    file_=None,
    name=None,
    status=None,
    type_=None,
    paths=None,
    no_datum=None,
    inc_unnamed=None,
    no_comp=None,
):
    """List feature parameters that match criteria.

    Will only list parameters on visible features.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is the currently active model.
        name (str, optional):
            Feature name (wildcards allowed: True).
            Defaults: All features are listed.
        status (str, optionnal):
            Feature status pattern.
            Defaults: All feature statuses.
            Valid values: ACTIVE, INACTIVE, FAMILY_TABLE_SUPPRESSED,
            SIMP_REP_SUPPRESSED, PROGRAM_SUPPRESSED, SUPPRESSED, UNREGENERATED.
        `type_` (str, optional):
            Feature type patter (wildcards allowed: True).
            Defaults: All feature types.
        paths (boolean, optionnal):
            Whether feature ID and feature number are returned with the data
            Default: False.
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

    Raises:
        ValueError: status value is incorrect.

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
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        data["name"] = name
    if status in STATUS_LIST:
        data["status"] = status
    elif status is not None:
        raise ValueError(f"`{status}` is not a correct status.")
    if type_ is not None:
        data["type"] = type_
    if paths is not None:
        data["paths"] = paths
    if no_datum is not None:
        data["no_datum"] = no_datum
    if inc_unnamed is not None:
        data["inc_unnamed"] = inc_unnamed
    if no_comp is not None:
        data["no_comp"] = no_comp
    return client._creoson_post("feature", "list", data, "featlist")


def list_params(
    client,
    file_=None,
    name=None,
    type_=None,
    no_datum=None,
    inc_unnamed=None,
    no_comp=None,
    param=None,
    value=None,
    encoded=None,
):
    """List feature parameters that match criteria.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is the currently active model.
        name (str|int, optional):
            str: Feature name (wildcards allowed: True).
            int: Feature ID.
            Defaults: All features are listed.
        `type_` (str, optional):
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
        param (str|list:str, optional):
            Parameter name; (wildcards allowed: True)
            if empty all parameters are listed.
        value (str, optional):
            Parameter value filter (wildcards allowed: True).
            Defaults is no filter.
        encoded (boolean, optional):
            Whether to return the values Base64-encoded.
            Defaults is False.

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
            description (str):
                List of parameter information.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        if isinstance(param, (str)):
            data["name"] = name
        elif isinstance(param, (list)):
            data["feat_id"] = name
    if type_ is not None:
        data["type"] = type_
    if no_datum is not None:
        data["no_datum"] = no_datum
    if inc_unnamed is not None:
        data["inc_unnamed"] = inc_unnamed
    if no_comp is not None:
        data["no_comp"] = no_comp
    if param is not None:
        if isinstance(param, (str)):
            data["param"] = param
        elif isinstance(param, (list)):
            data["params"] = param
    if value is not None:
        data["value"] = value
    if encoded is not None:
        data["encoded"] = encoded
    return client._creoson_post("feature", "list_params", data, "paramlist")


def list_group_features(client, group_name, type_=None, file_=None):
    """List features in a Creo Group.

    Args:
        client (obj):
            creopyson Client.
        group_name (str):
            Group name.
        `type_` (str, optional):
            Feature type patter (wildcards allowed: True).
            Defaults: All feature types.
        `file_` (str, optional):
            File name. Defaults is the currently active model.

    Returns:
        (list:dict): List of feature information

    """
    data = {
        "group_name": group_name,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if type_ is not None:
        data["type"] = type_
    return client._creoson_post("feature", "list_group_features", data, "featlist")


def list_pattern_features(client, patter_name, type_=None, file_=None):
    """List features in a Creo Pattern.

    Args:
        client (obj):
            creopyson Client.
        patter_name (str):
            Pattern name.
        `type_` (str, optional):
            Feature type patter (wildcards allowed: True).
            Defaults: All feature types.
        `file_` (str, optional):
            File name. Defaults is the currently active model.

    Returns:
        (list:dict): List of feature information

    """
    data = {
        "patter_name": patter_name,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if type_ is not None:
        data["type"] = type_
    return client._creoson_post("feature", "list_group_features", data, "featlist")


def list_selected(client):
    """List the currently selected features in Creo

    Returns:
        (list): List of feature informations.
            [
                {
                    'file' : model name (str)

                    'name' : feature name (str)

                    'status' : feature status (str)

                    'type' : feature type (str)

                    'feat_id' : feature ID (int)

                    'feat_number' : feature number (int)

                    'path' : feature's component path (list of ints)

                },

            ]

    """
    data = None
    return client._creoson_post("feature", "list_selected", data, "featlist")


def param_exists(client, file_=None, name=None, param=None):
    """Check whether parameter(s) exists on a feature.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is the currently active model.
        name (str, optional):
            Parameter name (wildcards allowed: True).
            Defaults: All parameter names.
        param (str|list:str, optional):
            Parameter name; (wildcards allowed: True)
            if empty all parameters are listed.

    Returns:
        (boolean): Whether the parameter exists on the model

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        data["name"] = name
    if param is not None:
        if isinstance(param, (str)):
            data["param"] = param
        elif isinstance(param, (list)):
            data["params"] = param
    return client._creoson_post("feature", "param_exists", data, "exists")


def rename(client, name, new_name, file_=None):
    """Rename a feature.

    Args:
        client (obj):
            creopyson Client.
        name (str|int, optional):
            Feature name (str) or Feature ID (int).
        new_name (str):
            New name for the feature.
        `file_` (str, optional):
            File name.
            Defaults is the currently active model.

    Returns:
        None

    """
    data = {"new_name": new_name}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if isinstance(name, (str)):
        data["name"] = name
    elif isinstance(name, (int)):
        data["feat_id"] = name
    else:
        raise TypeError("name must be str or int")
    return client._creoson_post("feature", "rename", data)


def resume(client, file_=None, name=None, status=None, type_=None, with_children=None):
    """Resume one or more features that match criteria.

    Will only resume visible features.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name (wildcards allowed: True).
            Defaults is the currently active model.
        name (int|str|list:str, optional):
            Feature name or Feature ID, (wildcards allowed: True);
            if empty then all features are resumed.
            int => Feat_ID
            str => name
            list:str => names
        status (str, optional):
            Feature status pattern. Defaults: All feature statuses.
            Valid values: ACTIVE, INACTIVE, FAMILY_TABLE_SUPPRESSED,
            SIMP_REP_SUPPRESSED, PROGRAM_SUPPRESSED, SUPPRESSED, UNREGENERATED
        `type_` (str, optional):
            Feature type pattern (wildcards allowed: True).
            Defaults: All feature types.
        with_children (boolean, optional):
            Whether to resume any child features of the resumed feature.
            Defaults is False.

    Raises:
        ValueError: status value is incorrect.

    Returns:
        None

    """
    data = {
        "with_children": False,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        if isinstance(name, (int)):
            data["feat_id"] = name
        elif isinstance(name, (str)):
            data["name"] = name
        elif isinstance(name, (list)):
            data["names"] = name
    if status in STATUS_LIST:
        data["status"] = status
    elif status is not None:
        raise ValueError(f"`{status}` is not a correct status.")
    if type_ is not None:
        data["type"] = type_
    if with_children is not None:
        data["with_children"] = with_children
    return client._creoson_post("feature", "resume", data)


def set_param(
    client,
    param,
    file_=None,
    name=None,
    type_=None,
    value=None,
    encoded=None,
    designate=None,
    description=None,
    no_create=None,
):
    """Set the value of a feature parameter.

    Will only set parameters on visible features.

    Args:
        client (obj):
            creopyson Client.
        param (str):
            Parameter name.
        `file_` (str, optional):
            File name (wildcards allowed: True).
            Defaults is the currently active model.
        name (str, optional):
            Feature name. Defaults: All features are updated.
        `type_` (str, optional):
            Parameter data type. Defaults is True.
            Valid values: STRING, DOUBLE, INTEGER, BOOL, NOTE.
        value (depends on data type, optional):
            Parameter value. Defaults: Clears the parameter value if missing.
        encoded (boolean, optional):
            Value is Base64-encoded. Defaults is False.
        designate (boolean, optional):
            Set parameter to be designated/not designated, blank=do not set.
            Defaults is `blank`.
        description (str, optionnal):
            Parameter description. If missing, leaves the currect description in place.
        no_create (boolean, optional):
            If parameter does not already exist, do not create it.
            Defaults is False.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        data["name"] = name
    if param is not None:
        data["param"] = param
    if type_ is not None:
        data["type"] = type_
    if value is not None:
        data["value"] = value
    if encoded is not None:
        data["encoded"] = encoded
    if designate is not None:
        data["designate"] = designate
    if description is not None:
        data["description"] = description
    if no_create is not None:
        data["no_create"] = no_create
    return client._creoson_post("feature", "set_param", data)


def suppress(
    client,
    file_=None,
    name=None,
    status=None,
    type_=None,
    clip=None,
    with_children=None,
):
    """Suppress one or more features that match criteria.

    Will only suppress visible features.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name (wildcards allowed: True).
            Defaults is the currently active model.
        name (int|str|list:str, optional):
            Feature name or Feature ID, (wildcards allowed: True);
            if empty then all features are suppressed.
            int => Feat_ID
            str => name
            list:str => names
        status (str, optional):
            Feature status pattern. Defaults: All feature statuses.
            Valid values: ACTIVE, INACTIVE, FAMILY_TABLE_SUPPRESSED,
            SIMP_REP_SUPPRESSED, PROGRAM_SUPPRESSED, SUPPRESSED, UNREGENERATED
        `type_` (str, optional):
            Feature type pattern (wildcards allowed: True).
            Defaults: All feature types.
        clip (boolean, optional):
            Whether to clip-suppress ANY features from this feature through
            the end of the structure. Defaults is True.
        with_children (boolean, optional):
            Whether to suppress  any child features of the suppressed feature.
            Defaults is True.

    Raises:
        ValueError: status value is incorrect.

    Returns:
        None

    """
    data = {"clip": True, "with_children": True}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if name is not None:
        if isinstance(name, (int)):
            data["feat_id"] = name
        elif isinstance(name, (str)):
            data["name"] = name
        elif isinstance(name, (list)):
            data["names"] = name
    if status in STATUS_LIST:
        data["status"] = status
    elif status is not None:
        raise ValueError(f"`{status}` is not a correct status.")
    if type_ is not None:
        data["type"] = type_
    if clip is False:
        data["clip"] = False
    if with_children is False:
        data["with_children"] = False
    return client._creoson_post("feature", "suppress", data)


def user_select_csys(client, file_=None, max_=None):
    """Prompt the user to select one or more coordinate systems.

    and return their selections.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name.
            Defaults is the currently active model.
        `max_` (int, optional):
            The maximum number of dimensions that the user can select.
            Defaults is `1`.

    Returns:
        (list:dict):
            List of feature information.
                name (str):
                    Feature name.
                type (string):
                    Feature type.
                status (str):
                    Feature status.
                    Valid values: ACTIVE, INACTIVE, FAMILY_TABLE_SUPPRESSED,
                    SIMP_REP_SUPPRESSED, PROGRAM_SUPPRESSED, SUPPRESSED,
                    UNREGENERATED.
                feat_id (int):
                    Feature ID.
                file (str):
                    File name containing the feature.
                path (list:int):
                    Component Path to feature (optionnal)

    """
    data = {
        "max": 1,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file:
            data["file"] = active_file["file"]
    if max_ is not None:
        data["max"] = max_
    return client._creoson_post("feature", "user_select_csys", data)
