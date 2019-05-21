"""Name module."""

from .core import creoson_post


def assemble(
    client,
    current_file,
    dirname=None,
    generic=None,
    into_asm=None,
    path=None,
    ref_model=None,
    transform=None,
    constraints=None,
    package_assembly=None,
    walk_children=None,
    assemble_to_root=None,
    suppress=None
):
    """Assemble a component into an assembly.

    Args:
        client (obj):
            creopyson Client.
        current_file (str):
            File name component.
        dirname (str, optional):
            Diretory name. Defaults is Creo's current working directory.
        generic (str, optional):
            Generic model name (if file name represents an instance).
            Defaults is generic model name (if file name represents an
            instance).
        into_asm (str, optional):
            Target assembly. Defaults is currently active model.
        path (list:int, optional):
            Path to a component that the new part will be constrained to.
            Defaults to None.
        ref_model (str, optional):
            Reference model that the new part will be constrained to;
            only used if path is not given.  If there are multiple of this
            model in the assembly, the component will be assembled multiple
            times, once to each occurrence. Defaults to None.
        transform (obj:JLTransform, optional):
            Transform structure for the initial position and orientation of
            the new component; only used if there are no constraints, or for
            certain constraint types. Defaults to None.
        constraints (obj_array:JLConstraint, optional):
            Assembly constraints. Defaults to None.
        package_assembly (boolean, optional):
            Whether to package the component to the assembly; only used if
            there are no constraints specified. Defaults is If there are no
            constraints, then the user will be prompted to constrain the
            component through the Creo user interface.
        walk_children (boolean, optional):
            Whether to walk into subassemblies to find reference models to
            constrain to. Defaults to None.
        assemble_to_root (boolean, optional):
            Whether to always assemble to the root assembly, or assemble to
            the subassembly containing the reference path/model.
            Defaults to None.
        suppress (boolean, optional):
            Whether to suppress the components immediately after assembling
            them. Defaults to None.

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str):
                Directory name of component.
            files (list:str):
                File name of component.
            revision (int):
                Revision of file that was opened; if more than one
                file was opened, this field is not returned.
            featureid (int):
                Last Feature ID of component after assembly.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "assemble",
        "data": {
            "file": current_file
        }
    }
    if dirname:
        request["data"]["dirname"] = dirname
    if generic:
        request["data"]["generic"] = generic
    if into_asm:
        request["data"]["into_asm"] = into_asm
    if path:
        request["data"]["path"] = path
    if ref_model:
        request["data"]["ref_model"] = ref_model
    if transform:
        request["data"]["transform"] = transform
    if constraints:
        request["data"]["constraints"] = constraints
    if package_assembly:
        request["data"]["package_assembly"] = package_assembly
    if walk_children:
        request["data"]["walk_children"] = walk_children
    if assemble_to_root:
        request["data"]["assemble_to_root"] = assemble_to_root
    if suppress:
        request["data"]["suppress"] = suppress
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def backup(client, target_dir, current_file=None):
    """Backup a model.

    Args:
        client (obj):
            creopyson Client.
        target_dir (str):
            Target directory name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns: None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "backup",
        "data": {
            "target_dir": target_dir
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def close_window(client, current_file=None):
    """Close the window containing a model.

    Args:
        client (obj):
            creopyson object.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns: None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "close_window",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def display(client, current_file, activate=None):
    """Display a model in a window.

    Args:
        client (obj):
            creopyson object.
        current_file (str):
            File name
        activate (boolean, optional):
            Activate the model after displayong. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns: None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "display",
        "data": {
            "file": current_file
        }
    }
    if activate:
        request["data"]["activate"] = activate
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def erase(client, current_file=None, files=None, erase_children=None):
    """Erase one or more models from memory.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name; only used if files is not given
            (Wildcards allowed: True). Defaults to None.
        files (list:str, optional):
            List of file names. Defaults is the file parameter is used;
            if both are empty, then all models in memory are erased.
        erase_children (boolean, optional):
            Erase children of the models too. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns: None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "erase",
    }
    if current_file:
        request["data"]["file"] = current_file
    if files:
        request["data"]["files"] = files
    if erase_children:
        request["data"]["erase_children"] = erase_children
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


# def erase_not_displayed():
#     pass


def exists(client, current_file):
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
