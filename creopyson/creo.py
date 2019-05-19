"""Name module."""

from .core import creoson_post


# def cd():
#     pass


# def delete_files():
#     pass


# def get_config():
#     pass


# def get_std_color():
#     pass


def list_dirs(client, query="*"):
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "list_dirs",
        "data": {
            "dirname": query
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data['dirlist']


def list_files(client, query='*prt|*drw|*asm'):
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "list_files",
        "data": {
            "filename": query
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data['filelist']


# def mkdir():
#     pass


def pwd(client):
    request = {
        "sessionId": client.sessionId,
        "command": "creo",
        "function": "pwd"
    }
    status, data = creoson_post(client, request)
    if not status:
        return data['dirname']


# def rmdir():
#     pass


# def set_config():
#     pass


# def set_std_color():
#     pass
