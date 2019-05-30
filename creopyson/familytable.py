"""Familytable module."""


def add_inst(client, instance, current_file=None):
    """Add a new instance to a family table.

    Creates a family table if one does not exist.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            New instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {"instance": instance}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "add_inst", data)


def create_inst(client, instance, current_file=None):
    """Create a new model from a family table row.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (str): New model name.

    """
    data = {"instance": instance}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "create_inst", data)["name"]


def delete_inst(client, instance, current_file=None):
    """Delete an instance from a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {"instance": instance}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "delete_inst", data)


def delete(client, current_file=None):
    """Delete an entire family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name (wildcards allowed: True).
            Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "delete", data)


def exists(client, instance, current_file=None):
    """Check whether an instance exists in a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (boolean):
            Whether the instance exists in the model's family table;
            returns false if there is no family table in the model.

    """
    data = {"instance": instance}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "exists", data)["exists"]


def get_cell(client, instance, colid, current_file=None):
    """Get one cell of a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            Instance name.
        colid (str):
            Colimn ID.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            instance (str):
                Family Table instance name.
            colid (str):
                Column ID.
            value (depends on datatype):
                Cell value.
            datatype (str):
                Data type.
            coltype (str):
                Column Type; a string corresponding to the Creo column type.

    """
    data = {
        "instance": instance,
        "colid": colid
    }
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "get_cell", data)


def get_header(client, current_file=None):
    """Get the header of a family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name.
            Defaults is currently active model.

    Returns:
        (list:dict):
            colid (str):
                Column ID.
            value (depends on date type):
                Cell value.
            datatype (str):
                Data type. Valid values: STRING, DOUBLE, INTEGER, BOOL, NOTE.
            coltype (str):
                Column Type; a string corresponding to the Creo column type.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "get_header", data)["columns"]


def get_parents(client, current_file=None):
    """Get the parent instances of a model in a nested family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name.
            Defaults is currently active model.

    Returns:
        (list:str):
            List of parent instance names, starting with
            the immediate parent and working back.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "get_parents", data)["parents"]


def get_row(client, instance, current_file=None):
    """Get one row of a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            Instance name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            colid (str):
                Column ID.
            value (depends on datatype):
                Cell value.
            datatype (str):
                Data type.
            coltype (str):
                Column Type; a string corresponding to the Creo column type.

    """
    data = {"instance": instance}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "get_row", data)["columns"]


def list_(client, current_file=None, instance=None):
    """List the instance names in a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (str, optional):
            Instance name filter (wildcards allowed: True).
            Defaults is all instances.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (list:str): List of matching instance names

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if instance:
        data["instance"] = instance
    return client.creoson_post("familytable", "list", data)["instances"]


def list_tree(client, current_file=None, erase=None):
    """Get a hierarchical structure of a nested family table.

    Args:
        client (obj):
            creopyson Client.
        erase (boolean, optional):
            Erase model and non-displayed models afterwards.
            Defaults is `False`.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (list:str):
            List of child instances
                total (int):
                    Count of all child instances including their decendants.
                children (list:dict):
                    name (str):
                        Name of the family table instance.
                    total (int):
                        Count of all child instances including their
                        decendants.
                    children (list:dict):
                        List of child instances.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if erase:
        data["erase"] = erase
    return client.creoson_post("familytable", "list_tree", data)["instances"]


def replace(
    client,
    cur_model,
    new_inst,
    current_file=None,
    cur_inst=None,
    path=None
):
    """Replace a model in an assembly with another inst in the same family table.

    You must specify either cur_inst or path.

    Args:
        client (obj):
            creopyson Client.
        cur_model (str):
            Generic model containing the instances.
        new_inst (str):
            New instance name.
        current_file (str, optional):
            File name (usually an assembly).
            Defaults is currently active model.
        cur_inst (str):
            Instance name to replace. Defaults to None.
        path (list:int, optional):
            Path to component to replace. Defaults to None.

    Returns:
        None

    """
    data = {
        "cur_model": cur_model,
        "new_inst": new_inst,
    }
    if current_file:
        data["file"] = current_file
    if cur_inst:
        data["cur_inst"] = cur_inst
    if path:
        data["path"] = path
    return client.creoson_post("familytable", "replace", data)
    # TODO: path/cur_inst


def set_cell(client, instance, colid, value, current_file=None):
    """Set the value of one cell of a family table.

    Args:
        client (obj):
            creopyson Client.
        instance (str):
            Family Table instance name.
        colid (str):
            Column ID.
        value (depends on data type):
            Cell value.
        current_file (str, optional):
            File name (usually an assembly).
            Defaults is currently active model.

    Returns:
        None

    """
    data = {
        "instance": instance,
        "colid": colid,
        "value": value,
    }
    if current_file:
        data["file"] = current_file
    return client.creoson_post("familytable", "set_cell", data)
