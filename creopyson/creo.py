"""Name module."""

from .core import creoson_post


def cd(client, dirname):
    r"""Change Creo's working directory.

    You can use absolute path or relative:
    "C:\\My Workdir\\"
    "..\\Other_directory\\"

    Args:
        client (obj): creopyson Client.
        dirname (str): New directory name.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): Name of new working directory.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "cd",
        "data": {
            "dirname": dirname
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["dirname"]
    else:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str): List of deleted files.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "delete_files",
        "data": {}
    }
    if filename:
        if isinstance(filename, (list)):
            request["data"]["filenames"] = filename
        else:
            request["data"]["filename"] = str(filename)
    if dirname:
        request["data"]["dirname"] = dirname
    status, data = creoson_post(client, request)
    if not status:
        return data["filelist"]
    else:
        raise Warning(data)


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
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "get_config",
        "data": {
            "name": name
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["values"]
    else:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            red (int): Red value (0-255)
            green (int): Green value (0-255)
            blue (int): Blue value (0-255)

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "get_std_color",
        "data": {
            "color_type": color_type
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def list_dirs(client, dirname=None):
    """List subdirectories of Creo's current working directory.

    Args:
        client (obj):
            creoopyson Client.
        dirname (str, optional):
            Directory name filter (wildcards_allowed: True).
            Defaults: All subdirectories are listed.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict:str): List of subdirectories

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "list_dirs",
        "data": {
            "dirname": "*"
        }
    }
    if dirname:
        request["data"]["dirname"] = dirname
    status, data = creoson_post(client, request)
    if not status:
        return data["dirlist"]
    else:
        raise Warning(data)


def list_files(client, filename=None):
    """List files in Creo's current working directory.

    Args:
        client (obj):
            creopyson Client.
        filename (str, optional):
            File name filter (wildcards_allowed: True).
            Defaults: all files are listed.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:int): List of files.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "list_files",
        "data": {
            "filename": "*"
        }
    }
    if filename:
        request["data"]["filename"] = filename
    status, data = creoson_post(client, request)
    if not status:
        return data["filelist"]
    else:
        raise Warning(data)


def mkdir(client, dirname):
    """Create a new directory.

    Args:
        client (obj): creopyson Client.
        dirname (str): New directory name.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): Full name of new working directory.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "mkdir",
        "data": {
            "dirname": dirname
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["dirname"]
    else:
        raise Warning(data)


def pwd(client):
    """Return Creo's current working directory.

    Args:
        client (obj): creopyson Client.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): Full name of working directory.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "pwd"
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["dirname"]
    else:
        raise Warning(data)


def rmdir(client, dirname):
    """Delete a directory.

    Args:
        client (obj): creopyson Client.
        dirname (str): Directory name to delete.

    Raises:
        Warning: error message from creoson.

    Returns:
        None.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "rmdir",
        "data": {
            "dirname": dirname
        }
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        None.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "set_config",
        "data": {
            "name": name,
            "value": value,
            "ignore_errors": False
        }
    }
    if ignore_errors:
        request["data"]["ignore_errors"] = ignore_errors
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        None.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "rmdir",
        "data": {
            "color_type": color_type,
            "red": red,
            "green": green,
            "blue": blue
        }
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)
    # TODO: convert RGB to a tuple or hexa color?
