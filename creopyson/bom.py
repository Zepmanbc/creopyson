"""Bom module."""


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
            has_simprep (boolean):
                Whether the assembly has a Simplified Rep.

            in `children` there is the `seq_path` which indicates
            the children level, ex: `root.3.2`.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if paths:
        data["paths"] = paths
    if skeletons:
        data["skeletons"] = skeletons
    if top_level:
        data["top_level"] = top_level
    if get_transforms:
        data["get_transforms"] = get_transforms
    if exclude_inactive:
        data["exclude_inactive"] = exclude_inactive
    return client._creoson_post("bom", "get_paths", data)
