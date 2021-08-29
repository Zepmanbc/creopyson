"""Drawing module."""


def add_model(client, model, drawing=None):
    """Add a model to a drawing.

    Args:
        client (obj):
            creopyson Client.
        model (str):
            Model name.
        drawing (str, optional):
            Drawing name. Defaults is Current active drawing.

    Returns:
        None

    """
    data = {"model": model}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "add_model", data)


def add_sheet(client, position=None, drawing=None):
    """Add a drawing sheet.

    Args:
        client (obj):
            creopyson Client.
        position (int, optional):
            Position to add the sheet.
            Defaults: Sheet will be added to the end.
        drawing (str, optional):
            Drawing name. Defaults is current active drawing.

    Returns:
        None

    """
    data = {}
    if position is not None:
        data["position"] = position
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "add_sheet", data)


def create(
    client,
    template,
    model=None,
    drawing=None,
    scale=None,
    display=None,
    activate=None,
    new_window=None,
):
    """Create a new drawing from a template.

    Args:
        client (obj):
            creopyson Client.
        template (str):
            Template
        model (str, optional):
            Model name. Defaults: Current active model.
        drawing (str, optional):
            New drawing name.
            Defaults: A name derived from the model's instance name.
        scale (float, optional):
            Drawing scale. Defaults is `1.0`.
        display (boolean, optional):
            Display the drawing after open. Defaults is False.
        activate (boolean, optional):
            Activate the drawing window after open. Defaults is False.
        new_window (boolean, optional):
            Open drawing in a new window. Defaults is False.

    Returns:
        (str): New drawing name.

    """
    data = {"template": template}
    if model is not None:
        data["model"] = model
    if drawing is not None:
        data["drawing"] = drawing
    if scale is not None:
        data["scale"] = scale
    if display is not None:
        data["display"] = display
    if activate is not None:
        data["activate"] = activate
    if new_window is not None:
        data["new_window"] = new_window
    return client._creoson_post("drawing", "create", data, "drawing")


def create_gen_view(
    client,
    model_view,
    point,
    drawing=None,
    view=None,
    sheet=None,
    model=None,
    scale=None,
    display_data=None,
    exploded=None,
):
    """Create general view on a drawing.

    Args:
        client (obj):
            creopyson Client
        model_view (str):
            Model view to use for the drawing view orientation.
        point (dict):
            Coordinates for the view in Drawing Units.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        view (str, optional):
            New view name. Defaults: the model_view parameter.
        sheet (int, optional):
            Sheet number. Defaults: current active sheet on the drawing.
        model (str, optional):
            Model for the view. Defaults: current active model on the drawing.
        scale (float, optional):
            View scale. Defaults: the sheet's scale.
        display_data (dict, optional):
            Display parameters used to create the view.
            Defaults: Creo defaults.
        exploded (boolean, optional):
            Whether to create the view as an exploded view. Defaults is False.

    Returns:
        None

    """
    data = {"model_view": model_view, "point": point}
    if drawing is not None:
        data["drawing"] = drawing
    if view is not None:
        data["view"] = view
    if sheet is not None:
        data["sheet"] = sheet
    if model is not None:
        data["model"] = model
    if scale is not None:
        data["scale"] = scale
    if display_data is not None:
        data["display_data"] = display_data
    if exploded is not None:
        data["exploded"] = exploded
    return client._creoson_post("drawing", "create_gen_view", data)
    # TODO: JLpoint Method for point
    # TODO: ViewDisplayData method for display_data


def create_proj_view(
    client,
    parent_view,
    point,
    drawing=None,
    view=None,
    sheet=None,
    display_data=None,
    exploded=None,
):
    """Create projection view on a drawing.

    When specifying the view coordinates, you should specify only an X or a Y
    coordinate to avoid confusion.  If you specify both coordinates, it
    appears Creo may be using whichever has the larger absolute value.

    Args:
        client (obj):
            creopyson Client
        parent_view (str):
            Parent view for the projection view.
        point (dict):
            Coordinates for the view, relative to the location
            of the parent view, in Drawing Units.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        view (str, optional):
            New view name. Defaults: Creo's default name for a new view.
        sheet (int, optional):
            Sheet number. Defaults: current active sheet on the drawing.
        display_data (dict, optional):
            Display parameters used to create the view.
            Defaults: the display parameters of the parent view.
        exploded (boolean, optional):
            Whether to create the view as an exploded view. Defaults is False.

    Returns:
        None

    """
    data = {"parent_view": parent_view, "point": point}
    if drawing is not None:
        data["drawing"] = drawing
    if view is not None:
        data["view"] = view
    if sheet is not None:
        data["sheet"] = sheet
    if display_data is not None:
        data["display_data"] = display_data
    if exploded is not None:
        data["exploded"] = exploded
    return client._creoson_post("drawing", "create_proj_view", data)


