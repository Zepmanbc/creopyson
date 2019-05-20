"""Interface module.

Export 3D pdf, file (step, iges, dxf, etc...), picture, plot
Run mapkey
Import/Export program (pls, als)

"""

from .core import creoson_post


def export_3dpdf(
    client,
    current_file=None,
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
        current_file (str, optional):
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

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "export_3dpdf",
    }
    if current_file:
        request["data"]["file"] = current_file
    if filename:
        request["data"]["filename"] = filename
    if dirname:
        request["data"]["dirname"] = dirname
    if height:
        request["data"]["height"] = height
    if width:
        request["data"]["width"] = width
    if dpi:
        request["data"]["dpi"] = dpi
    if use_drawing_settings:
        request["data"]["use_drawing_settings"] = use_drawing_settings
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def export_file(
    client,
    file_type,
    current_file=None,
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
        current_file (str, optional):
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

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "export_file",
        "data": {
            "type": file_type
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if filename:
        request["data"]["filename"] = filename
    if dirname:
        request["data"]["dirname"] = dirname
    if geom_flags:
        request["data"]["geom_flags"] = geom_flags
    if advanced:
        request["data"]["advanced"] = advanced
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def export_image(
    client,
    file_type,
    current_file=None,
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
        current_file (str, optional):
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

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "export_image",
        "data": {
            "type": file_type
        }
    }
    if current_file:
        request["data"]["file"] = current_file
    if filename:
        request["data"]["filename"] = filename
    # if dirname:
    #     request["data"]["dirname"] = dirname
    if height:
        request["data"]["height"] = height
    if width:
        request["data"]["width"] = width
    if dpi:
        request["data"]["dpi"] = dpi
    if depth:
        request["data"]["depth"] = depth
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def export_pdf(
    client,
    current_file=None,
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
        current_file (str, optional):
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

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "export_pdf",
    }
    if current_file:
        request["data"]["file"] = current_file
    if filename:
        request["data"]["filename"] = filename
    if dirname:
        request["data"]["dirname"] = dirname
    if height:
        request["data"]["height"] = height
    if width:
        request["data"]["width"] = width
    if dpi:
        request["data"]["dpi"] = dpi
    if use_drawing_settings:
        request["data"]["use_drawing_settings"] = use_drawing_settings
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def export_program(client, current_file=None):
    """Export a model's program to a file.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is current active model.

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "export_program",
    }
    if current_file:
        request["data"]["file"] = current_file
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)


def import_program(client, current_file=None, filename=None, dirname=None):
    """Import a program file for a model.

    Cannot specify both file and filename parameters.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Destination Model name.
            Defaults is currently active model, or the model for
            the filename parameter if given.
        filename (str, optional):
            Source file name.
            Default is the model name with the appropriate file extension.
        dirname (str, optional):
            Source directory. Defaults is Creo's current working directory.

    Raises:
        Warning: error message from creoson.

    Returns:
        str: Name of the model updated

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "import_program",
    }
    if current_file:
        request["data"]["file"] = current_file
    if filename:
        request["data"]["filename"] = filename
    if dirname:
        request["data"]["dirname"] = dirname
    status, data = creoson_post(client, request)
    if not status:
        return data["file"]
    else:
        raise Warning(data)


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
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "mapkey",
        "data": {
            "script": script,
        }
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def plot(client, current_file=None, dirname=None, driver=None):
    """Export a model plot.

    Args:
        client (obj):
            creopyson Client.
        current_file (str, optional):
            Model name. Defaults is currently active model.
        dirname (str, optional):
            Destination directory.
            Defaults is Creo's current working directory.
        driver (str, optional):
            Driver export.
            Defaults is `POSTSCRIPT`.
            Valid values: POSTSCRIPT, JPEG, TIFF.

    Raises:
        Warning: error message from creoson.

    Returns:
        dict:
            dirname (str): Directory of the output file
            filename (str): Name of the output file

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "plot",
    }
    if current_file:
        request["data"]["file"] = current_file
    if dirname:
        request["data"]["dirname"] = dirname
    if driver:
        request["data"]["driver"] = driver
    status, data = creoson_post(client, request)
    if not status:
        return data
    else:
        raise Warning(data)
