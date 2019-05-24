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


def create_gen_view(client, ):
    pass


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
