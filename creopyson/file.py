"""File module."""


def assemble(
    client,
    file_,
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
    suppress=None,
):
    """Assemble a component into an assembly.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str):
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
        package_assembly (bool, optional):
            Whether to package the component to the assembly; only used if
            there are no constraints specified. Defaults is If there are no
            constraints, then the user will be prompted to constrain the
            component through the Creo user interface.
        walk_children (bool, optional):
            Whether to walk into subassemblies to find reference models to
            constrain to. Defaults to None.
        assemble_to_root (bool, optional):
            Whether to always assemble to the root assembly, or assemble to
            the subassembly containing the reference path/model.
            Defaults to None.
        suppress (bool, optional):
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
    data = {"file": file_}
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
    return client._creoson_post("file", "assemble", data)


def backup(client, target_dir, file_=None):
    """Backup a model.

    Args:
        client (obj):
            creopyson Client.
        target_dir (str):
            Target directory name.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {"target_dir": target_dir}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "backup", data)


def close_window(client, file_=None):
    """Close the window containing a model.

    Args:
        client (obj):
            creopyson object.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "close_window", data)


def delete_material(client, material, file_=None):
    """Delete a material from a part.

    Args:
        client (obj):
            creopyson object
        material (str):
            Material name.
        `file_` (str, optional):
            File name.
            (Wildcards allowed: True).
            Defaults is currently active model.

    """
    data = {
        "material": material,
    }
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "delete_material", data)


def display(client, file_, activate=None):
    """Display a model in a window.

    Args:
        client (obj):
            creopyson object.
        `file_` (str):
            File name
        activate (bool, optional):
            Activate the model after displaying. Defaults is True.

    Returns:
        None

    """
    data = {"file": file_, "activate": True}
    if activate is not None:
        data["activate"] = activate
    return client._creoson_post("file", "display", data)


def erase(client, file_=None, erase_children=None):
    """Erase one or more models from memory.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str|list:str, optional):
            File name or List of file names;
            (Wildcards allowed: True).
            if empty all models in memory are erased.
        erase_children (bool, optional):
            Erase children of the models too. Defaults is False.

    Returns:
        None

    """
    data = {}
    if file_:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    if erase_children:
        data["erase_children"] = erase_children
    return client._creoson_post("file", "erase", data)


def erase_not_displayed(client):
    """Erase all non-displayed models from memory.

    Args:
        client (obj): creopyson Client.

    Returns:
        None

    """
    return client._creoson_post("file", "erase_not_displayed")


def exists(client, file_):
    """Check whether a model exists in memory.

    Args:
        client (obj): creopyson Client.
        `file_` (str): File name.

    Returns:
        (bool): Whether the file is open in Creo.

    """
    data = {"file": file_}
    return client._creoson_post("file", "exists", data, "exists")


def get_accuracy(client, file_=None):
    """Get a solid's accuracy.

    If the model has no accuracy value, this function will return null.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name.
            Defaults is current active model

    Returns:
        (list):
            accuracy (float):
                Accuracy value.
            relative (bool):
                True = relative; False = absolute accuracy.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "get_accuracy", data)


def get_active(client):
    """Get the active model from Creo.

    Args:
        client (obj): creopyson Client.

    Returns:
        (dict):
            dirname (str): Directory name of current model.
            file (str): File name of current model.

    """
    return client._creoson_post("file", "get_active")


def get_cur_material(client, file_=None):
    """Get the current material for a part.

    Note: This is the same as 'get_cur_material_wildcard' but this function
    does not allow wildcards on the part name. They are separate functions
    because the return structures are different. This function is retained
    for backwards compatibility.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Part name. Defaults to None is current active model.

    Returns:
        str:
            Current material for the part, may be null if there is no
            current material.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "get_cur_material", data, "material")


def get_cur_material_wildcard(client, file_=None, include_non_matching_parts=False):
    """Get the current material for a part or parts.

    Note: This is the same as 'get_cur_material' but this function allows
    wildcards on the part name. They are separate functions because the return
    structures are different.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Part name. Defaults to None is current active model.
        include_non_matching_parts (bool, optionnal):
            Whether to include parts that match the part name pattern but don't
            have a current material.
            Defaults to False.

    Returns:
        list:
            A list of part and current-material pairs.
    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if include_non_matching_parts:
        data["include_non_matching_parts"] = True
    return client._creoson_post("file", "get_cur_material_wildcard", data, "materials")


def get_fileinfo(client, file_=None):
    """Open one or more files in memory or from the drive.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            dirname (str):
                Directory name of the file.
            file (str):
                File name.
            revision (int):
                Revision number of file.
                (Not availlable if the file is in Windchill)

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "get_fileinfo", data)


def get_length_units(client, file_=None):
    """Get the current length units for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (str): Length units.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "get_length_units", data, "units")


