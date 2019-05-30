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
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "authorize",
        "data": {
            "user": user,
            "password": password
        }
    }

    return client.creoson_post(request)


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
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "clear_workspace",
        "data": {
            "workspace": active_workspace
        }
    }

    if workspace:
        request["data"]["workspace"] = workspace

    return client.creoson_post(request)


def create_workspace(client, workspace, context_name):
    """Create a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name
        context_name (str): Context name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "create_workspace",
        "data": {
            "workspace": workspace,
            "context": context_name
        }
    }
    return client.creoson_post(request)


def delete_workspace(client, workspace):
    """Delete a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "delete_workspace",
        "data": {
            "workspace": workspace
        }
    }

    return client.creoson_post(request)


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
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "file_checked_out",
        "data": {
            "workspace": active_workspace,
            "filename": filename
        }
    }
    if workspace:
        request["data"]["workspace"] = workspace

    return client.creoson_post(request)["checked_out"]


def get_workspace(client):
    """Retrieve the name of the active workspace on the active server.

    Args:
        client (obj): creopyson Client

    Returns:
        str: Active Workspace name.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "get_workspace",
        "data": {}
    }

    return client.creoson_post(request)["workspace"]


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
        list: List of files in the workspace correspnding to the request.

    """
    active_workspace = client.windchill_get_workspace()
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "list_workspace_files",
        "data": {
            "workspace": active_workspace,
            "filename": "*"
        }
    }
    if workspace:
        request["data"]["workspace"] = workspace
    if filename:
        request["data"]["filename"] = filename

    return client.creoson_post(request)["filelist"]


def list_workspaces(client):
    """Get a list of workspaces the user can access on the active server.

    Args:
        client (obj): creopyson Client

    Returns:
        list: List of workspaces

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "list_workspaces",
        "data": {}
    }

    return client.creoson_post(request)["workspaces"]


def server_exists(client, server_url):
    """Check whether a server exists.

    Args:
        client (obj): creopyson Client
        server_url (str): server URL or Alias

    Returns:
        Boolean: Whether the server exists

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "server_exists",
        "data": {
            "server_url": server_url
        }
    }

    return client.creoson_post(request)["exists"]


def set_server(client, server_url):
    """Select a Windchill server.

    Args:
        client (obj): creopyson Client
        server_url (str): server URL or Alias

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "set_server",
        "data": {
            "server_url": server_url
        }
    }

    return client.creoson_post(request)


def set_workspace(client, workspace):
    """Select a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "set_workspace",
        "data": {
            "workspace": workspace
        }
    }

    return client.creoson_post(request)


def workspace_exists(client, workspace):
    """Check whether a workspace exists on the active server.

    Args:
        client (obj): creopyson Client
        workspace (str): Workspace name

    Returns:
        Boolean: Whether the workspace exists

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "workspace_exists",
        "data": {
            "workspace": workspace
        }
    }

    return client.creoson_post(request)["exists"]
