"""Drawing testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None


def test_drawing_add_model(mk_creoson_post_None):
    """Test add_model."""
    c = creopyson.Client()
    result = c.drawing_add_model("model", drawing="drawing")
    assert result is None


def test_drawing_add_sheet(mk_creoson_post_None):
    """Test add_sheet."""
    c = creopyson.Client()
    result = c.drawing_add_sheet(position=3, drawing="drawing")
    assert result is None


def test_drawing_create(mk_creoson_post_dict):
    """Test create."""
    c = creopyson.Client()
    result = c.drawing_create(
        "template",
        model="model",
        drawing="drawing",
        scale=2.5,
        display=True,
        activate=True,
        new_window=True
    )
    assert isinstance(result, (str))


def test_drawing_create_gen_view(mk_creoson_post_None):
    """Test create_gen_view."""
    c = creopyson.Client()
    result = c.drawing_create_gen_view(
        "model_view",
        {"point": 12},
        drawing="drawing",
        view="view",
        sheet=3,
        model="model",
        scale=1.5,
        display_data={"display": "data"},
        exploded=True
    )
    assert result is None


def test_drawing_create_proj_view(mk_creoson_post_None):
    """Test create_proj_view."""
    c = creopyson.Client()
    result = c.drawing_create_proj_view(
        "parent_view",
        {"point": "xyz"},
        drawing="drawing",
        view="view",
        sheet=2,
        display_data=True,
        exploded=True
    )
    assert result is None


def test_drawing_create_symbol(mk_creoson_post_None):
    """Test create_symbol."""
    c = creopyson.Client()
    result = c.drawing_create_symbol(
        "symbol_file",
        {"point": "xyz"},
        drawing="drawing",
        replace_values={"replace": "values"},
        sheet=3
    )
    assert result is None


def test_drawing_delete_models(mk_creoson_post_None):
    """Test delete_models."""
    c = creopyson.Client()
    result = c.drawing_delete_models(
        model="model",
        drawing="drawing",
        delete_views=True
    )
    assert result is None


def test_drawing_delete_sheet(mk_creoson_post_None):
    """Test delete_sheet."""
    c = creopyson.Client()
    result = c.drawing_delete_sheet(5, drawing="drawing")
    assert result is None


def test_drawing_delete_symbol_def(mk_creoson_post_None):
    """Test delete_symbol_def."""
    c = creopyson.Client()
    result = c.drawing_delete_symbol_def("symbol_file", drawing="drawing")
    assert result is None


def test_drawing_delete_symbol_inst(mk_creoson_post_None):
    """Test delete_symbol_inst."""
    c = creopyson.Client()
    result = c.drawing_delete_symbol_inst("symbol_id", drawing="drawing")
    assert result is None


def test_drawing_delete_view(mk_creoson_post_None):
    """Test delete_view."""
    c = creopyson.Client()
    result = c.drawing_delete_view(
        "view",
        drawing="drawing",
        sheet=3,
        del_children=True
    )
    assert result is None


def test_drawing_get_cur_model(mk_creoson_post_dict):
    """Test get_cur_model."""
    c = creopyson.Client()
    result = c.drawing_get_cur_model(drawing="drawing")
    assert isinstance(result, (str))


def test_drawing_get_cur_sheet(mk_creoson_post_dict):
    """Test get_cur_sheet."""
    c = creopyson.Client()
    result = c.drawing_get_cur_sheet(drawing="drawing")
    assert isinstance(result, (int))


def test_drawing_get_num_sheets(mk_creoson_post_dict):
    """Test get_num_sheets."""
    c = creopyson.Client()
    result = c.drawing_get_num_sheets(drawing="drawing")
    assert isinstance(result, (int))


def test_drawing_get_sheet_scale(mk_creoson_post_dict):
    """Test get_sheet_scale."""
    c = creopyson.Client()
    result = c.drawing_get_sheet_scale(
        2,
        drawing="drawing",
        model="model"
    )
    assert isinstance(result, (float))


def test_drawing_get_sheet_size(mk_creoson_post_dict):
    """Test get_sheet_size."""
    c = creopyson.Client()
    result = c.drawing_get_sheet_size(2, drawing="drawing")
    assert isinstance(result, (str))


def test_drawing_get_view_loc(mk_creoson_post_dict):
    """Test get_view_loc."""
    c = creopyson.Client()
    result = c.drawing_get_view_loc("view", drawing="drawing")
    assert isinstance(result, (dict))


def test_drawing_get_view_scale(mk_creoson_post_dict):
    """Test get_view_scale."""
    c = creopyson.Client()
    result = c.drawing_get_view_scale("view", drawing="drawing")
    assert isinstance(result, (float))


def test_drawing_get_view_sheet(mk_creoson_post_dict):
    """Test get_view_sheet."""
    c = creopyson.Client()
    result = c.drawing_get_view_sheet("view", drawing="drawing")
    assert isinstance(result, (int))


def test_drawing_is_symbol_def_loaded(mk_creoson_post_dict):
    """Test is_symbol_def_loaded."""
    c = creopyson.Client()
    result = c.drawing_is_symbol_def_loaded("symbol_file", drawing="drawing")
    assert isinstance(result, (bool))


def test_drawing_list_models(mk_creoson_post_dict):
    """Test list_models."""
    c = creopyson.Client()
    result = c.drawing_list_models(model="model", drawing="drawing")
    assert isinstance(result, (list))


def test_drawing_list_symbols(mk_creoson_post_dict):
    """Test list_symbols."""
    c = creopyson.Client()
    result = c.drawing_list_symbols(
        drawing="drawing",
        symbol_file="symbol_file",
        sheet=2
    )
    assert isinstance(result, (list))


def test_drawing_list_view_details(mk_creoson_post_dict):
    """Test list_view_details."""
    c = creopyson.Client()
    result = c.drawing_list_view_details(view="view", drawing="drawing")
    assert isinstance(result, (list))


def test_drawing_list_views(mk_creoson_post_dict):
    """Test list_views."""
    c = creopyson.Client()
    result = c.drawing_list_views(view="view", drawing="drawing")
    assert isinstance(result, (list))


def test_drawing_load_symbol_def(mk_creoson_post_dict):
    """Test load_symbol_def."""
    c = creopyson.Client()
    result = c.drawing_load_symbol_def(
        "symbol_file", symbol_dir="symbol_dir", drawing="drawing")
    assert isinstance(result, (dict))


def test_drawing_regenerate(mk_creoson_post_None):
    """Test regenerate."""
    c = creopyson.Client()
    result = c.drawing_regenerate(drawing="drawing")
    assert result is None


def test_drawing_regenerate_sheet(mk_creoson_post_None):
    """Test regenerate_sheet."""
    c = creopyson.Client()
    result = c.drawing_regenerate_sheet(sheet=2, drawing="drawing")
    assert result is None


def test_drawing_rename_view(mk_creoson_post_None):
    """Test rename_view."""
    c = creopyson.Client()
    result = c.drawing_rename_view("old_name", "new_name", drawing="drawing")
    assert result is None


def test_drawing_scale_sheet(mk_creoson_post_None):
    """Test scale_sheet."""
    c = creopyson.Client()
    result = c.drawing_scale_sheet(2, 1.5, drawing="drawing", model="model")
    assert result is None


def test_drawing_scale_view(mk_creoson_post_dict):
    """Test scale_view."""
    c = creopyson.Client()
    result = c.drawing_scale_view(1.5, drawing="drawing", view="view")
    assert isinstance(result, (dict))


def test_drawing_select_sheet(mk_creoson_post_None):
    """Test select_sheet."""
    c = creopyson.Client()
    result = c.drawing_select_sheet(3, drawing="drawing")
    assert result is None


def test_drawing_set_cur_model(mk_creoson_post_None):
    """Test set_cur_model."""
    c = creopyson.Client()
    result = c.drawing_set_cur_model("model", drawing="drawing")
    assert result is None


def test_drawing_set_view_loc(mk_creoson_post_None):
    """Test set_view_loc."""
    c = creopyson.Client()
    result = c.drawing_set_view_loc(
        "view", {"coord": "xyz"}, drawing="drawing")
    assert result is None


def test_drawing_view_bound_box(mk_creoson_post_dict):
    """Test view_bound_box."""
    c = creopyson.Client()
    result = c.drawing_view_bound_box("view", drawing="drawing")
    assert isinstance(result, (dict))