def get_mass_units(client, file_=None):
    """Get the current mass units for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (str): mass units.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "get_mass_units", data, "units")


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
    return client._creoson_post("file", "get_transform", data)


def has_instances(client, file_=None):
    """Check whether a model has a family table.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (bool): Whether the file has a family table.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "has_instances", data, "exists")


def is_active(client, file_):
    """Check whether a model is the active model.

    Args:
        client (obj): creopyson Client.
        `file_` (str): File name.

    Returns:
        (bool): Whether the file is the currently active model.

    """
    data = {"file": file_}
    return client._creoson_post("file", "is_active", data, "active")


def list_(client, file_=None):
    """Get a list of files in the current Creo session that match patterns.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str|list:str, optional):
            File name or List of file names;

    Returns:
        (list:str) List of files.

    """
    data = {}
    if file_:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    return client._creoson_post("file", "list", data, "files")


def list_instances(client, file_=None):
    """List instances in a model's family table.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            dirname (str): Directory name of the file.
            generic (str): Generic name.
            files (list:str): List of model names in the table.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "list_instances", data)


def list_materials(client, file_=None, material=None):
    """List materials on a part.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.
        material (str, optional):
            Material name pattern.
            Wildcards allowed.
            Defaults to None is all materials.

    Returns:
        list: List of materials in the part.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if material:
        data["material"] = material
    return client._creoson_post("file", "list_materials", data, "materials")


def list_materials_wildcard(
    client, file_=None, material=None, include_non_matching_parts=False
):
    """List materials on a part or parts.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.
        material (str, optional):
            Material name pattern.
            Wildcards allowed.
            Defaults to None is all materials.
        include_non_matching_parts (bool, optional):
            Whether to include parts that match the part name pattern but
            don't have any materials matching the material pattern.
            Defaults to False.

    Returns:
        list:
            A list of part and material pairs. If a part has more than one
            material, it will have multiple entries in this array.
    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if material:
        data["material"] = material
    if include_non_matching_parts:
        data["include_non_matching_parts"] = True
    return client._creoson_post("file", "list_materials_wildcard", data, "materials")


def list_simp_reps(client, file_=None, rep=None):
    """List simplified reps in a model.

    Args:
        client (obj):
            creopyson Client
        `file_` (str, optional):
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
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if rep:
        data["rep"] = rep
    return client._creoson_post("file", "list_simp_reps", data)


def load_material_file(client, material, dirname=None, file_=None):
    """Load a new material file into a part or parts.

    Note: If 'material' has a file extension, it will be removed before
    the material is loaded.

    Args:
        client (obj):
            creopyson Client
        material (str):
            Material name
        dirname (str, optional):
            Directory name containing the material file.
            Default is Creo's 'pro_material_dir' config setting,
            or search path, or current working directory
        `file_` (str, optional):
            File name.
            Wildcards allowed.
            Defaults is currently active model.

    Returns:
        list:
            List of files impacted.

    """
    data = {"dirname": dirname, "material": material}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "load_material_file", data, "files")


def massprops(client, file_=None):
    """Get mass property information about a model.

    Notes: PTC's description of coord_sys_inertia:
    "The inertia matrix with respect to coordinate frame:(element ij is
    the integral of x_i x_j over the object)".
    PTC's description of coord_sys_inertia_tensor:
    "The inertia tensor with respect to coordinate frame:
    CoordSysInertiaTensor =
    trace(CoordSysInertia) * identity - CoordSysInertia".

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (dict):
            volume (float):
                Model volume.
            mass (float):
                Model mass.
            density (float):
                Model density.
            surface_area (float):
                Model surface area.
            ctr_grav_inertia_tensor (object:JLInertia):
                Model's Inertia Tensor translated to center of gravity.
            coord_sys_inertia (object:JLInertia):
                Model's Inertia Matrix with respect to the coordinate frame.
            coord_sys_inertia_tensor (object:JLInertia):
                Model's Inertia Tensor with respect to the coordinate frame.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "massprops", data)


def open_(
    client,
    file_,
    dirname=None,
    generic=None,
    display=None,
    activate=None,
    new_window=None,
    regen_force=None,
):
    """Open one or more files in memory or from the drive.

    note: if you open more than one file, it will only put file in your session
    you won't be able to display more than one file at once.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str|list:str):
            File name or List of file names;
        dirname (str, optional):
            Directory name. Defaults is Creo's current working directory.
        generic (str, optional):
            Generic model name (if file name represents an instance).
            Defaults to None.
        display (bool, optional):
            Display the model after opening. Defaults is True.
        activate (bool, optional):
            Activate the model after opening. Defaults is True.
        new_window (bool, optional):
            Open model in a new window. Defaults is False.
        regen_force (bool, optional):
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
    data = {
        "display": True,
        "activate": True,
    }
    if file_:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    if dirname:
        data["dirname"] = dirname
    if generic:
        data["generic"] = generic
    if display is not None:
        data["display"] = display
    if activate is not None:
        data["activate"] = activate
    if new_window:
        data["new_window"] = new_window
    if regen_force:
        data["regen_force"] = regen_force
    return client._creoson_post("file", "open", data)
    # TODO


