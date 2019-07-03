"""Creo module."""
from creopyson.exceptions import MissingKey


def cd(client, dirname):
    r"""Change Creo's working directory.

    You can use absolute path or relative:
    "C:\\My Workdir\\"
    "..\\Other_directory\\"

    Args:
        client (obj): creopyson Client.
        dirname (str): New directory name.

    Returns:
        (str): Name of new working directory.

    """
    data = {"dirname": dirname}
    return client._creoson_post("creo", "cd", data, "dirname")


def delete_files(client, filename=None, dirname=None):
    """Delete files from a directory working directory.

    Args:
        client (obj):
            creopyson Client.
        filename (str or list:str, optional):
            File name filter or list of file names.
            if blank all files will be deleted.
            (wildcards_allowed: True). Defaults to None.
        dirname (str, optional):
            Directory name. Defaults is Creo's current working directory.

    Returns:
        (list:str): List of deleted files.

    """
    data = {}
    if filename:
        if isinstance(filename, (list)):
            data["filenames"] = filename
        else:
            data["filename"] = str(filename)
    if dirname:
        data["dirname"] = dirname
    return client._creoson_post("creo", "delete_files", data, "filelist")


def get_config(client, name):
    """Get the value of a Creo config option.

    Args:
        client (obj): creopyson Client.
        name (str): Option name.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str):
            List of option values (some options can have multiple values).

    """
    data = {"name": name}
    return client._creoson_post("creo", "get_config", data, "values")


def get_std_color(client, color_type):
    """Get one of Creo's standard colors.

    Args:
        client (obj):
            creopyson Client.
        color_type (str):
            Color type.
            Valid values: letter, highlight, drawing, background, half_tone,
            edge_highlight, dimmed, error, warning, sheetmetal, curve,
            presel_highlight, selected, secondary_selected, preview,
            secondary_preview, datum, quilt.

    Returns:
        (dict):
            red (int): Red value (0-255)
            green (int): Green value (0-255)
            blue (int): Blue value (0-255)

    """
    data = {"color_type": color_type}
    return client._creoson_post("creo", "get_std_color", data)


def list_dirs(client, dirname=None):
    """List subdirectories of Creo's current working directory.

    Args:
        client (obj):
            creoopyson Client.
        dirname (str, optional):
            Directory name filter (wildcards_allowed: True).
            Defaults: All subdirectories are listed.

    Returns:
        (list:str): List of subdirectories

    """
    data = {"dirname": "*"}
    if dirname:
        data["dirname"] = dirname
    try:
        result = client._creoson_post("creo", "list_dirs", data, "dirlist")
    except MissingKey:
        result = []
    return result


def list_files(client, filename=None):
    """List files in Creo's current working directory.

    Args:
        client (obj):
            creopyson Client.
        filename (str, optional):
            File name filter (wildcards_allowed: True).
            Defaults: all files are listed.

    Returns:
        (list:int): List of files.

    """
    data = {"filename": "*"}
    if filename:
        data["filename"] = filename
    return client._creoson_post("creo", "list_files", data, "filelist")


def mkdir(client, dirname):
    """Create a new directory.

    Args:
        client (obj): creopyson Client.
        dirname (str): New directory name.

    Returns:
        (str): Full name of new working directory.

    """
    data = {"dirname": dirname}
    return client._creoson_post("creo", "mkdir", data, "dirname")


def pwd(client):
    """Return Creo's current working directory.

    Args:
        client (obj): creopyson Client.

    Returns:
        (str): Full name of working directory.

    """
    return client._creoson_post("creo", "pwd", key_data="dirname")


def rmdir(client, dirname):
    """Delete a directory.

    Args:
        client (obj): creopyson Client.
        dirname (str): Directory name to delete.

    Returns:
        None.

    """
    data = {"dirname": dirname}
    return client._creoson_post("creo", "rmdir", data)


def set_config(client, name, value, ignore_errors=None):
    """Set a Creo config option.

    Args:
        client (obj):
            creopyson Client.
        name (str):
            Option name.
        value (str):
            New option value.
        ignore_errors (boolean, optional):
            Whether to ignore errors that might occur when setting the config
            option. Defaults is False.

    Returns:
        None.

    """
    data = {
        "name": name,
        "value": value,
        "ignore_errors": False
    }
    if ignore_errors:
        data["ignore_errors"] = ignore_errors
    return client._creoson_post("creo", "set_config", data)


def set_std_color(client, color_type, red, green, blue):
    """Set one of Creo's standard colors.

    Args:
        client (obj):
            creopyson Client.
        color_type (str):
            Color type.
            Valid values: letter, highlight, drawing, background, half_tone,
            edge_highlight, dimmed, error, warning, sheetmetal, curve,
            presel_highlight, selected, secondary_selected, preview,
            secondary_preview, datum, quilt.
        red (int):
            Red value (0-255).
        green (int):
            Green value (0-255).
        blue (int):
            Blue value (0-255).

    Returns:
        None.

    """
    data = {
        "color_type": color_type,
        "red": red,
        "green": green,
        "blue": blue
    }
    return client._creoson_post("creo", "rmdir", data)
    # TODO: convert RGB to a tuple or hexa color?
