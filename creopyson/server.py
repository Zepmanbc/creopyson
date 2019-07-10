"""Server module."""

import requests
import json
import re


def pwd(client):
    """Return the creoson server's execution directory.

    Args:
        client (obj):
            creopyson Client.

    Raises:
        Warning: error message from creoson.

    Returns:
        (str): Full name of working directory.

    """
    request = {
        "sessionId": client.sessionId,
        "command": "server",
        "function": "pwd",
    }
    # ask `http://localhost:9056/server` vs `http://localhost:9056/creoson`
    server_adress = re.sub(r'creoson$', 'server',  client.server)
    r = requests.post(server_adress, data=json.dumps(request))
    json_result = r.json()
    status = json_result["status"]["error"]

    if not status:
        return json_result["data"]["dirname"]
    else:
        raise Warning(json_result["status"]["message"])
