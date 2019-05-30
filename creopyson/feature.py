"""Feature module."""


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

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if names:
        data["names"] = names
    if status:
        data["status"] = status
    if type_:
        data["type"] = type_
    if clip:
        data["clip"] = clip
    return client.creoson_post("feature", "delete", data)["exists"]


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

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if param:
        data["param"] = param
    return client.creoson_post("feature", "delete_param", data)["exists"]


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
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is the currently active model.
        name ([str, optional):
            Feature name (wildcards allowed: True).
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
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if type_:
        data["type"] = type_
    if no_datum:
        data["no_datum"] = no_datum
    if inc_unnamed:
        data["inc_unnamed"] = inc_unnamed
    if no_comp:
        data["no_comp"] = no_comp
    if param:
        data["param"] = param
    if params:
        data["params"] = params
    if value:
        data["value"] = value
    if encoded:
        data["encoded"] = encoded
    return client.creoson_post("feature", "list", data)
    # TODO: param/params


def param_exists(client, current_file=None, param=None, params=None):
    """Check whether parameter(s) exists on a feature.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is the currently active model.
        param (string, optional):
            Parameter name; only used if params is not given.
            (wildcards allowed: True)
        params (list:str, optional):
            List of parameter names.
            Defaults: The param parameter is used; if both are empty,
            then all parameters are listed.

    Returns:
        (boolean): Whether the parameter exists on the model

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if param:
        data["param"] = param
    if params:
        data["params"] = params
    return client.creoson_post("feature", "param_exists", data)["exists"]
    # TODO: param/params


def rename(client, new_name, current_file=None, feat_id=None, name=None):
    """Rename a feature.

    Args:
        client (obj):
            creopyson Client.
        new_name (str):
            New name for the feature.
        current_file (str, optional):
            File name.
            Defaults is the currently active model.
        feat_id (int, optional):
            Feature ID. Defaults: the name parameter is used.
        name (list:str, optional):
            Feature name; only used if feat_id is not given.
            Defaults to None.

    Returns:
        None

    """
    data = {"new_name": new_name}
    if current_file:
        data["file"] = current_file
    if feat_id:
        data["feat_id"] = feat_id
    if name:
        data["name"] = name
    return client.creoson_post("feature", "rename", data)
    # TODO: feat_id/name


def resume(
    client,
    current_file=None,
    name=None,
    names=None,
    status=None,
    type_=None,
    with_children=None
):
    """Resume one or more features that match criteria.

    Will only resume visible features.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name (wildcards allowed: True).
            Defaults is the currently active model.
        name (str, optional):
            Feature name; only used if names is not given
            (wildcards allowed: True). Defaults to None.
        names (lst:str, optional):
            List of feature names. Defaults to None.
            The name parameter is used; if both are empty,
            then all features may be resumed.
        status (str, optional):
            Feature status pattern. Defaults: All feature statuses.
            Valid values: ACTIVE, INACTIVE, FAMILY_TABLE_SUPPRESSED,
            SIMP_REP_SUPPRESSED, PROGRAM_SUPPRESSED, SUPPRESSED, UNREGENERATED
        `type_` (str, optional):
            Feature type pattern (wildcards allowed: True).
            Defaults: All feature types.
        with_children (boolean, optional):
            Whether to resume any child features of the resumed feature.
            Defaults is True.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if names:
        data["names"] = names
    if status:
        data["status"] = status
    if type_:
        data["type"] = type_
    if with_children:
        data["with_children"] = with_children
    return client.creoson_post("feature", "resume", data)


def set_param(
    client,
    current_file=None,
    name=None,
    param=None,
    type_=None,
    value=None,
    encoded=None,
    designate=None,
    no_create=None
):
    """Set the value of a feature parameter.

    Will only set parameters on visible features.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name (wildcards allowed: True).
            Defaults is the currently active model.
        name (str, optional):
            Feature name. Defaults: All features are updated.
        param (str, optional):
            Parameter name. Defaults is True.
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
        no_create (boolean, optional):
            If parameter does not already exist, do not create it.
            Defaults is False.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if param:
        data["param"] = param
    if type_:
        data["type"] = type_
    if value:
        data["value"] = value
    if encoded:
        data["encoded"] = encoded
    if designate:
        data["designate"] = designate
    if no_create:
        data["no_create"] = no_create
    return client.creoson_post("feature", "set_param", data)


def suppress(
    client,
    current_file=None,
    name=None,
    names=None,
    status=None,
    type_=None,
    clip=None,
    with_children=None
):
    """Suppress one or more features that match criteria.

    Will only suppress visible features.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name (wildcards allowed: True).
            Defaults is the currently active model.
        name (str, optional):
            Feature name; only used if names is not given
            (wildcards allowed: True). Defaults to None.
        names (lst:str, optional):
            List of feature names. Defaults to None.
            The name parameter is used; if both are empty,
            then all features may be suppressed.
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
            Whether to resume any child features of the resumed feature.
            Defaults is True.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if name:
        data["name"] = name
    if names:
        data["names"] = names
    if status:
        data["status"] = status
    if type_:
        data["type"] = type_
    if clip:
        data["clip"] = clip
    if with_children:
        data["with_children"] = with_children
    return client.creoson_post("feature", "suppress", data)


def user_select_csys(client, current_file=None, max_=None):
    """Prompt the user to select one or more coordinate systems.

    and return their selections.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
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
                feat_number (int):
                    Feature Number.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if max_:
        data["max"] = max_
    return client.creoson_post("feature", "user_select_csys", data)
