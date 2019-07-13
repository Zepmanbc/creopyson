"""Test server Module."""

import requests
import json
import pytest
import creopyson


def test_server_pwd_ok(monkeypatch):
    """Test server_pwd ok."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        def json(self):
            results = {
                "status": {
                    "error": False,
                },
                "data": {
                    "dirname": "C:/CreosonServer-2.3.0-win64"
                }
            }
            return results

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    result = c.server_pwd()
    assert result == "C:/CreosonServer-2.3.0-win64"


def test_server_pwd_error(monkeypatch):
    """Test creoson return error."""
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

    monkeypatch.setattr(requests, 'post', Mk_post)
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.server_pwd()
    assert pytest_wrapped_e.value.args[0] == "error message"
