"""Parameters testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_parameter_copy(mk_creoson_post_None, mk_getactivefile):
    """Test copy."""
    c = creopyson.Client()
    result = c.parameter_copy(
        "name", "to_name", file_="file", to_file="target file", designate=True
    )
    assert result is None
    result = c.parameter_copy("name", "to_name")
    assert result is None


def test_parameter_delete(mk_creoson_post_None, mk_getactivefile):
    """Test delete."""
    c = creopyson.Client()
    result = c.parameter_delete("name", file_="file")
    assert result is None
    result = c.parameter_delete("name")
    assert result is None


def test_parameter_exists(mk_creoson_post_dict, mk_getactivefile):
    """Test exists."""
    c = creopyson.Client()
    result = c.parameter_exists(name="name", file_="file")
    assert result is True
    result = c.parameter_exists(name=["name", "other name"])
    assert result is True


def test_parameter_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.parameter_list(name="name", file_="file", encoded=True, value="value")
    assert isinstance(result, (list))
    result = c.parameter_list(name=["name", "other name"])
    assert isinstance(result, (list))


def test_parameter_set(mk_creoson_post_None, mk_getactivefile):
    """Test set."""
    c = creopyson.Client()
    result = c.parameter_set(
        "name",
        value=12,
        file_="file",
        type_="INTEGER",
        encoded=True,
        designate=True,
        description="This is a description",
        no_create=True,
    )
    assert result is None
    result = c.parameter_set("name")
    assert result is None


def test_parameter_set_designated(mk_creoson_post_None, mk_getactivefile):
    """Test set_designated."""
    c = creopyson.Client()
    result = c.parameter_set_designated("name", True, file_="file")
    assert result is None
    result = c.parameter_set_designated("name", True)
    assert result is None
