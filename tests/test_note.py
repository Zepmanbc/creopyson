"""Note testing."""
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_note_copy(mk_creoson_post_None, mk_getactivefile):
    """Test copy."""
    c = creopyson.Client()
    result = c.note_copy(
        "name",
        to_name="target name",
        file_="file",
        to_file="target file"
    )
    assert result is None
    result = c.note_copy("name")
    assert result is None


def test_note_delete(mk_creoson_post_None, mk_getactivefile):
    """Test delete."""
    c = creopyson.Client()
    result = c.note_delete("name", file_="file")
    assert result is None
    result = c.note_delete("name")
    assert result is None


def test_note_exists(mk_creoson_post_dict, mk_getactivefile):
    """Test exists."""
    c = creopyson.Client()
    result = c.note_exists(file_="file", name="name")
    assert isinstance(result, (bool))
    result = c.note_exists(name=["name", "other name"])
    assert isinstance(result, (bool))


def test_note_get(mk_creoson_post_dict, mk_getactivefile):
    """Test get."""
    c = creopyson.Client()
    result = c.note_get("name", file_="file")
    assert isinstance(result, (dict))
    result = c.note_get("name")
    assert isinstance(result, (dict))


def test_note_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.note_list(
        file_="file",
        name="name",
        value="value",
        get_expanded=True
    )
    assert isinstance(result, (list))
    result = c.note_list(name=["name", "other name"])
    assert isinstance(result, (list))


def test_note_set(mk_creoson_post_None, mk_getactivefile):
    """Test set."""
    c = creopyson.Client()
    result = c.note_set(
        "name",
        file_="file",
        encoded=True,
        value="value"
    )
    assert result is None
    result = c.note_set("name")
    assert result is None
