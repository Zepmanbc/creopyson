"""Creo testing."""

import creopyson
import pytest
# import requests
# import json


@pytest.fixture
def mk_creoson_post_T(monkeypatch):
    """Mock creoson_post, error, error message."""
    def fake_func(client, request):
        status = True
        data = "error message"
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_F_dirname(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"dirname": "C:\\User\\Working directory\\"}
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


def test_creo_cd_ok(mk_creoson_post_F_dirname):
    """Test creo_cd ok."""
    c = creopyson.Client()
    dirname = "C:\\User\\Working directory\\"
    result = c.creo_cd(dirname)
    assert result == dirname


def test_creo_cd_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_cd("fake_path")
    assert pytest_wrapped_e.value.args[0] == "error message"


@pytest.fixture
def mk_creoson_post_F_dilelist(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"filelist": ["fakefile.prt"]}
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


def test_creo_delete_files_ok(mk_creoson_post_F_dilelist):
    """Test creo_delete_files ok."""
    c = creopyson.Client()
    result = c.creo_delete_files()
    assert isinstance(result, (list))


def test_creo_delete_files_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_delete_files(filename="fake_file.prt")
    assert pytest_wrapped_e.value.args[0] == "error message"
