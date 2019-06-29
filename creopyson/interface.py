"""Interface module.

Export 3D pdf, file (step, iges, dxf, etc...), picture, plot
Run mapkey
Import/Export program (pls, als)

"""

# TODO : add STL export


def export_3dpdf(
    client,
    file_=None,
    filename=None,
    dirname=None,
    height=None,
    width=None,
    dpi=None,
    use_drawing_settings=None
):
    """Export a model to a 3D PDF file.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        filename (str, optional):
            Destination file name. May also contain a path to the file.
            Defaults is the model name with the appropriate file extension,
            in Creo's working directory.
        dirname (str, optional):
            Destination directory. Defaults is Creo's current
            working directory.
        height (float, optional):
            PDF image height. Defaults is Creo default export height.
        width (float, optional):
            PDF image width. Defaults is Creo default export width.
        dpi (int, optional):
            PDF Image DPI. Default is Creo default export DPI.
        use_drawing_settings (boolean, optional):
            Whether to use special settings for exporting drawings.
            Defaut is False.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if filename:
        data["filename"] = filename
    if dirname:
        data["dirname"] = dirname
    if height:
        data["height"] = height
    if width:
        data["width"] = width
    if dpi:
        data["dpi"] = dpi
    if use_drawing_settings:
        data["use_drawing_settings"] = use_drawing_settings
    return client._creoson_post("interface", "export_3dpdf", data)


def export_file(
    client,
    file_type,
    file_=None,
    filename=None,
    dirname=None,
    geom_flags=None,
    advanced=None
):
    """Export a model to a file.

    The geom_flags option only applies to IGES and STEP exports.
    Setting geom_flags to 'default' will cause it to check the Creo config
    option 'intf3d_out_default_option' for the setting
    The advanced option will cause the Export to use settings defined in the
    appropriate `export_profiles` Creo Config Option for the file type.
    The advanced option only applies to DXF, IGES and STEP exports.
    The advanced option will only work with Creo 4 M030 or later.

    Args:
        client (obj):
            creopyson Client.
        file_type (str):
            File type. Valid values: DXF, IGES, PV, STEP, VRML.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        filename (str, optional):
            Destination file name. May also contain a path to the file.
            Defaults is the model name with the appropriate file extension,
            in Creo's working directory.
        dirname (str, optional):
            Destination directory. Defaults is Creo's current
            working directory.
        geom_flags (str, optional):
            Geometry type for the export.
            Defaults is `solids`.
            Valid values: solids, surfaces, wireframe, wireframe_surfaces,
            quilts, default.
        advanced (Boolean, optional):
            Whether to use the newer Creo 4 file export function.
            Defaults is False.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    data = {"type": file_type}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if filename:
        data["filename"] = filename
    if dirname:
        data["dirname"] = dirname
    if geom_flags:
        data["geom_flags"] = geom_flags
    if advanced:
        data["advanced"] = advanced
    return client._creoson_post("interface", "export_file", data)


def export_image(
    client,
    file_type,
    file_=None,
    filename=None,
    height=None,
    width=None,
    dpi=None,
    depth=None
):
    """Export a model to an image file.

    Args:
        client (obj):
            creopyson Client.
        file_type (str):
            Image Type. Valid values: BMP, EPS, JPEG, TIFF.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        filename (str, optional):
            Destination file name. May also contain a path to the file.
            Defaults is the model name with the appropriate file extension,
            in Creo's working directory.
        height (float, optional):
            Image height. Defaults is `7.5`.
        width (float, optional):
            Image width. Defaults is `10.0`.
        dpi (int, optional):
            Image DPI. Defaults is `100`.
        depth (int, optional):
            Image depth. Defaults is `24`.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    data = {"type": file_type}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if filename:
        data["filename"] = filename
    # if dirname:
    #     data["dirname"] = dirname
    if height:
        data["height"] = height
    if width:
        data["width"] = width
    if dpi:
        data["dpi"] = dpi
    if depth:
        data["depth"] = depth
    return client._creoson_post("interface", "export_image", data)


def export_pdf(
    client,
    file_=None,
    filename=None,
    dirname=None,
    height=None,
    width=None,
    dpi=None,
    use_drawing_settings=None
):
    """Export a model to a PDF file.

    When use_drawing_settings is true, the Font Stroke option will be set to
    Stroke All Fonts, and the Color Depth option will be set to Grayscale.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.
        filename (str, optional):
            Destination file name. May also contain a path to the file.
            Defaults is the model name with the appropriate file extension,
            in Creo's working directory.
        dirname (str, optional):
            Destination directory. Defaults is Creo's current
            working directory.
        height (float, optional):
            PDF image height. Defaults is Creo default export height.
        width (float, optional):
            PDF image width. Defaults is Creo default export width.
        dpi (int, optional):
            PDF Image DPI. Default is Creo default export DPI.
        use_drawing_settings (boolean, optional):
            Whether to use special settings for exporting drawings.
            Defaut is False.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if filename:
        data["filename"] = filename
    if dirname:
        data["dirname"] = dirname
    if height:
        data["height"] = height
    if width:
        data["width"] = width
    if dpi:
        data["dpi"] = dpi
    if use_drawing_settings:
        data["use_drawing_settings"] = use_drawing_settings
    return client._creoson_post("interface", "export_pdf", data)


def export_program(client, file_=None):
    """Export a model's program to a file.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is current active model.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    return client._creoson_post("interface", "export_program", data)


def import_program(client, file_=None, filename=None, dirname=None):
    """Import a program file for a model.

    Cannot specify both file and filename parameters.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Destination Model name.
            Defaults is currently active model, or the model for
            the filename parameter if given.
        filename (str, optional):
            Source file name.
            Default is the model name with the appropriate file extension.
        dirname (str, optional):
            Source directory. Defaults is Creo's current working directory.

    Returns:
        str: Name of the model updated

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if filename:
        data["filename"] = filename
    if dirname:
        data["dirname"] = dirname
    return client._creoson_post("interface", "import_program", data, "file")


def mapkey(client, script):
    """Run a Mapkey script in Creo.

    Make sure to remove any `mapkey(continued)` clauses from the script
    argument. The tilde at the start of a line should occur immediately
    after the semicolon at the end of the previous line.

    Args:
        client (obj): creopyson Client.
        script (str): The mapkey script to run.

    Returns: None

    """
    data = {"script": script}
    return client._creoson_post("interface", "mapkey", data)


def plot(client, file_=None, dirname=None, driver=None):
    """Export a model plot.

    Args:
        client (obj):
            creopyson Client.
        `file_` (str, optional):
            Model name. Defaults is currently active model.
        dirname (str, optional):
            Destination directory.
            Defaults is Creo's current working directory.
        driver (str, optional):
            Driver export.
            Defaults is `POSTSCRIPT`.
            Valid values: POSTSCRIPT, JPEG, TIFF.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    data = {}
    if file_ is not None:
        data["file"] = file_
    else:
        active_file = client.file_get_active()
        if active_file is not None:
            data["file"] = active_file["file"]
    if dirname:
        data["dirname"] = dirname
    if driver:
        data["driver"] = driver
    return client._creoson_post("interface", "plot", data)
