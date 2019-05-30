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
            "dirname": "dirname",
            "dimlist": [],
            "dirlist": [],
            "exists": True,
            "errors": True,
            "file": "file",
            "filelist": [],
            "files": [],
            "relations": [],
            "running": True,
            "transform": {"fake obj": 123},
            "units": "units",
            "values": [],
            "viewlist": [],
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
