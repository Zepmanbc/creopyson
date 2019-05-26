"""Connection module."""
import requests
import json
import functools
import sys

from creopyson.core import creoson_post


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
            sys.exit(e)

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

        Raises:
            Warning: error message from creoson.

        Returns:
            (boolean): True if Creo is running, False instead.

        """
        request = {
            "command": "connection",
            "function": "is_creo_running"
        }
        status, data = creoson_post(self, request)
        if not status:
            return data["running"]
        else:
            raise Warning(data)

    def kill_creo(self):
        """Kill primary Creo processes.

        This will kill the 'xtop.exe' and 'nmsd.exe' processes by name.
        The sessionId is optional, and ignored.

        Raises:
            Warning: error message from creoson.

        Returns:
            None

        """
        request = {
            "command": "connection",
            "function": "kill_creo"
        }
        status, data = creoson_post(self, request)
        if status:
            raise Warning(data)

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

        Raises:
            Warning: error message from creoson.

        Returns:
            None

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
            raise Warning(data)

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
        request = {
            "sessionId": self.sessionId,
            "command": "connection",
            "function": "stop_creo"
        }
        status, data = creoson_post(self, request)
        if status:
            raise Warning(data)


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

# Bom
from creopyson.bom import get_paths as bom_get_paths
Client.bom_get_paths = make_api_method(bom_get_paths)


# Creo
from creopyson.creo import cd as creo_cd
from creopyson.creo import delete_files as creo_delete_files
from creopyson.creo import get_config as creo_get_config
from creopyson.creo import get_std_color as creo_get_std_color
from creopyson.creo import list_dirs as creo_list_dirs
from creopyson.creo import list_files as creo_list_files
from creopyson.creo import mkdir as creo_mkdir
from creopyson.creo import pwd as creo_pwd
from creopyson.creo import rmdir as creo_rmdir
from creopyson.creo import set_config as creo_set_config
from creopyson.creo import set_std_color as creo_set_std_color
Client.creo_cd = make_api_method(creo_cd)
Client.creo_delete_files = make_api_method(creo_delete_files)
Client.creo_get_config = make_api_method(creo_get_config)
Client.creo_get_std_color = make_api_method(creo_get_std_color)
Client.creo_list_dirs = make_api_method(creo_list_dirs)
Client.creo_list_files = make_api_method(creo_list_files)
Client.creo_mkdir = make_api_method(creo_mkdir)
Client.creo_pwd = make_api_method(creo_pwd)
Client.creo_rmdir = make_api_method(creo_rmdir)
Client.creo_set_config = make_api_method(creo_set_config)
Client.creo_set_std_color = make_api_method(creo_set_std_color)


# Dimension
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


# Drawing
from creopyson.drawing import add_model as drawing_add_model
from creopyson.drawing import add_sheet as drawing_add_sheet
from creopyson.drawing import create_gen_view as drawing_create_gen_view
from creopyson.drawing import create as drawing_create
from creopyson.drawing import create_proj_view as drawing_create_proj_view
from creopyson.drawing import create_symbol as drawing_create_symbol
from creopyson.drawing import delete_models as drawing_delete_models
from creopyson.drawing import delete_sheet as drawing_delete_sheet
from creopyson.drawing import delete_symbol_def as drawing_delete_symbol_def
from creopyson.drawing import delete_symbol_inst as drawing_delete_symbol_inst
from creopyson.drawing import delete_view as drawing_delete_view
from creopyson.drawing import get_cur_model as drawing_get_cur_model
from creopyson.drawing import get_cur_sheet as drawing_get_cur_sheet
from creopyson.drawing import get_num_sheets as drawing_get_num_sheets
from creopyson.drawing import get_sheet_scale as drawing_get_sheet_scale
from creopyson.drawing import get_sheet_size as drawing_get_sheet_size
from creopyson.drawing import get_view_loc as drawing_get_view_loc
from creopyson.drawing import get_view_scale as drawing_get_view_scale
from creopyson.drawing import get_view_sheet as drawing_get_view_sheet
from creopyson.drawing import is_symbol_def_loaded as \
    drawing_is_symbol_def_loaded
from creopyson.drawing import list_models as drawing_list_models
from creopyson.drawing import list_symbols as drawing_list_symbols
from creopyson.drawing import list_view_details as drawing_list_view_details
from creopyson.drawing import list_views as drawing_list_views
from creopyson.drawing import load_symbol_def as drawing_load_symbol_def
from creopyson.drawing import regenerate as drawing_regenerate
from creopyson.drawing import regenerate_sheet as drawing_regenerate_sheet
from creopyson.drawing import rename_view as drawing_rename_view
from creopyson.drawing import scale_sheet as drawing_scale_sheet
from creopyson.drawing import scale_view as drawing_scale_view
from creopyson.drawing import select_sheet as drawing_select_sheet
from creopyson.drawing import set_cur_model as drawing_set_cur_model
from creopyson.drawing import set_view_loc as drawing_set_view_loc
from creopyson.drawing import view_bound_box as drawing_view_bound_box
Client.drawing_add_model = make_api_method(drawing_add_model)
Client.drawing_add_sheet = make_api_method(drawing_add_sheet)
Client.drawing_create_gen_view = make_api_method(drawing_create_gen_view)
Client.drawing_create = make_api_method(drawing_create)
Client.drawing_create_proj_view = make_api_method(drawing_create_proj_view)
Client.drawing_create_symbol = make_api_method(drawing_create_symbol)
Client.drawing_delete_models = make_api_method(drawing_delete_models)
Client.drawing_delete_sheet = make_api_method(drawing_delete_sheet)
Client.drawing_delete_symbol_def = make_api_method(drawing_delete_symbol_def)
Client.drawing_delete_symbol_inst = make_api_method(drawing_delete_symbol_inst)
Client.drawing_delete_view = make_api_method(drawing_delete_view)
Client.drawing_get_cur_model = make_api_method(drawing_get_cur_model)
Client.drawing_get_cur_sheet = make_api_method(drawing_get_cur_sheet)
Client.drawing_get_num_sheets = make_api_method(drawing_get_num_sheets)
Client.drawing_get_sheet_scale = make_api_method(drawing_get_sheet_scale)
Client.drawing_get_sheet_size = make_api_method(drawing_get_sheet_size)
Client.drawing_get_view_loc = make_api_method(drawing_get_view_loc)
Client.drawing_get_view_scale = make_api_method(drawing_get_view_scale)
Client.drawing_get_view_sheet = make_api_method(drawing_get_view_sheet)
Client.drawing_is_symbol_def_loaded = \
    make_api_method(drawing_is_symbol_def_loaded)
Client.drawing_list_models = make_api_method(drawing_list_models)
Client.drawing_list_symbols = make_api_method(drawing_list_symbols)
Client.drawing_list_view_details = make_api_method(drawing_list_view_details)
Client.drawing_list_views = make_api_method(drawing_list_views)
Client.drawing_load_symbol_def = make_api_method(drawing_load_symbol_def)
Client.drawing_regenerate = make_api_method(drawing_regenerate)
Client.drawing_regenerate_sheet = make_api_method(drawing_regenerate_sheet)
Client.drawing_rename_view = make_api_method(drawing_rename_view)
Client.drawing_scale_sheet = make_api_method(drawing_scale_sheet)
Client.drawing_scale_view = make_api_method(drawing_scale_view)
Client.drawing_select_sheet = make_api_method(drawing_select_sheet)
Client.drawing_set_cur_model = make_api_method(drawing_set_cur_model)
Client.drawing_set_view_loc = make_api_method(drawing_set_view_loc)
Client.drawing_view_bound_box = make_api_method(drawing_view_bound_box)


# Familytable
from creopyson.familytable import add_inst as familytable_add_inst
from creopyson.familytable import create_inst as familytable_create_inst
from creopyson.familytable import delete_inst as familytable_delete_inst
from creopyson.familytable import delete as familytable_delete
from creopyson.familytable import exists as familytable_exists
from creopyson.familytable import get_cell as familytable_get_cell
from creopyson.familytable import get_header as familytable_get_header
from creopyson.familytable import get_parents as familytable_get_parents
from creopyson.familytable import get_row as familytable_get_row
from creopyson.familytable import list_ as familytable_list
from creopyson.familytable import list_tree as familytable_list_tree
from creopyson.familytable import replace as familytable_replace
from creopyson.familytable import set_cell as familytable_set_cell
Client.familytable_add_inst = make_api_method(familytable_add_inst)
Client.familytable_create_inst = make_api_method(familytable_create_inst)
Client.familytable_delete_inst = make_api_method(familytable_delete_inst)
Client.familytable_delete = make_api_method(familytable_delete)
Client.familytable_exists = make_api_method(familytable_exists)
Client.familytable_get_cell = make_api_method(familytable_get_cell)
Client.familytable_get_header = make_api_method(familytable_get_header)
Client.familytable_get_parents = make_api_method(familytable_get_parents)
Client.familytable_get_row = make_api_method(familytable_get_row)
Client.familytable_list = make_api_method(familytable_list)
Client.familytable_list_tree = make_api_method(familytable_list_tree)
Client.familytable_replace = make_api_method(familytable_replace)
Client.familytable_set_cell = make_api_method(familytable_set_cell)


# Feature
from creopyson.feature import delete as feature_delete
from creopyson.feature import delete_param as feature_delete_param
from creopyson.feature import list_ as feature_list
from creopyson.feature import param_exists as feature_param_exists
from creopyson.feature import rename as feature_rename
from creopyson.feature import resume as feature_resume
from creopyson.feature import set_param as feature_set_param
from creopyson.feature import suppress as feature_suppress
from creopyson.feature import user_select_csys as feature_user_select_csys
Client.feature_delete = make_api_method(feature_delete)
Client.feature_delete_param = make_api_method(feature_delete_param)
Client.feature_list = make_api_method(feature_list)
Client.feature_param_exists = make_api_method(feature_param_exists)
Client.feature_rename = make_api_method(feature_rename)
Client.feature_resume = make_api_method(feature_resume)
Client.feature_set_param = make_api_method(feature_set_param)
Client.feature_suppress = make_api_method(feature_suppress)
Client.feature_user_select_csys = make_api_method(feature_user_select_csys)


# File
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


# Geometry
from creopyson.geometry import bound_box as geometry_bound_box
from creopyson.geometry import get_edges as geometry_get_edges
from creopyson.geometry import get_surfaces as geometry_get_surfaces
Client.geometry_bound_box = make_api_method(geometry_bound_box)
Client.geometry_get_edges = make_api_method(geometry_get_edges)
Client.geometry_get_surfaces = make_api_method(geometry_get_surfaces)


# Interface
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


# Layer
from creopyson.layer import delete as layer_delete
from creopyson.layer import exists as layer_exists
from creopyson.layer import list_ as layer_list
from creopyson.layer import show as layer_show
Client.layer_delete = make_api_method(layer_delete)
Client.layer_exists = make_api_method(layer_exists)
Client.layer_list = make_api_method(layer_list)
Client.layer_show = make_api_method(layer_show)


# Note
from creopyson.note import copy as note_copy
from creopyson.note import delete as note_delete
from creopyson.note import exists as note_exists
from creopyson.note import get as note_get
from creopyson.note import list_ as note_list
from creopyson.note import set_ as note_set
Client.note_copy = make_api_method(note_copy)
Client.note_delete = make_api_method(note_delete)
Client.note_exists = make_api_method(note_exists)
Client.note_get = make_api_method(note_get)
Client.note_list = make_api_method(note_list)
Client.note_set = make_api_method(note_set)


# Parameter
from creopyson.parameter import copy as parameter_copy
from creopyson.parameter import delete as parameter_delete
from creopyson.parameter import exists as parameter_exists
from creopyson.parameter import list_ as parameter_list
from creopyson.parameter import set_ as parameter_set
Client.parameter_copy = make_api_method(parameter_copy)
Client.parameter_delete = make_api_method(parameter_delete)
Client.parameter_exists = make_api_method(parameter_exists)
Client.parameter_list = make_api_method(parameter_list)
Client.parameter_set = make_api_method(parameter_set)


# Server
from creopyson.server import pwd as server_pwd
Client.server_pwd = make_api_method(server_pwd)


# View
from creopyson.view import activate as view_activate
from creopyson.view import list_exploded as view_list_exploded
from creopyson.view import list_ as view_list
from creopyson.view import save as view_save
Client.view_activate = make_api_method(view_activate)
Client.view_list_exploded = make_api_method(view_list_exploded)
Client.view_list = make_api_method(view_list)
Client.view_save = make_api_method(view_save)


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
