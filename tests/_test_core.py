"""Core testing."""

from creopyson.core import creoson_post
import creopyson
import requests
import json


def test_core_creoson_post_return_error_msg(monkeypatch):
    """Test when creoson return an error message."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "status": {
                    "error": True,
                    "message": "Error message"
                },
                "data": None
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)

    c = creopyson.Client()

    status, data = creoson_post(c, None)

    assert status
    assert data == "Error message"


def test_core_creoson_post_return_data(monkeypatch):
    """Test when creoson return data."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "status": {
                    "error": False,
                    "message": "Error message"
                },
                "data": {
                    "random_data": 12345,
                }
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)

    c = creopyson.Client()

    status, data = creoson_post(c, None)

    assert not status
    assert data
    assert isinstance(data, dict)


def test_core_creoson_post_return_None(monkeypatch):
    """Test when creoson return nothing."""
    class Mk_post():
        def __init__(self, *args, **kwargs):
            pass

        @property
        def content(self):
            results = {
                "status": {
                    "error": False,
                    "message": "Error message"
                },
            }
            return json.dumps(results).encode()

    monkeypatch.setattr(requests, 'post', Mk_post)

    c = creopyson.Client()

    status, data = creoson_post(c, None)

    assert not status
    assert data is None
