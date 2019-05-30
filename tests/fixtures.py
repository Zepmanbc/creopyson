"""Fixtures for tests."""
import creopyson
import pytest


@pytest.fixture
def mk_creoson_post_dict(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return {
            "running": True,
            "checked_out": True,
            "dirname": "dirname",
            "dimlist": [],
            "dirlist": [],
            "exists": True,
            "filelist": [],
            "values": [],
            "workspace": "",
            "workspaces": [],
        }
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_None(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return None
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)
