"""View module."""


def activate(client, name, file_=None):
    """Activate a model view.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            View name.
        `file_` (str, optional):
            Model name. Defaults is current active model.

    Returns:
        None

    """
    data = {"name": name}
    if file_:
        data["file"] = file_
    return client._creoson_post("view", "activate", data)


def list_exploded(client, file_=None, name=None):
    """List views that match criteria and are exploded.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            View name (wildcards allowed: True).
            Defaults is None: all views are listed.

    Returns:
        (list:str): List of view names.

    """
    data = {"name": name}
    if file_:
        data["file"] = file_
    return client._creoson_post("view", "list_exploded", data, "viewlist")


def list_(client, file_=None, name=None):
    """List views that match criteria.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        name (str, optional):
            View name (wildcards allowed: True).
            Defaults is None: all views are listed.

    Returns:
        (list:str): List of view names.

    """
    data = {"name": name}
    if file_:
        data["file"] = file_
    return client._creoson_post("view", "list", data, "viewlist")
    # TODO: group with list_exploded?


def save(client, name, file_=None):
    """Save a model's current orientation as a new view.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            View name.
        `file_` (str, optional):
            Model name. Defaults is current active model.

    Returns:
        None

    """
    data = {"name": name}
    if file_:
        data["file"] = file_
    return client._creoson_post("view", "save", data)
