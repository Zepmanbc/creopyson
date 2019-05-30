"""Dimension testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None


def test_dimension_copy(mk_creoson_post_None):
    """Test dimension_copy."""
    c = creopyson.Client()
    result = c.dimension_copy(
        "old_name",
        "new_name",
        file_="file.prt",
        to_file="file.prt"
    )
    assert result is None


def test_dimension_list(mk_creoson_post_dict):
    """Test dimension_list."""
    c = creopyson.Client()
    result = c.dimension_list(
        name="name",
        file_="file.prt",
        dim_type="linear",
        encoded=True
    )
    assert isinstance(result, (list))
    result = c.dimension_list(
        name=["name", "other name"],
        file_="file.prt",
        dim_type="linear",
        encoded=True
    )
    assert isinstance(result, (list))


def test_dimension_list_detail(mk_creoson_post_dict):
    """Test dimension_list."""
    c = creopyson.Client()
    result = c.dimension_list_detail(
        name="name",
        file_="file.prt",
        dim_type="linear",
        encoded=True
    )
    assert isinstance(result, (list))
    result = c.dimension_list_detail(
        name=["name", "other name"],
        file_="file.prt",
        dim_type="linear",
        encoded=True
    )
    assert isinstance(result, (list))


def test_dimension_set(mk_creoson_post_None):
    """Test dimension_set."""
    c = creopyson.Client()
    result = c.dimension_set(
        "file",
        "name",
        12.4,
        encoded=True
    )
    assert result is None


def test_dimension_show(mk_creoson_post_None):
    """Test dimension_show."""
    c = creopyson.Client()
    result = c.dimension_show(
        "name",
        file_="filename",
        assembly="asm name",
        path=['path']
    )
    assert result is None


def test_dimension_user_select(mk_creoson_post_dict):
    """Test user_select."""
    c = creopyson.Client()
    result = c.dimension_user_select(
        file_="file.prt",
        maxi=3
    )
    assert isinstance(result, (list))
