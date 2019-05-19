"""Name module."""

from .core import creoson_post


# def export_3dpdf():
#     pass


# def export_file():
#     pass


# def export_image():
#     pass


def export_pdf(client, current_file):
    """Export pdf file.

    Args:
        client (obj): creopyson Client
        current_file (str): file name

    Returns:
        dict: export path

    """
    request = {
        "sessionId": client.sessionId,
        "command": "interface",
        "function": "export_pdf",
        "data": {
            "file": current_file
        }
    }
    status, data = creoson_post(client, request)
    if not status:
        return data


# def export_program():
#     pass


# def import_program():
#     pass


# def mapkey():
#     pass


# def plot():
#     pass
