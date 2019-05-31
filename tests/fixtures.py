"""Fixtures for tests."""
import creopyson
import pytest


@pytest.fixture
def mk_creoson_post_dict(monkeypatch):
    """Mock creoson_post return dict."""
    def fake_func(client, command, function, data=None):
        return {
            "active": True,
            "checked_out": True,
            "columns": [],
            "contourlist": [],
            "dirname": "dirname",
            "dimlist": [],
            "dirlist": [],
            "drawing": "drawing",
            "exists": True,
            "errors": True,
            "file": "file",
            "filelist": [],
            "files": [],
            "instances": [],
            "itemlist": [],
            "layers": [],
            "loaded": True,
            "name": "name",
            "num_sheets": 4,
            "paramlist": [],
            "parents": [],
            "relations": [],
            "running": True,
            "scale": 1.5,
            "size": "size",
            "sheet": 4,
            "symbols": [],
            "transform": {"fake obj": 123},
            "units": "units",
            "values": [],
            "viewlist": [],
            "views": [],
            "workspace": "workspace",
            "workspaces": [],
        }
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_None(monkeypatch):
    """Mock creoson_post return None."""
    def fake_func(client, command, function, data=None):
        return None
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_list(monkeypatch):
    """Mock creoson_post return list."""
    def fake_func(client, command, function, data=None):
        return ['information']
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)