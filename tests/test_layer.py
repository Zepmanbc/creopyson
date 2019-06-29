"""Layer testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_layer_delete(mk_creoson_post_None, mk_getactivefile):
    """Test delete."""
    c = creopyson.Client()
    result = c.layer_delete(name="name", file_="file")
    assert result is None
    result = c.layer_delete()
    assert result is None


def test_layer_exists(mk_creoson_post_dict, mk_getactivefile):
    """Test exists."""
    c = creopyson.Client()
    result = c.layer_exists(name="name", file_="file")
    assert isinstance(result, (bool))
    result = c.layer_exists()
    assert isinstance(result, (bool))


def test_layer_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.layer_list(name="name", file_="file")
    assert isinstance(result, (list))
    result = c.layer_list()
    assert isinstance(result, (list))


def test_layer_show(mk_creoson_post_None, mk_getactivefile):
    """Test show."""
    c = creopyson.Client()
    result = c.layer_show(name="name", file_="file", show_=True)
    assert result is None
    result = c.layer_show()
    assert result is None
