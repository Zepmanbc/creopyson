"""Creo testing."""
import creopyson
from creopyson.exceptions import MissingKey
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None


def test_creo_cd(mk_creoson_post_dict):
    """Test creo_cd."""
    c = creopyson.Client()
    dirname = "C:\\User\\Working directory\\"
    result = c.creo_cd(dirname)
    assert isinstance(result, (str))


def test_creo_delete_files(mk_creoson_post_dict):
    """Test creo_delete_files."""
    c = creopyson.Client()
    result = c.creo_delete_files()
    assert isinstance(result, (list))
    result = c.creo_delete_files(dirname="C:/dir/", filename="fake_file.prt")
    assert isinstance(result, (list))
    result = c.creo_delete_files(filename=["C:/dir/fake_file.prt"])
    assert isinstance(result, (list))


def test_creo_get_config(mk_creoson_post_dict):
    """Test creo_get_config."""
    c = creopyson.Client()
    result = c.creo_get_config("option")
    assert isinstance(result, (list))


def test_creo_get_std_color(mk_creoson_post_dict):
    """Test creo_get_std_color."""
    c = creopyson.Client()
    result = c.creo_get_std_color("letter")
    assert isinstance(result, (dict))


def test_creo_list_dirs(mk_creoson_post_dict):
    """Test creo_list_dirs."""
    c = creopyson.Client()
    result = c.creo_list_dirs("filter_*")
    assert isinstance(result, (list))
    result = c.creo_list_dirs()
    assert isinstance(result, (list))


def test_creo_list_dirs_empty(monkeypatch):
    """Correction issue #1.

    if there is no folder in directory, creoson does not return `data`.
    Need to return an empty list.
    """

    def fake_func(client, command, function, data=None, key_data=None):
        raise MissingKey("Missing `data` in creoson return")

    monkeypatch.setattr(creopyson.connection.Client, "_creoson_post", fake_func)
    c = creopyson.Client()
    result = c.creo_list_dirs()
    assert result == []


def test_creo_list_files(mk_creoson_post_dict):
    """Test creo_list_dirs."""
    c = creopyson.Client()
    result = c.creo_list_files("filter_*")
    assert isinstance(result, (list))


def test_creo_mkdir(mk_creoson_post_dict):
    """Test creo_mkdir."""
    c = creopyson.Client()
    result = c.creo_mkdir("new_dir")
    assert isinstance(result, (str))


def test_creo_pwd(mk_creoson_post_dict):
    """Test creo_pwd."""
    c = creopyson.Client()
    result = c.creo_pwd()
    assert isinstance(result, (str))


def test_creo_rmdir_ok(mk_creoson_post_None):
    """Test creo_rmdir."""
    c = creopyson.Client()
    result = c.creo_rmdir("fake_dir")
    assert result is None


def test_creo_set_config_ok(mk_creoson_post_None):
    """Test creo_set_config."""
    c = creopyson.Client()
    result = c.creo_set_config("option", 12, True)
    assert result is None


def test_creo_set_creo_version(mk_creoson_post_None):
    """Test creo_set_creao_version."""
    c = creopyson.Client()
    result = c.creo_set_creo_version(7)
    assert result is None


def test_creo_set_std_color_ok(mk_creoson_post_None):
    """Test creo_set_std_color."""
    c = creopyson.Client()
    result = c.creo_set_std_color("letter", 0, 0, 0)
    assert result is None
