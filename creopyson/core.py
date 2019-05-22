"""Core module."""

import requests
import json


def creoson_post(client, request):
    """Send a POST request to creoson server.

    Args:
        client (obj): creopyson Client.
        request (dict): Command for creoson.

    Returns:
        (dict):
            status (boolean):
                'True' if creoson return an error
                'False" if creoson is ok
            data (dict):
                creoson return (it depend the request)

    """
    r = requests.post(client.server, data=json.dumps(request))
    json_result = json.loads(r.content)
    status = json_result["status"]["error"]
    if status:
        data = json_result["status"]["message"]
    else:
        if "data" in json_result.keys():
            data = json_result["data"]
        else:
            data = None
    return status, data
