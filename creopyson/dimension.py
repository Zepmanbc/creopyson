"""Name module."""

import requests
import json


# def copy():
#     pass


# def list_():
#     pass


# def list_detail():
#     pass


def set_(client, name, value, current_file=None):
    request = {
        "sessionId": client.sessionId,
        "command": "dimension",
        "function": "set",
        "data": {
            "name": name,
            "value": value,
            "encoded": False
        }
    }
    if current_file:
        request["data"]["file"] = current_file
        requests.post(client.server, data=json.dumps(request))


# def show():
#     pass


# def user_select():
#     pass
