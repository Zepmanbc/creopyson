"""Name module."""

from .core import creoson_post


def cd(client, dirname):
    """Change Creo's working directory.

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


def delete_files(client, dirname=None, filename=None, filenames=None):
    """Delete files from a directory working directory.

    Args:
        client (obj):
            creopyson Client.
        dirname (str, optional):
            Directory name. Defaults is Creo's current working directory.
        filename (str, optional):
            File name filter; only used if filenames is not give
            (wildcards_allowed: True). Defaults to None.
        filenames (list:str, optional):
            List of file names. Defaults to None.
            The filename parameter is used; if both are blank,
            all files will be deleted.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str): List of deleted files.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "dele_files",
    }
    if dirname:
        request["data"]["dirname"] = dirname
    if filename:
        request["data"]["filename"] = filename
    if filenames:
        request["data"]["filenames"] = filenames
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
        "function": "dele_files",
    }
    if dirname:
        request["data"]["dirname"] = dirname
    status, data = creoson_post(client, request)
    if not status:
        return data["dirlist"]
    else:
        raise Warning(data)


def list_files(client, query='*prt|*drw|*asm'):
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "list_files",
        "data": {
            "filename": query
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data['filelist']


# def mkdir():
#     pass


def pwd(client):
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "pwd"
    }
    status, data = creoson_post(client, request)
    if not status:
        return data['dirname']


# def rmdir():
#     pass


# def set_config():
#     pass


# def set_std_color():
#     pass
