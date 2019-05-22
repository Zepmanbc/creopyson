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


# def delete_param():
#     pass


# def list():
#     pass


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
