"""File module."""

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
        (dict):
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

    Returns:
        None

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
    if status:
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

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "close_window",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
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

    Returns:
        None

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
    if status:
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

    Returns:
        None

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
    if status:
        raise Warning(data)


def erase_not_displayed(client):
    """Erase all non-displayed models from memory.

    Args:
        client (obj): creopyson Client.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "erase_not_displayed",
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def exists(client, current_file):
    """Check whether a model exists in memory.

    Args:
        client (obj): creopyson Client.
        current_file (str): File name.

    Raises:
        Warning: error message from creoson.

    Returns:
        (Boolean): Whether the file is open in Creo.

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
    else:
        raise Warning(data)


def get_active(client):
    """Get the active model from Creo.

    Args:
        client (obj): creopyson Client.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            dirname (str): Directory name of current model.
            file (str): File name of current model.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "get_active",
    }
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def get_fileinfo(client, current_file=None):
    """Open one or more files in memory or from the drive.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            dirname (str): Directory name of the file.
            file (str): File name.
            revision (int): Revision number of file.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "get_fileinfo",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def get_length_units(client, current_file=None):
    """Get the current length units for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): Length units.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "get_length_units",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["units"]
    else:
        raise Warning(data)


def get_mass_units(client, current_file=None):
    """Get the current mass units for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): mass units.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "get_mass_units",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["units"]
    else:
        raise Warning(data)


def get_transform(client, asm=None, path=None, csys=None):
    """Get the 3D transform for a component in an assembly.

    Args:
        client (obj):
            creopyson Client
        asm (str, optional):
            Assembly name. Defaults is currently active model.
        path (list:int, optional):
            Path to a component in the assembly.
            Defaults is the transform is calculated for the assembly itself.
        csys (str, optional):
            Coordinate system on the component to calculate the transform for.
            Defaults is the component's default coordinate system.

    Raises:
        Warning: error message from creoson.

    Returns:
        (obj:JLTransform): The 3D transform from the assembly to
        the component's coordinate system.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "get_transform",
    }
    if asm:
        request["data"]["asm"] = asm
    if path:
        request["data"]["path"] = path
    if csys:
        request["data"]["csys"] = csys
    status, data = creoson_post(client, request)
    if not status:
        return data["transform"]
    else:
        raise Warning(data)


def has_instances(client, current_file=None):
    """Check whether a model has a family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean): Whether the file has a family table.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "has_instances",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]
    else:
        raise Warning(data)


def is_active(client, current_file):
    """Check whether a model is the active model.

    Args:
        client (obj): creopyson Client.
        current_file (str): File name.

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean): Whether the file is the currently active model.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "is_active",
        "data": {
            "file": current_file
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["active"]
    else:
        raise Warning(data)


def list_(client, current_file=None, files=None):
    """Get a list of files in the current Creo session that match patterns.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name; only used if files is not given. Defaults to None.
        files (list:str, optional):
            List of file names. Defaults to None.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str) List of files.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "is_active",
    }
    if current_file:
        request["data"]["file"] = current_file
    if files:
        request["data"]["files"] = files
    status, data = creoson_post(client, request)
    if not status:
        return data["files"]
    else:
        raise Warning(data)


def list_instances(client, current_file=None):
    """List instances in a model's family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            dirname (str): Directory name of the file.
            generic (str): Generic name.
            files (list:str): List of model names in the table.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "list_instances",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def list_simp_reps(client, current_file=None, rep=None):
    """List simplified reps in a model.

    Args:
        client (obj):
            creopyson Client
        current_file (str, optional):
            File name. Defaults is currently active model.
        rep (str, optional):
            Simplified rep name pattern (wildcards_allowed: True).
            Defaults is all simplified reps.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            rep (str): Simplified rep name.
            reps (list:str): Simplified reps names.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "list_simp_reps",
    }
    if current_file:
        request["data"]["file"] = current_file
    if rep:
        request["data"]["rep"] = rep
    status, data = creoson_post(client, request)
    if not status:
        return data
        # TODO return only list between `rep` and `reps`
    else:
        raise Warning(data)


