"""Connection module."""
import requests
import json
import functools

from .core import creoson_post


class Client(object):
    """Creates Client object."""

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
                path to the .bat file
                will be split in 'start_command' and 'start_dir'
            retries (int):
                Number of retries to make when connecting
                (default 0)

        Returns:
            None:
                'nitro_proe_remote.bat' was found and executed
            string:
                "You may only specify 'nitro_proe_remote.bat'
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
    """Provide a single entry point for modifying all API methods.

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
from creopyson.dimension import copy as dimension_copy
from creopyson.dimension import list_detail as dimension_list_detail
from creopyson.dimension import list_ as dimension_list
from creopyson.dimension import set_ as dimension_set
from creopyson.dimension import show as dimension_show
from creopyson.dimension import user_select as dimension_user_select
Client.dimension_copy = make_api_method(dimension_copy)
Client.dimension_list_detail = make_api_method(dimension_list_detail)
Client.dimension_list = make_api_method(dimension_list)
Client.dimension_set = make_api_method(dimension_set)
Client.dimension_show = make_api_method(dimension_show)
Client.dimension_user_select = make_api_method(dimension_user_select)

# file.py
from creopyson.file import assemble as file_assemble
from creopyson.file import backup as file_backup
from creopyson.file import close_window as file_close_window
from creopyson.file import display as file_display
from creopyson.file import erase as file_erase
from creopyson.file import erase_not_displayed as file_erase_not_displayed
from creopyson.file import exists as file_exists
from creopyson.file import get_active as file_get_active
from creopyson.file import get_fileinfo as file_get_fileinfo
from creopyson.file import get_length_units as file_get_length_units
from creopyson.file import get_mass_units as file_get_mass_units
from creopyson.file import get_transform as file_get_transform
from creopyson.file import has_instances as file_has_instances
from creopyson.file import is_active as file_is_active
from creopyson.file import list_instances as file_list_instances
from creopyson.file import list_ as file_list
from creopyson.file import list_simp_reps as file_list_simp_reps
from creopyson.file import massprops as file_massprops
from creopyson.file import open_errors as file_open_errors
from creopyson.file import open_ as file_open
from creopyson.file import postregen_relations_get as \
    file_postregen_relations_get
from creopyson.file import postregen_relations_set as \
    file_postregen_relations_set
from creopyson.file import refresh as file_refresh
from creopyson.file import regenerate as file_regenerate
from creopyson.file import relations_get as file_relations_get
from creopyson.file import relations_set as file_relations_set
from creopyson.file import rename as file_rename
from creopyson.file import repaint as file_repaint
from creopyson.file import save as file_save
from creopyson.file import set_length_units as file_set_length_units
from creopyson.file import set_mass_units as file_set_mass_units
Client.file_assemble = make_api_method(file_assemble)
Client.file_backup = make_api_method(file_backup)
Client.file_close_window = make_api_method(file_close_window)
Client.file_display = make_api_method(file_display)
Client.file_erase = make_api_method(file_erase)
Client.file_erase_not_displayed = make_api_method(file_erase_not_displayed)
Client.file_exists = make_api_method(file_exists)
Client.file_get_active = make_api_method(file_get_active)
Client.file_get_fileinfo = \
    make_api_method(file_get_fileinfo)
Client.file_get_length_units = make_api_method(file_get_length_units)
Client.file_get_mass_units = make_api_method(file_get_mass_units)
Client.file_get_transform = make_api_method(file_get_transform)
Client.file_has_instances = make_api_method(file_has_instances)
Client.file_is_active = make_api_method(file_is_active)
Client.file_list_instances = make_api_method(file_list_instances)
Client.file_list = make_api_method(file_list)
Client.file_list_simp_reps = make_api_method(file_list_simp_reps)
Client.file_massprops = make_api_method(file_massprops)
Client.file_open_errors = make_api_method(file_open_errors)
Client.file_open = make_api_method(file_open)
Client.file_postregen_relations_get = \
    make_api_method(file_postregen_relations_get)
Client.file_postregen_relations_set = \
    make_api_method(file_postregen_relations_set)
Client.file_refresh = make_api_method(file_refresh)
Client.file_regenerate = make_api_method(file_regenerate)
Client.file_relations_get = make_api_method(file_relations_get)
Client.file_relations_set = make_api_method(file_relations_set)
Client.file_rename = make_api_method(file_rename)
Client.file_repaint = make_api_method(file_repaint)
Client.file_save = make_api_method(file_save)
Client.file_set_length_units = make_api_method(file_set_length_units)
Client.file_set_mass_units = make_api_method(file_set_mass_units)

# interface.py
from creopyson.interface import export_3dpdf as interface_export_3dpdf
from creopyson.interface import export_file as interface_export_file
from creopyson.interface import export_image as interface_export_image
from creopyson.interface import export_pdf as interface_export_pdf
from creopyson.interface import export_program as interface_export_program
from creopyson.interface import import_program as interface_import_program
from creopyson.interface import mapkey as interface_mapkey
from creopyson.interface import plot as interface_plot
Client.interface_export_3dpdf = make_api_method(interface_export_3dpdf)
Client.interface_export_file = make_api_method(interface_export_file)
Client.interface_export_image = make_api_method(interface_export_image)
Client.interface_export_pdf = make_api_method(interface_export_pdf)
Client.interface_export_program = make_api_method(interface_export_program)
Client.interface_import_program = make_api_method(interface_import_program)
Client.interface_mapkey = make_api_method(interface_mapkey)
Client.interface_plot = make_api_method(interface_plot)

# Windchill
from creopyson.windchill import authorize as windchill_authorize
from creopyson.windchill import clear_workspace as windchill_clear_workspace
from creopyson.windchill import create_workspace as windchill_create_workspace
from creopyson.windchill import delete_workspace as windchill_delete_workspace
from creopyson.windchill import file_checked_out as windchill_file_checked_out
from creopyson.windchill import get_workspace as windchill_get_workspace
from creopyson.windchill import list_workspace_files as \
    windchill_list_workspace_files
from creopyson.windchill import list_workspaces as windchill_list_workspaces
from creopyson.windchill import server_exists as windchill_server_exists
from creopyson.windchill import set_server as windchill_set_server
from creopyson.windchill import set_workspace as windchill_set_workspace
from creopyson.windchill import workspace_exists as windchill_workspace_exists
Client.windchill_authorize = make_api_method(windchill_authorize)
Client.windchill_clear_workspace = make_api_method(windchill_clear_workspace)
Client.windchill_create_workspace = make_api_method(windchill_create_workspace)
Client.windchill_delete_workspace = make_api_method(windchill_delete_workspace)
Client.windchill_file_checked_out = make_api_method(windchill_file_checked_out)
Client.windchill_get_workspace = make_api_method(windchill_get_workspace)
Client.windchill_list_workspace_files = \
    make_api_method(windchill_list_workspace_files)
Client.windchill_list_workspaces = make_api_method(windchill_list_workspaces)
Client.windchill_server_exists = make_api_method(windchill_server_exists)
Client.windchill_set_server = make_api_method(windchill_set_server)
Client.windchill_set_workspace = make_api_method(windchill_set_workspace)
Client.windchill_workspace_exists = make_api_method(windchill_workspace_exists)