def create_symbol(
    client, symbol_file, point, drawing=None, replace_values=None, sheet=None
):
    """Add a symbol instance to a drawing.

    Args:
        client (obj):
            creopyson Client
        symbol_file (str):
            Name of the symbol file.
        point (dict):
            Coordinates for the symbol in Drawing Units.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        replace_values (dict, optional):
            Object containing replacement values for any
            variable text in the symbol. Defaults to None.
        sheet (int, optional):
            Sheet number (0 for all sheets).
            Defaults: the symbol will be added to all sheets.

    Returns:
        None

    """
    data = {"symbol_file": symbol_file, "point": point}
    if drawing is not None:
        data["drawing"] = drawing
    if replace_values is not None:
        data["replace_values"] = replace_values
    if sheet is not None:
        data["sheet"] = sheet
    return client._creoson_post("drawing", "create_symbol", data)


def delete_models(client, model=None, drawing=None, delete_views=None):
    """Delete one or more models from a drawing.

    Args:
        client (obj):
            creopyson Client
        model (str, optional):
            Model name (wildcard allowed: True).
            Defaults: all models will be deleted from the drawing.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        delete_views (boolean, optional):
            Whether to delete drawing views associated with the model.
            Defaults is False.

    Returns:
        None

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    if model is not None:
        data["model"] = model
    if delete_views is not None:
        data["delete_views"] = delete_views
    return client._creoson_post("drawing", "delete_models", data)


def delete_sheet(client, sheet, drawing=None):
    """Delete a drawing sheet.

    An error will occur if you try to delete the only sheet in a drawing.

    Args:
        client (obj):
            creopyson Client
        sheet (int):
            Sheet number.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"sheet": sheet}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "delete_sheet", data)


def delete_symbol_def(client, symbol_file, drawing=None):
    """Delete a symbol definition and its instances from a drawing.

    Args:
        client (obj):
            creopyson Client
        symbol_file (str):
            Name of the symbol file.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"symbol_file": symbol_file}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "delete_symbol_def", data)


def delete_symbol_inst(client, symbol_id, drawing=None):
    """Delete a specific symbol instance from a drawing.

    Args:
        client (obj):
            creopyson Client
        symbol_id (str):
            ID of the symbol instance.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"symbol_id": symbol_id}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "delete_symbol_inst", data)


def delete_view(client, view, drawing=None, sheet=None, del_children=None):
    """Delete a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            View name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        sheet (int, optional):
            Sheet number; if filled in, the view will only be deleted if it is
            on that sheet. Defaults: Delete the view from any sheet.
        del_children ([boolean, optional):
            Whether to also delete any children of the view. Defaults is False.

    Returns:
        None

    """
    data = {"view": view}
    if drawing is not None:
        data["drawing"] = drawing
    if sheet is not None:
        data["sheet"] = sheet
    if del_children is not None:
        data["del_children"] = del_children
    return client._creoson_post("drawing", "delete_view", data)


def get_cur_model(client, drawing=None):
    """Get the active model on a drawing.

    Args:
        client (obj):
            creopyson Client
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (str): Model name.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_cur_model", data, "file")


def get_cur_sheet(client, drawing=None):
    """Get the current drawing sheet.

    Args:
        client (obj):
            creopyson Client
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (int): Sheet number.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_cur_sheet", data, "sheet")


