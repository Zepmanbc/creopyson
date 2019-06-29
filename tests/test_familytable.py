"""Familytable testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_familytable_add_inst(mk_creoson_post_None, mk_getactivefile):
    """Test add_inst."""
    c = creopyson.Client()
    result = c.familytable_add_inst("instance", file_="file")
    assert result is None
    result = c.familytable_add_inst("instance")
    assert result is None


def test_familytable_create_inst(mk_creoson_post_dict, mk_getactivefile):
    """Test create_inst."""
    c = creopyson.Client()
    result = c.familytable_create_inst("instance", file_="file")
    assert isinstance(result, (str))
    result = c.familytable_create_inst("instance")
    assert isinstance(result, (str))


def test_familytable_delete_inst(mk_creoson_post_None, mk_getactivefile):
    """Test delete_inst."""
    c = creopyson.Client()
    result = c.familytable_delete_inst("instance", file_="file")
    assert result is None
    result = c.familytable_delete_inst("instance")
    assert result is None


def test_familytable_delete(mk_creoson_post_None, mk_getactivefile):
    """Test delete."""
    c = creopyson.Client()
    result = c.familytable_delete(file_="file")
    assert result is None
    result = c.familytable_delete()
    assert result is None


def test_familytable_exists(mk_creoson_post_dict, mk_getactivefile):
    """Test exists."""
    c = creopyson.Client()
    result = c.familytable_exists("instance", file_="file")
    assert isinstance(result, (bool))
    result = c.familytable_exists("instance")
    assert isinstance(result, (bool))


def test_familytable_get_cell(mk_creoson_post_dict, mk_getactivefile):
    """Test get_cell."""
    c = creopyson.Client()
    result = c.familytable_get_cell(
        "instance",
        12,
        file_="file"
    )
    assert isinstance(result, (dict))
    result = c.familytable_get_cell(
        "instance",
        12
    )
    assert isinstance(result, (dict))


def test_familytable_get_header(mk_creoson_post_dict, mk_getactivefile):
    """Test get_header."""
    c = creopyson.Client()
    result = c.familytable_get_header(file_="file")
    assert isinstance(result, (list))
    result = c.familytable_get_header()
    assert isinstance(result, (list))


def test_familytable_get_parents(mk_creoson_post_dict, mk_getactivefile):
    """Test get_parents."""
    c = creopyson.Client()
    result = c.familytable_get_parents(file_="file")
    assert isinstance(result, (list))
    result = c.familytable_get_parents()
    assert isinstance(result, (list))


def test_familytable_get_row(mk_creoson_post_dict, mk_getactivefile):
    """Test get_row."""
    c = creopyson.Client()
    result = c.familytable_get_row("instance", file_="file")
    assert isinstance(result, (list))
    result = c.familytable_get_row("instance")
    assert isinstance(result, (list))
    # it should have been a dict but colums already exist with list


def test_familytable_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.familytable_list(file_="file", instance="instance")
    assert isinstance(result, (list))
    result = c.familytable_list()
    assert isinstance(result, (list))


def test_familytable_list_tree(mk_creoson_post_dict, mk_getactivefile):
    """Test list_tree."""
    c = creopyson.Client()
    result = c.familytable_list_tree(file_="file", erase=True)
    assert isinstance(result, (list))
    result = c.familytable_list_tree()
    assert isinstance(result, (list))


def test_familytable_replace(mk_creoson_post_None, mk_getactivefile):
    """Test replace."""
    c = creopyson.Client()
    result = c.familytable_replace(
        "cur_model",
        "new_inst",
        file_="file",
        cur_inst="cur_inst",
        path=[1, 2, 3]
    )
    assert result is None
    result = c.familytable_replace(
        "cur_model",
        "new_inst"
    )
    assert result is None


def test_familytable_set_cell(mk_creoson_post_None, mk_getactivefile):
    """Test set_cell."""
    c = creopyson.Client()
    result = c.familytable_set_cell(
        "instance",
        "col id",
        23,
        file_="file"
    )
    assert result is None
    result = c.familytable_set_cell(
        "instance",
        "col id",
        23
    )
    assert result is None
