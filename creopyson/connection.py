import requests
import json
import functools

from .core import creoson_post


class Client(object):

    def __init__(self, ip_adress="localhost", port=9056):
        """Create Cleint objet. Define server and sessionID vars."""
        self.server = "http://{}:{}/creoson".format(ip_adress, port)
        self.sessionId = ''

    def connect(self):
        """Connect to CREOSON.

            Define 'sessionId'.
            Exit if server not found.
        """
        request = {
            "command": "connection",
            "function": "connect"
        }
        try:
            r = requests.post(self.server, data=json.dumps(request))
            self.sessionId = json.loads(r.content)['sessionId']
        except requests.exceptions.RequestException as e:
            print(e)
            exit()

    def disconnect(self):
        """Disconnect from CREOSON.

            Empty sessionId.
            Exit if server not found.
        """
        request = {
            "sessionId": self.sessionId,
            "command": "connection",
            "function": "disconnect"
        }
        try:
            status, data = creoson_post(self, request)
            self.sessionId = ''
        except requests.exceptions.RequestException as e:
            print(e)
            exit()

    def is_creo_running(self):
        """Check whether Creo is running.

        This function tests whether the current connection is still active;
        if there is no active connection, then it tries to make a new
        connection to Creo and returns whether the connection succeeds.
        The sessionId is optional, and ignored.

        return:
            Boolean: True if Creo is running, False instead.
        """
        request = {
            "command": "connection",
            "function": "is_creo_running"
        }
        status, data = creoson_post(self, request)
        return data['running']

    def kill_creo(self):
        """Kill primary Creo processes.

            This will kill the 'xtop.exe' and 'nmsd.exe' processes by name.
            The sessionId is optional, and ignored.
        """
        request = {
            "command": "connection",
            "function": "kill_creo"
        }
        creoson_post(self, request)

    def start_creo(self, path, retries=0):
        """Execute an external .bat file to start Creo, then attempts to
            connect to Creo.

            The .bat file is restricted to a specific name to make the
            function more secure. (nitro_proe_remote.bat)
            Set retries to 0 to NOT attempt to connect to Creo.
            The server will pause for 3 seconds before attempting a
            connection, and will pause for 10 seconds between
            connection retries", "If Creo pops up a message after startup,
            this function may cause Creo to crash unless retries is set to 0.

            Args:
                path (string): path to the .bat file
                    will be split in 'start_command' and 'start_dir'
                retries (int): Number of retries to make when connecting
                    (default 0)

            Returns:
                None: 'nitro_proe_remote.bat' was found and executed
                string: "You may only specify 'nitro_proe_remote.bat'
                    for the startCommand parameter"
        """
        start_command = path.split('/')[-1]
        start_dir = path.replace(start_command, '')[:-1]
        request = {
            "command": "connection",
            "function": "start_creo",
            "data": {
                "start_dir": start_dir,
                "start_command": start_command,
                "retries": retries
            }
        }
        status, data = creoson_post(self, request)
        if status:
            return data

    def stop_creo(self):
        """Disconnect current session from Creo and cause Creo to exit.

            NOTE that this will cause Creo to exit cleanly.
            If there is no current connection to Creo, this function
            will do nothing.
        """
        request = {
            "sessionId": self.sessionId,
            "command": "connection",
            "function": "stop_creo"
        }
        creoson_post(self, request)


def make_api_method(func):
    """
    Provides a single entry point for modifying all API methods.
    For now this is limited to allowing the client object to be modified
    with an `extra_params` keyword arg to each method, that is then used
    as the params for each web service requtes.
    Please note that this is an unsupported feature for advanced use only.
    It's also currently incompatibile with multiple threads, see GH #160.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args[0]._extra_params = kwargs.pop("extra_params", None)
        result = func(*args, **kwargs)
        try:
            del args[0]._extra_params
        except AttributeError:
            pass
        return result
    return wrapper


"""Add API methods to CLient."""

# bom.py
from creopyson.bom import get_paths as bom_get_paths
Client.bom_get_paths = make_api_method(bom_get_paths)

# creo.py
from creopyson.creo import pwd
from creopyson.creo import list_dirs
from creopyson.creo import list_files
Client.pwd = make_api_method(pwd)
Client.list_dirs = make_api_method(list_dirs)
Client.list_files = make_api_method(list_files)


# dimension.py
from creopyson.dimension import set_ as dimension_set
Client.dimension_set = make_api_method(dimension_set)

# file.py
from creopyson.file import exists as file_exists
from creopyson.file import open_ as file_open
from creopyson.file import regenerate as file_regenerate
Client.file_exists = make_api_method(file_exists)
Client.file_open = make_api_method(file_open)
Client.file_regenerate = make_api_method(file_regenerate)

# interface.py
from creopyson.interface import export_pdf as interface_export_pdf
Client.interface_export_pdf = make_api_method(interface_export_pdf)
