"""View testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None


def test_view_activate(mk_creoson_post_None):
    """Test activate."""
    c = creopyson.Client()
    result = c.view_activate(
        "name",
        file_="file.prt"
    )
    assert result is None


def test_view_list_exploded(mk_creoson_post_dict):
    """Test list_exploded."""
    c = creopyson.Client()
    result = c.view_list_exploded(
        file_="file",
        name="name"
    )
    assert isinstance(result, (list))


def test_view_list(mk_creoson_post_dict):
    """Test list."""
    c = creopyson.Client()
    result = c.view_list(
        file_="file",
        name="name"
    )
    assert isinstance(result, (list))


def test_view_save(mk_creoson_post_None):
    """Test save."""
    c = creopyson.Client()
    result = c.view_save(
        "name",
        file_="file.prt"
    )
    assert result is None