def massprops(client, current_file=None):
    """Get mass property information about a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            volume (float): Model volume.
            mass (float): Model mass.
            density (float): Model density.
            surface_area (float): Model surface area.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "massprops",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def open_(
    client,
    current_file=None,
    dirname=None,
    files=None,
    generic=None,
    display=None,
    activate=None,
    new_window=None,
    regen_force=None
):
    """Open one or more files in memory or from the drive.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name; only used if files is not given. Defaults to None.
        dirname (str, optional):
            Directory name. Defaults is Creo's current working directory.
        files (list:str, optional):
            List of file names. Defaults: the file parameter is used.
        generic (str, optional):
            Generic model name (if file name represents an instance).
            Defaults to None.
        display (boolean, optional):
            Display the model after opening. Defaults is False.
        activate (boolean, optional):
            Activate the model after opening. Defaults is False.
        new_window (boolean, optional):
            Open model in a new window. Defaults is False.
        regen_force (boolean, optional):
            Force regeneration after opening. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        (dict):
            dirname (str):
                Directory name of opened file(s).
            files (list:str):
                File names that were opened.
            revision (int):
                Revision of file that was opened;
                if more than one file was opened, this field is not returned.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "open",
    }
    if current_file:
        request["data"]["file"] = current_file
    if dirname:
        request["data"]["dirname"] = dirname
    if files:
        request["data"]["files"] = files
    if generic:
        request["data"]["generic"] = generic
    if display:
        request["data"]["display"] = display
    if activate:
        request["data"]["activate"] = activate
    if new_window:
        request["data"]["new_window"] = new_window
    if regen_force:
        request["data"]["regen_force"] = regen_force
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def open_errors(client, current_file=None):
    """Check whether Creo errors have occurred opening a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (boolean): Whether errors exist in Creo.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "open_errors",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["errors"]
    else:
        raise Warning(data)


def postregen_relations_get(client, current_file=None):
    """Get post-regeneration relations for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:str): Exported relations text, one entry per line.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "postregen_relations_get",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["relations"]
    else:
        raise Warning(data)


def postregen_relations_set(client, current_file=None, relations=None):
    """Set post-regeneration relations for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.
        relations (list:str, optional):
            Relations text to import, one line per entry.
            Clear the relations if missing.

    Raises:
        Warning: error message from creoson.

    Retunrs:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "postregen_relations_set",
    }
    if current_file:
        request["data"]["file"] = current_file
    if relations:
        request["data"]["relations"] = relations
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def refresh(client, current_file=None):
    """Refresh the window containing a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "refresh",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def regenerate(client, current_file=None, files=None, display=None):
    """Regenerate one or more models.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.
        files (list:str, optional):
            List of file names. Defaults: the file parameter is used.
        display (boolean, optional):
            Display the model before regenerating. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "regenerate",
    }
    if current_file:
        request["data"]["file"] = current_file
    if files:
        request["data"]["files"] = files
    if display:
        request["data"]["display"] = display
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def relations_get(client, current_file=None):
    """Get relations for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        (list:srt): Exported relations text, one entry per line.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "relations_get",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data["relations"]
    else:
        raise Warning(data)


def relations_set(client, current_file=None, relations=None):
    """Set relations for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.
        relations (list:str, optional):
            Relations text to import, one line per entry.
            Clear the relations if missing.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "relations_set",
    }
    if current_file:
        request["data"]["file"] = current_file
    if relations:
        request["data"]["relations"] = relations
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def rename(client, new_name, current_file=None, onlysession=None):
    """Rename a model.

    Args:
        client (obj):
            creopyson Client.
        new_name (str):
            New file name.
        current_file (str, optional):
            File name. Defaults is currently active model.
        onlysession (boolean, optional):
            Modify only in memory, not on disk. Defaults is False.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): The new model name.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "rename",
        "data": {
            "new_name": new_name,
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if onlysession:
        request["data"]["onlysession"] = onlysession
    status, data = creoson_post(client, request)
    if not status:
        return data["file"]
    else:
        raise Warning(data)


def repaint(client, current_file=None):
    """Repaint the window containing a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "file",
        "function": "repaint",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


# def save():
#     pass


# def set_length_units():
#     pass


# def set_mass_units():
#     pass
