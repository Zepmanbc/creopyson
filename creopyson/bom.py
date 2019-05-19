from .core import creoson_post


def get_paths(client, current_asm=None, paths=False, skeletons=False,
              top_level=False, get_transforms=False, exclude_inactive=False):
    """Get a hierarchy of components within an assembly.

    Even if you do not set exclude_inactive to true, the function will still
    exclude any components with a status of INACTIVE or UNREGENERATED.

    Args:
        current_asm (string): file name, if not set, active model is used.
        paths (Boolean): Whether to return component paths for each component
            (default" : False)
        skeletons (Boolean): Whether to include skeleton components
            (default" : False)
        top_level (Boolean): Whether to return only the top-level components
            in the assembly. (default" : False)
        get_transforms (Boolean): Whether to return the 3D transform matrix
            for each component. (default" : False)
        exclude_inactive (Boolean): Whether to exclude components which do not
            have an ACTIVE status. (default" : False)

    Returns: dict
        file (string): Assembly file name
        generic (string): Generic name for the assembly
        children (object:BomChild): The hierarchy of component data, starting
            with the top-level assembly.
        in `children` there is the `seq_path` which indicates
        the children level, ex: "root.3.2"
    """
    request = {
        "sessionId": client.sessionId,
        "command": "bom",
        "function": "get_paths",
        "data": {
            "paths": paths,
            "skeletons": skeletons,
            "top_level": top_level,
            "get_transforms": get_transforms,
            "exclude_inactive": exclude_inactive,
        }
    }
    if current_asm:
        request["data"]["file"] = current_asm
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise TypeError(data)
