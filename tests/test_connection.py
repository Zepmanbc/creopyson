"""Connection testing."""

import requests
import json
import pytest
import creopyson

from .fixtures import mk_creoson_post_None, mk_creoson_post_dict

# @pytest.fixture(autouse=True)
# def no_requests(monkeypatch):
#     monkeypatch.delattr("requests.sessions.Session.request")


def test_connection_wether_params_exists():
    """Test wether connection vars are created and well generated."""
    c = creopyson.Client()
    assert c.server == "http://localhost:9056/creoson"
    assert c.sessionId == ''

    c = creopyson.Client(ip_adress="here", port=1234)
    assert c.server == "http://here:1234/creoson"


def test_connection_connect_succed(monkeypatch):
    """Test when connection is ok.

    sessionId is created and retruened by creoson.

    """
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "sessionId": "123456"
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    c.connect()
    assert c.sessionId == "123456"


def test_connection_connect_fails(monkeypatch):
    """Test when connection fails and exit."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            raise requests.exceptions.RequestException

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        c.connect()
    assert pytest_wrapped_e.type == SystemExit


def test_connection_creoson_post_return_data(monkeypatch):
    """Test creoson_post returning data."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "status": {
                    "error": False,
                    "message": "error message"
                },
                "data": "creoson result"
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    result = c.creoson_post("function", "method", {})
    assert result == "creoson result"


def test_connection_creoson_post_return_None(monkeypatch):
    """Test creoson_post returning None."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "status": {
                    "error": False,
                    "message": "error message"
                }
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    result = c.creoson_post("function", "method", {})
    assert result is None


def test_connection_creoson_post_raise_Warning(monkeypatch):
    """Test creoson_post raise Warning."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "status": {
                    "error": True,
                    "message": "error message"
                }
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creoson_post("function", "method", {})
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_connection_disconnect_ok(mk_creoson_post_None):
    """Test wether client is disconnected (empty sessionId)."""
    c = creopyson.Client()
    c.sessionId = "12345"
    c.disconnect()
    assert c.sessionId == ""


def test_connection_is_creo_running_yes(mk_creoson_post_dict):
    """Test wether creo is running OK."""
    c = creopyson.Client()
    result = c.is_creo_running()
    assert result


def test_connection_kill_creo_ok(mk_creoson_post_None):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.kill_creo()
    assert result is None


def test_connection_start_creo_ok(mk_creoson_post_None):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.start_creo("C:/folder/nitro_proe_remote.bat")
    assert result is None


def test_connection_stop_creo_ok(mk_creoson_post_None):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.stop_creo()
    assert result is None
