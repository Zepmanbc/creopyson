"""Windchill testing."""

import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None


def test_windchill_authorize(mk_creoson_post_None):
    """Test windchill_authorize."""
    c = creopyson.Client()
    result = c.windchill_authorize("login", "password")
    assert result is None

def test_windchill_clear_workspace(monkeypatch, mk_creoson_post_None):
    """Test windchill_clear_workspace."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    result = c.windchill_clear_workspace("MyWorkspace")
    assert result is None


def test_windchill_create_workspace(mk_creoson_post_None):
    """Test windchill_create_workspace."""
    c = creopyson.Client()
    result = c.windchill_create_workspace("MyWorkspace", "Context")
    assert result is None


def test_windchill_delete_workspace(mk_creoson_post_None):
    """Test windchill_delete_workspace."""
    c = creopyson.Client()
    result = c.windchill_delete_workspace("MyWorkspace")
    assert result is None


def test_windchill_file_checked_out(monkeypatch, mk_creoson_post_dict):
    """Test file_checked_out."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    result = c.windchill_file_checked_out("myfile.prt", workspace="workspace_name")
    assert result is True


def test_windchill_get_workspace(mk_creoson_post_dict):
    """Test windchill_authorize."""
    c = creopyson.Client()
    result = c.windchill_get_workspace()
    assert isinstance(result, (str))


def test_windchill_list_workspace_files(monkeypatch, mk_creoson_post_dict):
    """Test list_workspace_files."""
    c = creopyson.Client()

    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    result = c.windchill_list_workspace_files(filename="*.prt", workspace="workspace_name")
    assert isinstance(result, (list))


def test_windchill_list_workspaces(mk_creoson_post_dict):
    """Test list_workspaces."""
    c = creopyson.Client()
    result = c.windchill_list_workspaces()
    assert isinstance(result, (list))


def test_windchill_server_exists(mk_creoson_post_dict):
    """Test server_exists."""
    c = creopyson.Client()
    result = c.windchill_server_exists("server_path")
    assert result is True


def test_windchill_set_server(mk_creoson_post_None):
    """Test set_server."""
    c = creopyson.Client()
    result = c.windchill_set_server("server_path")
    assert result is None


def test_windchill_set_workspace(mk_creoson_post_None):
    """Test set_workspace."""
    c = creopyson.Client()
    result = c.windchill_set_workspace("workspace_name")
    assert result is None


def test_windchill_workspace_exists(mk_creoson_post_dict):
    """Test workspace_exists."""
    c = creopyson.Client()
    result = c.windchill_workspace_exists("server_path")
    assert result is True
