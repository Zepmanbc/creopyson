"""Windchill module.

Connect to Windchill server, use workspaces (create/delete/list)
List files and checkout status.

"""

from .core import creoson_post


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
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def clear_workspace(client, workspace_name):
    """Clear a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace_name (str): workspace name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "clear_workspace",
        "data": {
            "workspace": workspace_name
        }
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def create_workspace(client, workspace_name, context_name):
    """Create a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace_name (str): Workspace name
        context_name (str): Context name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "create_workspace",
        "data": {
            "workspace": workspace_name,
            "context": context_name
        }
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def delete_workspace(client, workspace_name):
    """Delete a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace_name (str): Workspace name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "delete_workspace",
        "data": {
            "workspace": workspace_name
        }
    }
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def file_checked_out(client, workspace_name, filename):
    """Check whether a file is checked out in a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace_name (str): Workspace name
        filename (str): File name

    Returns:
        Boolean: Whether the file is checked out in the workspace.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "file_checked_out",
        "data": {
            "workspace": workspace_name,
            "filename": filename
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["checked_out"]


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
        "function": "get_workspace"
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["workspace"]


def list_workspace_files(client, filename=None):
    """Get a list of files in a workspace on the active server.

    Args:
        client (obj): creopyson Client
        filename (str, optional): File name or search. Defaults to None.
            ex: `*.asm`, `screw_*.prt`

    Returns:
        list: List of files in the workspace correspnding to the request.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "list_workspace_files",
    }
    if filename:
        request["data"]["filename"] = filename
    status, data = creoson_post(client, request)
    if not status:
        return data["filelist"]


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
        "function": "list_workspaces"
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["workspaces"]


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
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]


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
    status, data = creoson_post(client, request)
    if status:
        raise Warning(data)


def set_workspace(client, workspace_name):
    """Select a workspace on the active server.

    Args:
        client (obj): creopyson Client
        workspace_name (str): Workspace name

    Returns:
        None

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "set_workspace",
        "data": {
            "workspace": workspace_name
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        raise Warning(data)


def workspace_exists(client, workspace_name):
    """Check whether a workspace exists on the active server.

    Args:
        client (obj): creopyson Client
        workspace_name (str): Workspace name

    Returns:
        Boolean: Whether the workspace exists

    """
    request = {
        "sessionId": client.sessionId,
        "command": "windchill",
        "function": "workspace_exists",
        "data": {
            "workspace": workspace_name
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data["exists"]
