"""Connection testing."""

import requests
import json
import pytest
import creopyson
# from creopyson.core import creoson_post


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.delattr("requests.sessions.Session.request")


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


@pytest.fixture
def mk_creoson_post(monkeypatch):
    def creoson_post_mk(client, request):
        status = False
        data = {}
        return (status, data)
    monkeypatch.setattr(creopyson.core, 'creoson_post', creoson_post_mk)


def test_connection_disconnect_ok(mk_creoson_post):
    c = creopyson.Client()
    c.sessionId = "12345"
    c.disconnect()
    assert c.sessionId == ""


from unittest.mock import MagicMock


def test_connection_disconnect_ok2():
    creopyson.core.creoson_post = MagicMock(return_value=(False, {}))
    c = creopyson.Client()
    c.sessionId = "12345"
    c.disconnect()
    assert c.sessionId == ""


from creopyson.core import creoson_post

def test_connection_disconnect_ok3(monkeypatch):
    def creoson_post_mk(creoson_post):
        status = False
        data = {}
        return (status, data)
    monkeypatch.setattr(creopyson.core, 'creoson_post', creoson_post_mk)
    c = creopyson.Client()
    c.sessionId = "12345"
    c.disconnect()
    assert c.sessionId == ""

def test_connection_disconnect_ok4(monkeypatch):
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
    def creoson_post_mk(client, request):
        status = False
        data = {}
        return (status, data)
    monkeypatch.setattr(creopyson.core, 'creoson_post', creoson_post_mk)
    c = creopyson.Client()
    c.connect()
    c.disconnect()
    assert c.sessionId == ""


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
