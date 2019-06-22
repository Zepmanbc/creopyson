"""Windchill module.

Connect to Windchill server, use workspaces (create/delete/list)
List files and checkout status.

"""


def authorize(client, user, password):
    """Set user's Windchill login/password.

    Args:
        client (obj): creopyson Client
        user (str): user name
        password (str): password

    Returns:
        None

    """
    data = {
        "user": user,
        "password": password
    }
    return client._creoson_post("windchill", "authorize", data)


def clear_workspace(client, workspace=None):
    """Clear a workspace on the active server.

    Args:
        client (obj):
            creopyson Client
        workspace (str, optionnal):
            Workspace name. Default is current workspace.

    Returns:
        None

    """
    active_workspace = client.windchill_get_workspace()
    data = {"workspace": active_workspace}
    if workspace:
        data["workspace"] = workspace
    return client._creoson_post("windchill", "clear_workspace", data)


def create_workspace(client, workspace, context_name):
    """Create a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name
        context_name (str): Context name

    Returns:
        None

    """
    data = {
        "workspace": workspace,
        "context": context_name
    }
    return client._creoson_post("windchill", "create_workspace", data)


def delete_workspace(client, workspace):
    """Delete a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name

    Returns:
        None

    """
    data = {"workspace": workspace}
    return client._creoson_post("windchill", "delete_workspace", data)


def file_checked_out(client, filename, workspace=None):
    """Check whether a file is checked out in a workspace on the active server.

    Args:
        client (obj):
            creopyson Client
        filename (str):
            File name
        workspace (str, optionnal):
            Workspace name. Default is current workspace.

    Returns:
        Boolean: Whether the file is checked out in the workspace.

    """
    active_workspace = client.windchill_get_workspace()
    data = {
        "workspace": active_workspace,
        "filename": filename
    }
    if workspace:
        data["workspace"] = workspace
    return client._creoson_post(
        "windchill", "file_checked_out", data, "checked_out")


def get_workspace(client):
    """Retrieve the name of the active workspace on the active server.

    Args:
        client (obj): creopyson Client

    Returns:
        str: Active Workspace name.

    """
    return client._creoson_post(
        "windchill", "get_workspace", key_data="workspace")


def list_workspace_files(client, workspace=None, filename=None):
    """Get a list of files in a workspace on the active server.

    Args:
        client (obj):
            creopyson Client
        workspace (str, optionnal):
            Workspace name. Default is current workspace.
        filename (str, optional):
            File name or search. Default is all files.
            ex: `*.asm`, `screw_*.prt`

    Returns:
        list: List of files in the workspace correspnding to the data.

    """
    active_workspace = client.windchill_get_workspace()
    data = {
        "workspace": active_workspace,
        "filename": "*"
    }
    if workspace:
        data["workspace"] = workspace
    if filename:
        data["filename"] = filename
    return client._creoson_post(
        "windchill", "list_workspace_files", data, "filelist")


def list_workspaces(client):
    """Get a list of workspaces the user can access on the active server.

    Args:
        client (obj): creopyson Client

    Returns:
        list: List of workspaces

    """
    return client._creoson_post(
        "windchill", "list_workspaces", key_data="workspaces")


def server_exists(client, server_url):
    """Check whether a server exists.

    Args:
        client (obj): creopyson Client
        server_url (str): server URL or Alias

    Returns:
        Boolean: Whether the server exists

    """
    data = {"server_url": server_url}
    return client._creoson_post("windchill", "server_exists", data, "exists")


def set_server(client, server_url):
    """Select a Windchill server.

    Args:
        client (obj): creopyson Client
        server_url (str): server URL or Alias

    Returns:
        None

    """
    data = {"server_url": server_url}
    return client._creoson_post("windchill", "set_server", data)


def set_workspace(client, workspace):
    """Select a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name

    Returns:
        None

    """
    data = {"workspace": workspace}
    return client._creoson_post("windchill", "set_workspace", data)


def workspace_exists(client, workspace):
    """Check whether a workspace exists on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name

    Returns:
        Boolean: Whether the workspace exists

    """
    data = {"workspace": workspace}
    return client._creoson_post(
        "windchill", "workspace_exists", data, "exists")
