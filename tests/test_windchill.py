"""Windchill testing."""

import creopyson
import pytest


@pytest.fixture
def mk_creoson_post_T(monkeypatch):
    """Mock creoson_post, error, error message."""
    def fake_func(client, request):
        status = True
        data = "error message"
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


@pytest.fixture
def mk_creoson_post_F_None(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = None
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


##############################################
##########  authorize               ##########
##############################################
def test_windchill_authorize_ok(mk_creoson_post_F_None):
    """Test windchill_authorize ok."""
    c = creopyson.Client()
    result = c.windchill_authorize("login", "password")
    assert result is None


def test_windchill_authorize_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_authorize("login", "password")
    assert pytest_wrapped_e.value.args[0] == "error message"

##############################################
##########  clear_workspace         ##########
##############################################
def test_windchill_clear_workspace(monkeypatch, mk_creoson_post_F_None):
    """Test windchill_clear_workspace ok."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    result = c.windchill_clear_workspace("MyWorkspace")
    assert result is None

############################################
# @pytest.fixture
# def mk_windchill_get_workspace(monkeypatch):
#     def fake_func():
#         return "worskpace"
#     monkeypatch.setattr(creopyson.connection, 'windchill_get_workspace', fake_func)

# def test_windchill_clear_workspace2(mk_creoson_post_F_None, mk_windchill_get_workspace):
#     """Test windchill_clear_workspace ok."""
#     c = creopyson.Client()
#     result = c.windchill_clear_workspace("MyWorkspace")
#     assert result is None
########################################

def test_windchill_clear_workspace_error(monkeypatch, mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_clear_workspace("MyWorkspace")
    assert pytest_wrapped_e.value.args[0] == "error message"

##############################################
##########  create_workspace        ##########
##############################################
def test_windchill_create_workspace(mk_creoson_post_F_None):
    """Test windchill_create_workspace ok."""
    c = creopyson.Client()
    result = c.windchill_create_workspace("MyWorkspace", "Context")
    assert result is None


def test_windchill_create_workspace_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_create_workspace("MyWorkspace", "Context")
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  delete_workspace        ##########
##############################################
def test_windchill_delete_workspace(mk_creoson_post_F_None):
    """Test windchill_delete_workspace ok."""
    c = creopyson.Client()
    result = c.windchill_delete_workspace("MyWorkspace")
    assert result is None


def test_windchill_delete_workspace_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_delete_workspace("MyWorkspace")
    assert pytest_wrapped_e.value.args[0] == "error message"

##############################################
##########  file_checked_out        ##########
##############################################
@pytest.fixture
def mk_creoson_post_F_checked_out(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"checked_out": True}
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


def test_windchill_file_checked_out_ok(monkeypatch, mk_creoson_post_F_checked_out):
    """Test file_checked_out ok."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    result = c.windchill_file_checked_out("myfile.prt", workspace="workspace_name")
    assert result is True


def test_windchill_file_checked_out_error(monkeypatch, mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_file_checked_out("myfile.prt")
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  get_workspace           ##########
##############################################
@pytest.fixture
def mk_creoson_post_F_Workspace(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"workspace": "workspace"}
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


def test_windchill_get_workspace_ok(mk_creoson_post_F_Workspace):
    """Test windchill_authorize ok."""
    c = creopyson.Client()
    result = c.windchill_get_workspace()
    assert isinstance(result, (str))


def test_windchill_get_workspace_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_get_workspace()
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  list_workspace_files    ##########
##############################################
@pytest.fixture
def mk_creoson_post_F_filelist(monkeypatch):
    """Mock creoson_post, no error, no data."""
    def fake_func(client, request):
        status = False
        data = {"filelist": ["file1.prt", "file2.prt"]}
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


def test_windchill_list_workspace_files_ok(monkeypatch, mk_creoson_post_F_filelist):
    """Test list_workspace_files ok."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    result = c.windchill_list_workspace_files(filename = "*.prt", workspace="workspace_name")
    assert isinstance(result, (list))


def test_windchill_list_workspace_files_error(monkeypatch, mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    def fake_func():
        return "workspace"
    monkeypatch.setattr(c, 'windchill_get_workspace', fake_func)
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_list_workspace_files()
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  list_workspaces         ##########
##############################################
@pytest.fixture
def mk_creoson_post_F_workspaces(monkeypatch):
    """Mock creoson_post, no error, list."""
    def fake_func(client, request):
        status = False
        data = {"workspaces": ["workspace1", "workspace2"]}
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


def test_windchill_list_workspaces_ok(mk_creoson_post_F_workspaces):
    """Test list_workspaces ok."""
    c = creopyson.Client()
    result = c.windchill_list_workspaces()
    assert isinstance(result, (list))


def test_windchill_list_workspaces_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_list_workspaces()
    assert pytest_wrapped_e.value.args[0] == "error message"

##############################################
##########  server_exists            #########
##############################################
@pytest.fixture
def mk_creoson_post_F_exists(monkeypatch):
    """Mock creoson_post, no error, boolean."""
    def fake_func(client, request):
        status = False
        data = {"exists": True}
        return (status, data)
    monkeypatch.setattr(creopyson.windchill, 'creoson_post', fake_func)


def test_windchill_server_exists_ok(mk_creoson_post_F_exists):
    """Test server_exists ok."""
    c = creopyson.Client()
    result = c.windchill_server_exists("server_path")
    assert result is True


def test_windchill_server_exists_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_server_exists("server_path")
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  set_server               #########
##############################################
def test_windchill_set_server_ok(mk_creoson_post_F_None):
    """Test set_server ok."""
    c = creopyson.Client()
    result = c.windchill_set_server("server_path")
    assert result is None


def test_windchill_set_server_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_set_server("server_path")
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  set_workspace            #########
##############################################
def test_windchill_set_workspace_ok(mk_creoson_post_F_None):
    """Test set_workspace ok."""
    c = creopyson.Client()
    result = c.windchill_set_workspace("workspace_name")
    assert result is None


def test_windchill_set_workspace_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_set_workspace("workspace_name")
    assert pytest_wrapped_e.value.args[0] == "error message"


##############################################
##########  workspace_exists         #########
##############################################
def test_windchill_workspace_exists_ok(mk_creoson_post_F_exists):
    """Test workspace_exists ok."""
    c = creopyson.Client()
    result = c.windchill_workspace_exists("server_path")
    assert result is True


def test_windchill_workspace_exists_error(mk_creoson_post_T):
    """Test creoson return error."""
    c = creopyson.Client()
    with pytest.raises(Warning) as pytest_wrapped_e:
        c.windchill_workspace_exists("server_path")
    assert pytest_wrapped_e.value.args[0] == "error message"
