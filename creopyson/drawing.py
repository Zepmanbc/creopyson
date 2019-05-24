"""Drawing module."""

from .core import creoson_post


def add_model(client, model, drawing=None):
    """Add a model to a drawing.

    Args:
        client (obj):
            creopyson Client.
        model (str):
            Model name.
        drawing (str, optional):
            Drawing name. Defaults is Current active drawing.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "add_model",
        "data": {
            "model": model
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "add_sheet",
        "data": {}
    }
    if position:
        request["data"]["position"] = position
    if drawing:
        request["data"]["drawing"] = drawing
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def create(
    client,
    template,
    model=None,
    drawing=None,
    scale=None,
    display=None,
    activate=None,
    new_window=None
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

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): New drawing name.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "create",
        "data": {
            "template": template,
        }
    }
    if model:
        request["data"]["model"] = model
    if drawing:
        request["data"]["drawing"] = drawing
    if scale:
        request["data"]["scale"] = scale
    if display:
        request["data"]["display"] = display
    if activate:
        request["data"]["activate"] = activate
    if new_window:
        request["data"]["new_window"] = new_window
    status, data = creoson_post(client, request)
    if not status:
        return data["drawing"]
    else:
        raise Warning(data)


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
    exploded=None
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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "create_gen_view",
        "data": {
            "model_view": model_view,
            "point": point
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    if view:
        request["data"]["view"] = view
    if sheet:
        request["data"]["sheet"] = sheet
    if model:
        request["data"]["model"] = model
    if scale:
        request["data"]["scale"] = scale
    if display_data:
        request["data"]["display_data"] = display_data
    if exploded:
        request["data"]["exploded"] = exploded
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)
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
    exploded=None
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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "create_proj_view",
        "data": {
            "parent_view": parent_view,
            "point": point
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    if view:
        request["data"]["view"] = view
    if sheet:
        request["data"]["sheet"] = sheet
    if display_data:
        request["data"]["display_data"] = display_data
    if exploded:
        request["data"]["exploded"] = exploded
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def create_symbol(
    client,
    symbol_file,
    point,
    drawing=None,
    replace_values=None,
    sheet=None
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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "create_symbol",
        "data": {
            "symbol_file": symbol_file,
            "point": point
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    if replace_values:
        request["data"]["replace_values"] = replace_values
    if sheet:
        request["data"]["sheet"] = sheet
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete_models(
    client,
    model=None,
    drawing=None,
    delete_views=None
):
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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "delete_models",
        "data": {}
    }
    if drawing:
        request["data"]["drawing"] = drawing
    if model:
        request["data"]["model"] = model
    if delete_views:
        request["data"]["delete_views"] = delete_views
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


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

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "delete_sheet",
        "data": {
            "sheet": sheet
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete_symbol_def(client, symbol_file, drawing=None):
    """Delete a symbol definition and its instances from a drawing.

    Args:
        client (obj):
            creopyson Client
        symbol_file (str):
            Name of the symbol file.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "delete_symbol_def",
        "data": {
            "symbol_file": symbol_file
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete_symbol_inst(client, symbol_id, drawing=None):
    """Delete a specific symbol instance from a drawing.

    Args:
        client (obj):
            creopyson Client
        symbol_id (str):
            ID of the symbol instance.
        drawing (str, optional):
            Drawing name. Defaults: current active drawing.

    Raises:
        Warning: error message from creoson.

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "drawing",
        "function": "delete_symbol_inst",
        "data": {
            "symbol_id": symbol_id
        }
    }
    if drawing:
        request["data"]["drawing"] = drawing
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete_view(client, ):
    pass


def get_cur_model(client, ):
    pass


def get_cur_sheet(client, ):
    pass


def get_num_sheets(client, ):
    pass


def get_sheet_scale(client, ):
    pass


def get_sheet_size(client, ):
    pass


def get_view_loc(client, ):
    pass


def get_view_scale(client, ):
    pass


def get_view_sheet(client, ):
    pass


def is_symbol_def_loaded(client, ):
    pass


def list_models(client, ):
    pass


def list_symbols(client, ):
    pass


def list_view_details(client, ):
    pass


def list_views(client, ):
    pass


def load_symbol_def(client, ):
    pass


def regenerate(client, ):
    pass


def regenerate_sheet(client, ):
    pass


def rename_view(client, ):
    pass


def scale_sheet(client, ):
    pass


def scale_view(client, ):
    pass


def select_sheet(client, ):
    pass


def set_cur_model(client, ):
    pass


def set_view_loc(client, ):
    pass


def view_bound_box(client, ):
    pass
