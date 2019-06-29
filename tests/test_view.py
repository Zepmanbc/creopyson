"""View testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_view_activate(mk_creoson_post_None, mk_getactivefile):
    """Test activate."""
    c = creopyson.Client()
    result = c.view_activate(
        "name",
        file_="file.prt"
    )
    assert result is None
    result = c.view_activate("name")
    assert result is None


def test_view_list_exploded(mk_creoson_post_dict, mk_getactivefile):
    """Test list_exploded."""
    c = creopyson.Client()
    result = c.view_list_exploded(
        file_="file",
        name="name"
    )
    assert isinstance(result, (list))
    result = c.view_list_exploded()
    assert isinstance(result, (list))


def test_view_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.view_list(
        file_="file",
        name="name"
    )
    assert isinstance(result, (list))
    result = c.view_list()
    assert isinstance(result, (list))


def test_view_save(mk_creoson_post_None, mk_getactivefile):
    """Test save."""
    c = creopyson.Client()
    result = c.view_save(
        "name",
        file_="file.prt"
    )
    assert result is None
    result = c.view_save("name")
    assert result is None