def get_num_sheets(client, drawing=None):
    """Get the number of sheets on a drawing.

    Args:
        client (obj):
            creopyson Client
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (int): Number of sheets.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_num_sheets", data, "num_sheets")


def get_sheet_format(client, sheet, drawing=None):
    """Get the drawing format file of drawing sheet.

    Args:
        client (obj):
            creopyson Client.
        sheet (int):
            Sheet number.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (dict):
            file(str):
                Format file name, may be null if there is no current format.
            full_name(str):
                Format full name.
            common_name(str):
                Format common name.

    """
    data = {"sheet": sheet}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_sheet_format", data)


def get_sheet_scale(client, sheet, drawing=None, model=None):
    """Get the scale of a drawing sheet.

    Args:
        client (obj):
            creopyson Client
        sheet (int):
            Sheet number.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        model (str, optional):
            Drawing model used to calculate the scale.
            Defaults: the active model on the drawing.

    Returns:
        (float): Sheet scale.

    """
    data = {"sheet": sheet}
    if drawing is not None:
        data["drawing"] = drawing
    if model is not None:
        data["model"] = model
    return client._creoson_post("drawing", "get_sheet_scale", data, "scale")


def get_sheet_size(client, sheet, drawing=None):
    """Get the size of a drawing sheet.

    Args:
        client (obj):
            creopyson Client
        sheet (int):
            Sheet number.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (str): Sheet size.

    """
    data = {"sheet": sheet}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_sheet_size", data, "size")


def get_view_loc(client, view, drawing=None):
    """Get the location of a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            View name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (dict):
            x (float): X-coordinate of the view
            y (float): Y-coordinate of the view
            z (float): Z-coordinate of the view

    """
    data = {"view": view}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_view_loc", data)
    # TODO: return a tuple (x,y,z)?


def get_view_scale(client, view, drawing=None):
    """Get the scale of a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            View name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Raises:
        Warning: error message from creoson.

    Returns:
        (float): View scale.

    """
    data = {"view": view}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_view_scale", data, "scale")


def get_view_sheet(client, view, drawing=None):
    """Get the sheet number that contains a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            View name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (int): Sheet number.

    """
    data = {"view": view}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "get_view_sheet", data, "sheet")


def is_symbol_def_loaded(client, symbol_file, drawing=None):
    """Check whether a symbol definition file is loaded into Creo.

    Args:
        client (obj):
            creopyson Client
        symbol_file (str):
            Name of the symbol file.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (boolean): Whether the symbol definition is loaded into Creo.

    """
    data = {"symbol_file": symbol_file}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "is_symbol_def_loaded", data, "loaded")


def list_models(client, model=None, drawing=None):
    """List the models contained in a drawing.

    Args:
        client (obj):
            creopyson Client
        model (str, optional):
            Model name filter (wildcards allowed: True).
            Defaults: no filter.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (list:str): List of model names in the drawing.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    if model is not None:
        data["model"] = model
    return client._creoson_post("drawing", "list_models", data, "files")


def list_symbols(client, drawing=None, symbol_file=None, sheet=None):
    """List symbols contained on a drawing.

    Args:
        client (obj):
            creopyson Client
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        symbol_file (str, optional):
            Symbol file name filter. Defaults: no filter.
        sheet (int, optional):
            Sheet number (0 for all sheets).
            Defaults: The symbol will be added to all sheets.

    Returns:
        (list:dict):
            List of symbols in the drawing.
                id (int): Symbol ID.
                symbol_name (str): Symbol name.
                sheet (int): Sheet number.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    if symbol_file is not None:
        data["symbol_file"] = symbol_file
    if sheet is not None:
        data["sheet"] = sheet
    return client._creoson_post("drawing", "list_symbols", data, "symbols")


def list_view_details(client, view=None, drawing=None):
    """List the views contained in a drawing, with more details.

    Args:
        client (obj):
            creopyson Client
        view (str, optional):
            View name filter (wildcards allowed: True). Defaults: no filter.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (list:dict):
            List of views in the drawing
                name (str):
                    View name.
                sheet (int):
                    Sheet number.
                location (dict):
                    Coordonates
                        x (float): X-coordinate of the view
                        y (float): Y-coordinate of the view
                        z (float): Z-coordinate of the view
                text_height (float):
                    Text Heigh in Drawing Units.
                view_model (str):
                    View model name.
                simp_rep (str):
                    View simplified rep name.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    if view is not None:
        data["view"] = view
    return client._creoson_post("drawing", "list_view_details", data, "views")


