"""Connection testing."""

import requests
import json
import pytest
import creopyson

from .fixtures import mk_creoson_post_None, mk_creoson_post_dict, \
    mk_creoson_post_sessionId

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


def test_connection_connect_succed(mk__creoson_post_sessionId):
    """Test when connection is ok.

    sessionId is created and retruened by creoson.

    """
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


def test_connection__creoson_post_return_data(monkeypatch):
    """Test _creoson_post returning data."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        def json(self):
            results = {
                "status": {
                    "error": False,
                    "message": "error message"
                },
                "data": "creoson result"
            }
            return results

        @property
        def status_code(self):
            return 200

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    result = c._creoson_post("function", "method", {})
    assert result == "creoson result"


def test_connection__creoson_post_return_None(monkeypatch):
    """Test _creoson_post returning None."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        def json(self):
            results = {
                "status": {
                    "error": False,
                    "message": "error message"
                }
            }
            return results

        @property
        def status_code(self):
            return 200

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    result = c._creoson_post("function", "method", {})
    assert result is None


def test_connection__creoson_post_raise_Warning(monkeypatch):
    """Test _creoson_post raise Warning."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        def json(self):
            results = {
                "status": {
                    "error": True,
                    "message": "error message"
                }
            }
            return results

        @property
        def status_code(self):
            return 200

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    with pytest.raises(RuntimeError) as pytest_wrapped_e:
        c._creoson_post("function", "method", {})
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_connection_disconnect_ok(mk__creoson_post_None):
    """Test wether client is disconnected (empty sessionId)."""
    c = creopyson.Client()
    c.sessionId = "12345"
    c.disconnect()
    assert c.sessionId == ""


def test_connection_is_creo_running_yes(mk__creoson_post_dict):
    """Test wether creo is running OK."""
    c = creopyson.Client()
    result = c.is_creo_running()
    assert result


def test_connection_kill_creo_ok(mk__creoson_post_None):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.kill_creo()
    assert result is None


def test_connection_start_creo_ok(mk__creoson_post_None):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.start_creo("C:/folder/nitro_proe_remote.bat")
    assert result is None


def test_connection_stop_creo_ok(mk__creoson_post_None):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.stop_creo()
    assert result is None
