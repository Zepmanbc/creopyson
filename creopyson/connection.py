"""Connection module."""
import requests
import json
import sys


class Client(object):
    """Creates Client object."""

    def __init__(self, ip_adress="localhost", port=9056):
        """Create Cleint objet. Define server and sessionID vars."""
        self.server = "http://{}:{}/creoson".format(ip_adress, port)
        self.sessionId = ''

################################################
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
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        if r.status_code == 200:
            try:
                json_result = r.json()
            except AttributeError:
                print("No JSON result.")
            if 'sessionId' in json_result.keys():
                self.sessionId = json_result['sessionId']
            else:
                raise KeyError("No sessionID available.")
        else:
            raise ConnectionError()

############################################################
# TODO refactoriser connect qui ressemble bcp à creoson_post
# TODO docstring
    def creoson_post(self, command, function, data=None, key_data=None):
        """Send a POST request to creoson server.

        Args:
            request (dict): Command for creoson.

        Raises:
            RuntimeError: error message from creoson.
            ConnectionError: creoson not reachable.
            AttributeError: bad creoson return.

        Returns:
            (depends request): creoson return.

        """
        request = {
            "sessionId": self.sessionId,
            "command": command,
            "function": function,
            "data": data
        }
        try:
            r = requests.post(self.server, data=json.dumps(request))
        except requests.exceptions.RequestException as e:
            sys.exit(e)
        if r.status_code == 200:
            try:
                json_result = r.json()
            except AttributeError:
                print("No JSON result.")
            if "status" in json_result.keys():
                status = json_result["status"]["error"]
                if status:
                    error_msg = json_result["status"]["message"]
                    raise RuntimeError(error_msg)
                else:
                    if key_data:
                        if key_data in json_result["data"].keys():
                            return json_result["data"][key_data]
                        else:
                            raise KeyError("`{}` not in creoson result".format(key_data))
                    return json_result.get("data", None)
                # TODO tester la présence de data
                # TODO ajouter un raise de chaque keyvalue error de tous les modules
        else:
            raise ConnectionError()

    def disconnect(self):
        """Disconnect from CREOSON.

        Empty sessionId.
        """
        self.creoson_post("connection", "disconnect")
        self.sessionId = ''

    def is_creo_running(self):
        """Check whether Creo is running.

        This function tests whether the current connection is still active;
        if there is no active connection, then it tries to make a new
        connection to Creo and returns whether the connection succeeds.
        The sessionId is optional, and ignored.

        Raises:
            Warning: error message from creoson.

        Returns:
            (boolean): True if Creo is running, False instead.

        """
        # return self.creoson_post("connection", "is_creo_running")["running"]
        return self.creoson_post(
            "connection",
            "is_creo_running",
            key_data="running"
        )

    def kill_creo(self):
        """Kill primary Creo processes.

        This will kill the 'xtop.exe' and 'nmsd.exe' processes by name.
        The sessionId is optional, and ignored.

        Raises:
            Warning: error message from creoson.

        Returns:
            None

        """
        return self.creoson_post("connection", "kill_creo")

    def start_creo(self, path, retries=0):
        """Execute an external .bat file to start Creo.

        Then attempts to connect to Creo.

        The .bat file is restricted to a specific name to make the
        function more secure. (nitro_proe_remote.bat)
        Set retries to 0 to NOT attempt to connect to Creo.
        The server will pause for 3 seconds before attempting a
        connection, and will pause for 10 seconds between
        connection retries", "If Creo pops up a message after startup,
        this function may cause Creo to crash unless retries is set to 0.

        Args:
            path (string):
                path to the .bat file (must be full path)
                will be split in 'start_command' and 'start_dir'
            retries (int):
                Number of retries to make when connecting
                (default 0)

        Raises:
            Warning: error message from creoson.

        Returns:
            None

        """
        start_command = path.split('/')[-1]
        start_dir = path.replace(start_command, '')[:-1]
        data = {
            "start_dir": start_dir,
            "start_command": start_command,
            "retries": retries
        }
        return self.creoson_post("connection", "start_creo", data)

    def stop_creo(self):
        """Disconnect current session from Creo and cause Creo to exit.

        NOTE that this will cause Creo to exit cleanly.
        If there is no current connection to Creo, this function
        will do nothing.

        Raises:
            Warning: error message from creoson.

        Returns:
            None

        """
        return self.creoson_post("connection", "stop_creo")
