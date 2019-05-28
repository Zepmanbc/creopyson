"""Creo testing."""

import creopyson
import pytest


@pytest.fixture
def mk_creoson_post_T(monkeypatch):
    """Mock creoson_post, error, error message."""
    def fake_func(client, request):
        status = True
        data = "error message"
        return (status, data)
    monkeypatch.setattr(creopyson.bom, 'creoson_post', fake_func)
  

def test_bom_get_paths_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.bom_get_paths("fake_path")
    assert pytest_wrapped_e.value.args[0] == "error message"


@pytest.fixture
def mk_creoson_post_F_data(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {}
        return (status, data)
    monkeypatch.setattr(creopyson.bom, 'creoson_post', fake_func)


def test_bom_get_paths_ok(mk_creoson_post_F_data):
    """Test bom_get_paths ok."""
    c = creopyson.Client()
    result = c.bom_get_paths(
        file_="",
        paths=True,
        skeletons=True,
        top_level=True,
        get_transforms=True,
        exclude_inactive=True
    )
    assert isinstance(result, (dict))