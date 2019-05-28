"""Bom module."""
from .core import creoson_post


def get_paths(
    client,
    file_=None,
    paths=None,
    skeletons=None,
    top_level=None,
    get_transforms=None,
    exclude_inactive=None
):
    """Get a hierarchy of components within an assembly.

    Even if you do not set exclude_inactive to true, the function will still
    exclude any components with a status of INACTIVE or UNREGENERATED.

    Args:
        client (obj):
            creopyson Client.
        `file_` (string, optional):
            file name, if not set, active model is used.
        paths (boolean, optional):
            Whether to return component paths for each component
            (default" : False)
        skeletons (boolean, optional):
            Whether to include skeleton components
            (default" : False)
        top_level (boolean, optional):
            Whether to return only the top-level components
            in the assembly. (default" : False)
        get_transforms (boolean, optional):
            Whether to return the 3D transform matrix
            for each component. (default" : False)
        exclude_inactive (boolean, optional):
            Whether to exclude components which do not
            have an ACTIVE status. (default" : False)

    Returns:
        Dict:
            file (string):
                Assembly file name
            generic (string):
                Generic name for the assembly
            children (object:BomChild):
                The hierarchy of component data,
                starting with the top-level assembly.

            in `children` there is the `seq_path` which indicates
            the children level, ex: `root.3.2`.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "bom",
        "function": "get_paths",
        "data": {}
    }
    if file_:
        request["data"]["file"] = file_
    if paths:
        request["data"]["paths"] = paths
    if skeletons:
        request["data"]["skeletons"] = skeletons
    if top_level:
        request["data"]["top_level"] = top_level
    if get_transforms:
        request["data"]["get_transforms"] = get_transforms
    if exclude_inactive:
        request["data"]["exclude_inactive"] = exclude_inactive
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)
