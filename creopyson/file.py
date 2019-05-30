"""File module."""


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
    data = {"file": current_file}
    if dirname:
        data["dirname"] = dirname
    if generic:
        data["generic"] = generic
    if into_asm:
        data["into_asm"] = into_asm
    if path:
        data["path"] = path
    if ref_model:
        data["ref_model"] = ref_model
    if transform:
        data["transform"] = transform
    if constraints:
        data["constraints"] = constraints
    if package_assembly:
        data["package_assembly"] = package_assembly
    if walk_children:
        data["walk_children"] = walk_children
    if assemble_to_root:
        data["assemble_to_root"] = assemble_to_root
    if suppress:
        data["suppress"] = suppress
    return client.creoson_post("file", "assemble", data)


def backup(client, target_dir, current_file=None):
    """Backup a model.

    Args:
        client (obj):
            creopyson Client.
        target_dir (str):
            Target directory name.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {"target_dir": target_dir}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "backup", data)


def close_window(client, current_file=None):
    """Close the window containing a model.

    Args:
        client (obj):
            creopyson object.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "close_window", data)


def display(client, current_file, activate=None):
    """Display a model in a window.

    Args:
        client (obj):
            creopyson object.
        current_file (str):
            File name
        activate (boolean, optional):
            Activate the model after displayong. Defaults is False.

    Returns:
        None

    """
    data = {"file": current_file}
    if activate:
        data["activate"] = activate
    return client.creoson_post("file", "display", data)


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

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if files:
        data["files"] = files
    if erase_children:
        data["erase_children"] = erase_children
    return client.creoson_post("file", "erase", data)


def erase_not_displayed(client):
    """Erase all non-displayed models from memory.

    Args:
        client (obj): creopyson Client.

    Returns:
        None

    """
    return client.creoson_post("file", "erase_not_displayed")


def exists(client, current_file):
    """Check whether a model exists in memory.

    Args:
        client (obj): creopyson Client.
        current_file (str): File name.

    Returns:
        (Boolean): Whether the file is open in Creo.

    """
    data = {"file": current_file}
    return client.creoson_post("file", "exists", data)["exists"]


def get_active(client):
    """Get the active model from Creo.

    Args:
        client (obj): creopyson Client.

    Returns:
        (dict):
            dirname (str): Directory name of current model.
            file (str): File name of current model.

    """
    return client.creoson_post("file", "get_active")


def get_fileinfo(client, current_file=None):
    """Open one or more files in memory or from the drive.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            dirname (str): Directory name of the file.
            file (str): File name.
            revision (int): Revision number of file.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "get_fileinfo", data)


def get_length_units(client, current_file=None):
    """Get the current length units for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (str): Length units.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "get_length_units", data)["units"]


def get_mass_units(client, current_file=None):
    """Get the current mass units for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (str): mass units.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "get_mass_units", data)["units"]


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

    Returns:
        (obj:JLTransform): The 3D transform from the assembly to
        the component's coordinate system.

    """
    data = {}
    if asm:
        data["asm"] = asm
    if path:
        data["path"] = path
    if csys:
        data["csys"] = csys
    return client.creoson_post("file", "get_transform", data)["transform"]


def has_instances(client, current_file=None):
    """Check whether a model has a family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (boolean): Whether the file has a family table.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "has_instances", data)["exists"]


def is_active(client, current_file):
    """Check whether a model is the active model.

    Args:
        client (obj): creopyson Client.
        current_file (str): File name.

    Returns:
        (boolean): Whether the file is the currently active model.

    """
    data = {"file": current_file}
    return client.creoson_post("file", "is_active", data)["active"]


def list_(client, current_file=None, files=None):
    """Get a list of files in the current Creo session that match patterns.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name; only used if files is not given. Defaults to None.
        files (list:str, optional):
            List of file names. Defaults to None.

    Returns:
        (list:str) List of files.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if files:
        data["files"] = files
    return client.creoson_post("file", "is_active", data)["files"]


