"""Connection testing."""

import requests
import json
import pytest
import creopyson
# from creopyson.core import creoson_post


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


@pytest.fixture
def mk_creoson_post_F_no_data(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {}
        return (status, data)
    monkeypatch.setattr(creopyson.connection, 'creoson_post', fake_func)


def test_connection_disconnect_ok(mk_creoson_post_F_no_data):
    """Test wether client is disconnected (empty sessionId)."""
    c = creopyson.Client()
    c.sessionId = "12345"
    c.disconnect()
    assert c.sessionId == ""

@pytest.fixture
def mk_creoson_post_F_running(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"running": True}
        return (status, data)
    monkeypatch.setattr(creopyson.connection, 'creoson_post', fake_func)

def test_connection_is_creo_running_yes(mk_creoson_post_F_running):
    """Test wether creo is running OK."""
    c = creopyson.Client()
    result = c.is_creo_running()
    assert result

@pytest.fixture
def mk_creoson_post_T(monkeypatch):
    """Mock creoson_post, error, error message."""
    def fake_func(client, request):
        status = True
        data = "error message"
        return (status, data)
    monkeypatch.setattr(creopyson.connection, 'creoson_post', fake_func)


def test_connection_is_creo_running_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.is_creo_running()
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_connection_kill_creo_ok(mk_creoson_post_F_no_data):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.kill_creo()
    assert result is None


def test_connection_kill_creo_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.kill_creo()
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_connection_start_creo_ok(mk_creoson_post_F_no_data):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.start_creo("C:/folder/nitro_proe_remote.bat")
    assert result is None


def test_connection_start_creo_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.start_creo("C:/folder/nitro_proe_remote.bat")
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_connection_stop_creo_ok(mk_creoson_post_F_no_data):
    """Test no error returned from creoson."""
    c = creopyson.Client()
    result = c.stop_creo()
    assert result is None


def test_connection_stop_creo_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.stop_creo()
    assert pytest_wrapped_e.value.args[0] == "error message"


# TODO is it necessary?
def test_connection_wrapper_ok():
    from creopyson.connection import make_api_method

    class fakeobj():
        def __init__(self):
            pass

    def fakefunc():
        pass

    assert "fakefunc" not in dir(fakeobj)
    fakeobj.fakefunc = make_api_method(fakefunc)
    assert "fakefunc" in dir(fakeobj)

    print("toto")


def test_connection_wrapper_error():
    from creopyson.connection import make_api_method
    fakeobj = object()

    def fakefunc():
        pass
    with pytest.raises(AttributeError) as pytest_wrapped_e:
        fakeobj.add_fakefunc = make_api_method(fakefunc)
    assert pytest_wrapped_e.value.args[0] == \
        "'object' object has no attribute 'add_fakefunc'"
