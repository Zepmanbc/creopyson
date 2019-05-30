"""Fixtures for tests."""
import creopyson
import pytest


@pytest.fixture
def mk_creoson_post_boolean(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return True
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_dict(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return {
            "running": True,
            "checked_out": True,
            "dirname": "dirname",
            "dirlist": [],
            "exists": True,
            "filelist": [],
            "values": [],
            "workspace": "",
            "workspaces": [],
        }
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_list(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return []
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_str(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return ""
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_None(monkeypatch):
    """Mock creoson_postreturn dict."""
    def fake_func(client, command, function, data=None):
        return None
    monkeypatch.setattr(creopyson.connection.Client, 'creoson_post', fake_func)