def list_instances(client, current_file=None):
    """List instances in a model's family table.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            dirname (str): Directory name of the file.
            generic (str): Generic name.
            files (list:str): List of model names in the table.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "list_instances", data)


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

    Returns:
        (dict):
            rep (str): Simplified rep name.
            reps (list:str): Simplified reps names.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if rep:
        data["rep"] = rep
    return client.creoson_post("file", "list_simp_reps", data)
    # TODO return only list between `rep` and `reps`


def massprops(client, current_file=None):
    """Get mass property information about a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            volume (float): Model volume.
            mass (float): Model mass.
            density (float): Model density.
            surface_area (float): Model surface area.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "massprops", data)


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
    data = {}
    if current_file:
        data["file"] = current_file
    if dirname:
        data["dirname"] = dirname
    if files:
        data["files"] = files
    if generic:
        data["generic"] = generic
    if display:
        data["display"] = display
    if activate:
        data["activate"] = activate
    if new_window:
        data["new_window"] = new_window
    if regen_force:
        data["regen_force"] = regen_force
    return client.creoson_post("file", "open", data)
    # TODO


def open_errors(client, current_file=None):
    """Check whether Creo errors have occurred opening a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (boolean): Whether errors exist in Creo.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "open_errors", data)["errors"]


def postregen_relations_get(client, current_file=None):
    """Get post-regeneration relations for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (list:str): Exported relations text, one entry per line.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post(
        "file", "postregen_relations_get", data)["relations"]


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

    Retunrs:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if relations:
        data["relations"] = relations
    return client.creoson_post("file", "postregen_relations_set", data)


def refresh(client, current_file=None):
    """Refresh the window containing a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "refresh", data)


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

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if files:
        data["files"] = files
    if display:
        data["display"] = display
    return client.creoson_post("file", "regenerate", data)


def relations_get(client, current_file=None):
    """Get relations for a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (list:srt): Exported relations text, one entry per line.

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "relations_get", data)["relations"]


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

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if relations:
        data["relations"] = relations
    return client.creoson_post("file", "relations_set", data)


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

    Returns:
        (str): The new model name.

    """
    data = {"new_name": new_name}
    if current_file:
        data["file"] = current_file
    if onlysession:
        data["onlysession"] = onlysession
    return client.creoson_post("file", "rename", data)["file"]


def repaint(client, current_file=None):
    """Repaint the window containing a model.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    return client.creoson_post("file", "repaint", data)


def save(client, current_file=None, files=None):
    """Save one or more models.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            File name; only used if files is not given.
        files (list:str, optional):
            List of file names. Defaults: the file parameter is used.

    Returns:
        None

    """
    data = {}
    if current_file:
        data["file"] = current_file
    if files:
        data["files"] = files
    return client.creoson_post("file", "save", data)
    # TODO only one entry


def set_length_units(client, units, current_file=None, convert=None):
    """Set the current length units for a model.

    This will search the model's available Unit Systems for the first one
    which contains the given length unit.

    Args:
        client (obj):
            creopyson Client.
        units (str):
            New length units.
        current_file (str, optional):
            File name; only used if files is not given.
        convert (boolean, optional):
            Whether to convert the model's length values to the
            new units (True) or leave them the same value (False).
            Defaults is True.

    Returns:
        None

    """
    data = {"units": units}
    if current_file:
        data["file"] = current_file
    if convert:
        data["convert"] = convert
    return client.creoson_post("file", "set_length_units", data)


def set_mass_units(client, units, current_file=None, convert=None):
    """Set the mass units for a model.

    This will search the model's available Unit Systems for the first one
    which contains the given mass unit.

    Args:
        client (obj):
            creopyson Client.
        units (str):
            New mass units.
        current_file (str, optional):
            File name; only used if files is not given.
        convert (boolean, optional):
            Whether to convert the model's mass values to the
            new units (True) or leave them the same value (False).
            Defaults is True.

    Returns:
        None

    """
    data = {"units": units}
    if current_file:
        data["file"] = current_file
    if convert:
        data["convert"] = convert
    return client.creoson_post("file", "set_length_units", data)
