"""Geometry testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_geometry_bound_box(mk_creoson_post_dict, mk_getactivefile):
    """Test bound_box."""
    c = creopyson.Client()
    result = c.geometry_bound_box(file_="file")
    assert isinstance(result, (dict))
    result = c.geometry_bound_box()
    assert isinstance(result, (dict))


def test_geometry_get_edges(mk_creoson_post_dict, mk_getactivefile):
    """Test get_edges."""
    c = creopyson.Client()
    result = c.geometry_get_edges(["12", "34"], file_="file")
    assert isinstance(result, (list))
    result = c.geometry_get_edges(["12", "34"])
    assert isinstance(result, (list))


def test_geometry_get_surfaces(mk_creoson_post_dict, mk_getactivefile):
    """Test get_surfaces."""
    c = creopyson.Client()
    result = c.geometry_get_surfaces(file_="file")
    assert isinstance(result, (list))
    result = c.geometry_get_surfaces()
    assert isinstance(result, (list))
