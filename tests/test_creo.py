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
def mk_creoson_post_F_None(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = None
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_F_data(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {}
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
def mk_creoson_post_F_filelist(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"filelist": ["fakefile.prt"]}
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


def test_creo_delete_files_ok(mk_creoson_post_F_filelist):
    """Test creo_delete_files ok."""
    c = creopyson.Client()
    result = c.creo_delete_files()
    assert isinstance(result, (list))
    result = c.creo_delete_files(
        dirname="C:/somewhere/",
        filename="fakefile.prt")
    assert isinstance(result, (list))
    listfakefile = ["123", "456"]
    result = c.creo_delete_files(filename=listfakefile)
    assert isinstance(result, (list))


def test_creo_delete_files_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_delete_files(filename="fake_file.prt")
    assert pytest_wrapped_e.value.args[0] == "error message"


@pytest.fixture
def mk_creoson_post_F_values(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"values": "values"}
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


def test_creo_get_config_ok(mk_creoson_post_F_values):
    """Test creo_get_config ok."""
    c = creopyson.Client()
    result = c.creo_get_config("option")
    assert result


def test_creo_get_config_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_get_config("option")
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_get_std_color_ok(mk_creoson_post_F_data):
    """Test creo_get_std_color ok."""
    c = creopyson.Client()
    result = c.creo_get_std_color("letter")
    assert isinstance(result, (dict))


def test_creo_get_std_color_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_get_std_color("letter")
    assert pytest_wrapped_e.value.args[0] == "error message"


@pytest.fixture
def mk_creoson_post_F_dirlist(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"dirlist": ["directory"]}
        return (status, data)
    monkeypatch.setattr(creopyson.creo, 'creoson_post', fake_func)


def test_creo_list_dirs_ok(mk_creoson_post_F_dirlist):
    """Test creo_list_dirs ok."""
    c = creopyson.Client()
    result = c.creo_list_dirs("filter_*")
    assert isinstance(result, (list))


def test_creo_list_dirs_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_list_dirs()
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_list_files_ok(mk_creoson_post_F_filelist):
    """Test creo_list_dirs ok."""
    c = creopyson.Client()
    result = c.creo_list_files("filter_*")
    assert isinstance(result, (list))


def test_creo_list_files_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_list_files()
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_mkdir_ok(mk_creoson_post_F_dirname):
    """Test creo_mkdir ok."""
    c = creopyson.Client()
    result = c.creo_mkdir("new_dir")
    assert isinstance(result, (str))


def test_creo_mkdir_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_mkdir("C:/Workdir/")
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_pwd_ok(mk_creoson_post_F_dirname):
    """Test creo_pwd ok."""
    c = creopyson.Client()
    result = c.creo_pwd()
    assert isinstance(result, (str))


def test_creo_pwd_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_pwd()
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_rmdir_ok(mk_creoson_post_F_None):
    """Test creo_rmdir ok."""
    c = creopyson.Client()
    result = c.creo_rmdir("fake_dir")
    assert result is None


def test_creo_rmdir_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_rmdir("folder_to_delete")
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_set_config_ok(mk_creoson_post_F_None):
    """Test creo_set_config ok."""
    c = creopyson.Client()
    result = c.creo_set_config("option", 12, True)
    assert result is None


def test_creo_set_config_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_set_config("option", 12)
    assert pytest_wrapped_e.value.args[0] == "error message"


def test_creo_set_std_color_ok(mk_creoson_post_F_None):
    """Test creo_set_std_color ok."""
    c = creopyson.Client()
    result = c.creo_set_std_color("letter", 0, 0, 0)
    assert result is None


def test_creo_set_std_color_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.creo_set_std_color("letter", 0, 0, 0)
    assert pytest_wrapped_e.value.args[0] == "error message"
