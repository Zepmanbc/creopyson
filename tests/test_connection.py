"""Connection testing."""

import requests
import json
import pytest
import creopyson


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


# def test_connection_disconnect_ok():
# def test_connection_disconnect_error():
# def test_connection_is_creo_running_yes():
# def test connection_is_crei_running_no():
# def test connection_is_crei_running_error():
# def test_connection_kill_creo_ok():
# def test_connection_kill_creo_error():
# def test_connection_start_cre_ok():
# def test_connection_start_cre_error():
# def test_connection_stop_cre_ok():
# def test_connection_stop_cre_error():
