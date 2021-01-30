"""Fixtures for tests."""
import creopyson
import pytest


@pytest.fixture
def mk_creoson_post_dict(monkeypatch):
    """Mock _creoson_post return dict."""
    def fake_func(client, command, function, data=None, key_data=None):
        if key_data:
            result = {
                "active": True,
                "checked_out": True,
                "children": [],
                "columns": [],
                "contourlist": [],
                "dirname": "dirname",
                "dimlist": [],
                "dirlist": [],
                "drawing": "drawing",
                "exists": True,
                "errors": True,
                "featlist": [],
                "file": "file",
                "filelist": [],
                "files": [],
                "instances": [],
                "itemlist": [],
                "layers": [],
                "loaded": True,
                "material": "material",
                "materials": [],
                "name": "name",
                "num_sheets": 4,
                "paramlist": [],
                "parents": [],
                "relations": [],
                "running": True,
                "scale": 1.5,
                "size": "size",
                "sheet": 4,
                "surflist": [],
                "symbols": [],
                "transform": {"fake obj": 123},
                "units": "units",
                "values": [],
                "viewlist": [],
                "views": [],
                "workspace": "workspace",
                "workspaces": [],
            }
            return result[key_data]
        else:
            return {}
    monkeypatch.setattr(
        creopyson.connection.Client, '_creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_None(monkeypatch):
    """Mock _creoson_post return None."""
    def fake_func(client, command, function, data=None, key_data=None):
        return None
    monkeypatch.setattr(
        creopyson.connection.Client, '_creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_list(monkeypatch):
    """Mock _creoson_post return list."""
    def fake_func(client, command, function, data=None, key_data=None):
        return ['information']
    monkeypatch.setattr(
        creopyson.connection.Client, '_creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_sessionId(monkeypatch):
    """Mock _creoson_post return dict."""
    def fake_func(client, command, function, data=None, key_data=None):
        return "123456"
    monkeypatch.setattr(
        creopyson.connection.Client, '_creoson_post', fake_func)


@pytest.fixture
def mk_getactivefile(monkeypatch):
    """Mock file_get_active()."""
    def fake_func(client):
        return {
            "file": "file.prt"
        }
    monkeypatch.setattr(
        creopyson.connection.Client, "file_get_active", fake_func)