def list_views(client, view=None, drawing=None):
    """List the views contained in a drawing.

    Args:
        client (obj):
            creopyson Client
        view (str, optional):
            View name filter (wildcards allowed: True). Defaults: no filter.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (list:str): List of views in the drawing.

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    if view is not None:
        data["view"] = view
    return client._creoson_post("drawing", "list_views", data, "views")


def load_symbol_def(client, symbol_file, symbol_dir=None, drawing=None):
    """Load a Creo symbol definition file into Creo from disk.

    Args:
        client (obj):
            creopyson Client
        symbol_file (str):
            Name of the symbol file.
        symbol_dir (str, optional):
            Directory containing the symbol file; if relative,
            assumed to be relative to Creo's current working directory.
            Defaults: Creo's current working directory.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (dict): Symbol definition.
            id (int): ID of the loaded symbol.
            name (str): Symbol Name of the loaded symbol.

    """
    data = {"symbol_file": symbol_file}
    if drawing is not None:
        data["drawing"] = drawing
    if symbol_dir is not None:
        data["symbol_dir"] = symbol_dir
    return client._creoson_post("drawing", "load_symbol_def", data)


def regenerate(client, drawing=None):
    """Regenerate a drawing.

    Args:
        client (obj):
            creopyson Client
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "regenerate", data)


def regenerate_sheet(client, sheet=None, drawing=None):
    """Regenerate a sheet on a drawing.

    Args:
        client (obj):
            creopyson Client
        sheet (int, optional):
            Sheet number (0 for all sheets).
            Defaults: all sheets will be regenerated.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {}
    if sheet is not None:
        data["sheet"] = sheet
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "regenerate_sheet", data)


def rename_view(client, view, new_view, drawing=None):
    """Rename a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            Old view name.
        new_view (str):
            New view name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"view": view, "new_view": new_view}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "rename_view", data)


def scale_sheet(client, sheet, scale, drawing=None, model=None):
    """Set the scale of a drawing sheet.

    Args:
        client (obj):
            creopyson Client
        sheet (int):
            Sheet number.
        scale (float):
            View scale.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.
        model (str, optional):
            Drawing model to scale. Defaults: tThe active model on the drawing.

    Returns:
        None

    """
    data = {"sheet": sheet, "scale": scale}
    if drawing is not None:
        data["drawing"] = drawing
    if model is not None:
        data["model"] = model
    return client._creoson_post("drawing", "scale_sheet", data)


def scale_view(client, scale, view=None, drawing=None):
    """Set the scale of one or more drawing views.

    Args:
        client (obj):
            creopyson Client
        scale (float):
            View scale.
        view (str, optional):
            View name (wildcards allowed: True).
            Defaults: all views will be scaled.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (dict)
            succes_views (list):
                List of view which were successfully scaled.
            failed_views (list):
                List of view which failed to scale.

    """
    data = {"scale": scale}
    if drawing is not None:
        data["drawing"] = drawing
    if view is not None:
        data["view"] = view
    return client._creoson_post("drawing", "scale_view", data)


def select_sheet(client, sheet, drawing=None):
    """Make a drawing sheet the current sheet.

    Args:
        client (obj):
            creopyson Client
        sheet (int):
            Sheet number.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"sheet": sheet}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "select_sheet", data)


def set_cur_model(client, model, drawing=None):
    """Set the active model on a drawing.

    Args:
        client (obj):
            creopyson Client
        model (str):
            Model name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"model": model}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "set_cur_model", data)


def set_sheet_format(client, sheet, file_format, dirname=None, drawing=None):
    """Set the drawing format file of a drawing sheet.

    Args:
        client (obj):
            creopyson Client.
        sheet (int):
            Sheet number.
        file_format (str):
            Format file name.
        dirname (str, optional): Directory name containing the file format.
            Defaults to None is current working directory.
        drawing (str, optional):
            Drawing name. Defaults to None is current active drawing.

    Returns:
        None
    """
    data = {"sheet": sheet, "dirname": dirname}
    if drawing is not None:
        data["drawing"] = drawing
    if file_format is not None:
        data["file"] = file_format
    return client._creoson_post("drawing", "set_sheet_format", data)


def set_view_loc(client, view, point, drawing=None):
    """Set the location of a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            View name.
        point (dict):
            Coordinates for the view in Drawing Units
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        None

    """
    data = {"view": view, "point": point}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "set_cur_model", data)


def view_bound_box(client, view, drawing=None):
    """Get the 2D bounding box for a drawing view.

    Args:
        client (obj):
            creopyson Client
        view (str):
            View name.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Returns:
        (dict):
            xmin (float): Minimum X-coordinate of drawing view.
            xmax (float): Maximum X-coordinate of drawing view.
            ymin (float): Minimum Y-coordinate of drawing view.
            ymax (float): Maximum Y-coordinate of drawing view.

    """
    data = {"view": view}
    if drawing is not None:
        data["drawing"] = drawing
    return client._creoson_post("drawing", "view_bound_box", data)
