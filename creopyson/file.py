"""Name module."""

from .core import creoson_post


# def assemble():
#     pass


# def backup():
#     pass


# def close_window():
#     pass


# def display():
#     pass


# def erase():
#     pass


# def erase_not_displayed():
#     pass


def exists(client, current_file):
    """Test if file exists in Workdirectory.

    Args:
        client (obj): creopyson Client
        current_file (str): path to file

    Returns:
        Boolean: True if exists, False if not

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "exists",
        "data": {
            "file": current_file
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]


# def get_active():
#     pass


# def get_fileinfo():
#     pass


# def get_length_units():
#     pass


# def get_mass_units():
#     pass


# def get_transform():
#     pass


# def has_instances():
#     pass


# def is_active():
#     pass


# def list_():
#     pass


# def list_instances():
#     pass


# def list_simp_reps():
#     pass


# def massprops():
#     pass


def open_(client, query, dirname=None, generic=None, display=True,
          activate=True, new_window=False, regen_force=False):
    """Open files in Creo.

    Opening a single file: client.file_open("my_file.prt")
    Opening all drawings

    Args:
        client (obj): creopyson Client.
            query (list|string): file name or search with `*`.
            ex: `foo_*.prt` or `*.drw`
        dirname (string): Directory name
            (default: Creo's current working directory)
        generic (string):
            generic model name (if file name represents an instance).
        display (boolean):
            display the model after opening. (default True)
        activate (boolean):
            activate the model after opening (default True)
        new_window (boolean):
            open model in a new window (default False)
        regen_force (boolean):
            force regeneration after opening (default False)

    Returns:
        dict:
            "dirname" (string):
                Directory name of opened file(s).
            "files" (list|string):
                File names that were opened.
            "revision" (integer):
                Revision of file that was opened;
                if more than one file was opened, this field is not returned.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "open",
        "data": {
            "display": display,
            "activate": activate,
            "new_window": new_window,
            "regen_force": regen_force,
        }
    }
    if type(query) is list:
        request["data"]["files"] = query
    else:
        request["data"]["file"] = query
    if dirname:
        request["data"]["dirname"] = dirname
    if generic:
        request["data"]["generic"] = generic
    status, data = creoson_post(client, request)
    if not status:
        return data


# def open_errors():
#     pass


# def postregen_relations_get():
#     pass


# def postregen_relations_set():
#     pass


# def refresh():
#     pass


def regenerate(client, *args):
    """Regenerate Creo model.

    Args:
        client (obj): creopyson Client

    Raises:
        Error: [description]
        error: [description]

    Returns:
        Boolean: error status

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "regenerate",
        "data": {
            "file": args,
            "display": True
        }
    }
    if len(args) == 1:
        request["data"]["file"] = args[0]
    elif len(args) > 1:
        request["data"]["files"] = list(args)
    else:
        print("raise Error")
    status, data = creoson_post(client, request)
    return status
    # TODO: raise error


# def relations_get():
#     pass


# def relations_set():
#     pass


# def rename():
#     pass


# def repaint():
#     pass


# def save():
#     pass


# def set_length_units():
#     pass


# def set_mass_units():
#     pass