def open_errors(client, file_=None):
    """Check whether Creo errors have occurred opening a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (bool): Whether errors exist in Creo.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "open_errors", data, "errors")


def postregen_relations_get(client, file_=None):
    """Get post-regeneration relations for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (list:str): Exported relations text, one entry per line.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "postregen_relations_get", data, "relations")


def postregen_relations_set(client, file_=None, relations=None):
    """Set post-regeneration relations for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.
        relations (list:str, optional):
            Relations text to import, one line per entry.
            Clear the relations if missing.

    Retunrs:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if relations:
        data["relations"] = relations
    return client._creoson_post("file", "postregen_relations_set", data)


def refresh(client, file_=None):
    """Refresh the window containing a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "refresh", data)


def regenerate(client, file_=None, display=None):
    """Regenerate one or more models.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str|list:str, optional):
            File name or List of file names;
            Defaults is currently active model
        display (bool, optional):
            Display the model before regenerating. Defaults is False.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if display:
        data["display"] = display
    return client._creoson_post("file", "regenerate", data)


def relations_get(client, file_=None):
    """Get relations for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        (list:srt): Exported relations text, one entry per line.

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "relations_get", data, "relations")


def relations_set(client, file_=None, relations=None):
    """Set relations for a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.
        relations (list:str, optional):
            Relations text to import, one line per entry.
            Clear the relations if missing.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if relations:
        data["relations"] = relations
    return client._creoson_post("file", "relations_set", data)


def rename(client, new_name, file_=None, onlysession=None):
    """Rename a model.

    Args:
        client (obj):
            creopyson Client.
        new_name (str):
            New file name.
        `file_` (str, optional):
            File name. Defaults is currently active model.
        onlysession (bool, optional):
            Modify only in memory, not on disk. Defaults is False.

    Returns:
        (str): The new model name.

    """
    data = {"new_name": new_name, "onlysession": False}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if onlysession:
        data["onlysession"] = onlysession
    return client._creoson_post("file", "rename", data, "file")


def repaint(client, file_=None):
    """Repaint the window containing a model.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            File name. Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "repaint", data)


def save(client, file_=None):
    """Save one or more models.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str|list:str, optional):
            File name or List of file names;
            Defaults is currently active model.

    Returns:
        None

    """
    data = {}
    if file_ is not None:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "save", data)


def set_cur_material(client, material, file_=None):
    """Set the current material for a part or parts.

    Args:
        client (obj):
            creopyson Client.
        material (str):
            Material name.
        `file_` (str, optional):
            Part name. Wildcard allowed.
            Defaults is currently active model.

    Returns:
        list:
            list of impacted files.

    """
    data = {"material": material}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("file", "set_cur_material", data, "files")


def set_length_units(client, units, file_=None, convert=None):
    """Set the current length units for a model.

    This will search the model's available Unit Systems for the first one
    which contains the given length unit.

    Args:
        client (obj):
            creopyson Client.
        units (str):
            New length units.
        `file_` (str|list:str, optional):
            File name or List of file names;
            Defaults is currently active model.
        convert (bool, optional):
            Whether to convert the model's length values to the
            new units (True) or leave them the same value (False).
            Defaults is True.

    Returns:
        None

    """
    data = {"units": units}
    if file_ is not None:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if convert:
        data["convert"] = convert
    return client._creoson_post("file", "set_length_units", data)


def set_mass_units(client, units, file_=None, convert=None):
    """Set the mass units for a model.

    This will search the model's available Unit Systems for the first one
    which contains the given mass unit.

    Args:
        client (obj):
            creopyson Client.
        units (str):
            New mass units.
        `file_` (str|list:str, optional):
            File name or List of file names;
            Defaults is currently active model.
        convert (bool, optional):
            Whether to convert the model's mass values to the
            new units (True) or leave them the same value (False).
            Defaults is True.

    Returns:
        None

    """
    data = {"units": units}
    if file_ is not None:
        if isinstance(file_, (str)):
            data["file"] = file_
        elif isinstance(file_, (list)):
            data["files"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if convert:
        data["convert"] = convert
    return client._creoson_post("file", "set_mass_units", data)
