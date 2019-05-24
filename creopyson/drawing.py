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


def create_gen_view(
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
        "function": "create_gen_view",
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


def create(client, ):
    pass


def create_proj_view(client, ):
    pass


def create_symbol(client, ):
    pass


def delete_models(client, ):
    pass


def delete_sheet(client, ):
    pass


def delete_symbol_def(client, ):
    pass


def delete_symbol_inst(client, ):
    pass


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
