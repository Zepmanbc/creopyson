# -*- coding: utf-8 -*-

"""Top-level package for Creopyson."""

__author__ = """Benjamin C."""
__email__ = 'zepman@gmail.com'
__version__ = '0.5.0'

from creopyson.connection import Client
from creopyson.objects import jlpoint


"""Add API methods to CLient."""

# Bom
from creopyson.bom import get_paths as bom_get_paths
Client.bom_get_paths = bom_get_paths


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
Client.creo_cd = creo_cd
Client.creo_delete_files = creo_delete_files
Client.creo_get_config = creo_get_config
Client.creo_get_std_color = creo_get_std_color
Client.creo_list_dirs = creo_list_dirs
Client.creo_list_files = creo_list_files
Client.creo_mkdir = creo_mkdir
Client.creo_pwd = creo_pwd
Client.creo_rmdir = creo_rmdir
Client.creo_set_config = creo_set_config
Client.creo_set_std_color = creo_set_std_color


# Dimension
from creopyson.dimension import copy as dimension_copy
from creopyson.dimension import list_detail as dimension_list_detail
from creopyson.dimension import list_ as dimension_list
from creopyson.dimension import set_ as dimension_set
from creopyson.dimension import set_text as dimension_set_text
from creopyson.dimension import show as dimension_show
from creopyson.dimension import user_select as dimension_user_select
Client.dimension_copy = dimension_copy
Client.dimension_list_detail = dimension_list_detail
Client.dimension_list = dimension_list
Client.dimension_set = dimension_set
Client.dimension_set_text = dimension_set_text
Client.dimension_show = dimension_show
Client.dimension_user_select = dimension_user_select


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
from creopyson.drawing import get_sheet_format as drawing_get_sheet_format
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
from creopyson.drawing import set_sheet_format as drawing_set_sheet_format
from creopyson.drawing import set_view_loc as drawing_set_view_loc
from creopyson.drawing import view_bound_box as drawing_view_bound_box
Client.drawing_add_model = drawing_add_model
Client.drawing_add_sheet = drawing_add_sheet
Client.drawing_create_gen_view = drawing_create_gen_view
Client.drawing_create = drawing_create
Client.drawing_create_proj_view = drawing_create_proj_view
Client.drawing_create_symbol = drawing_create_symbol
Client.drawing_delete_models = drawing_delete_models
Client.drawing_delete_sheet = drawing_delete_sheet
Client.drawing_delete_symbol_def = drawing_delete_symbol_def
Client.drawing_delete_symbol_inst = drawing_delete_symbol_inst
Client.drawing_delete_view = drawing_delete_view
Client.drawing_get_cur_model = drawing_get_cur_model
Client.drawing_get_cur_sheet = drawing_get_cur_sheet
Client.drawing_get_num_sheets = drawing_get_num_sheets
Client.drawing_get_sheet_format = drawing_get_sheet_format
Client.drawing_get_sheet_scale = drawing_get_sheet_scale
Client.drawing_get_sheet_size = drawing_get_sheet_size
Client.drawing_get_view_loc = drawing_get_view_loc
Client.drawing_get_view_scale = drawing_get_view_scale
Client.drawing_get_view_sheet = drawing_get_view_sheet
Client.drawing_is_symbol_def_loaded = drawing_is_symbol_def_loaded
Client.drawing_list_models = drawing_list_models
Client.drawing_list_symbols = drawing_list_symbols
Client.drawing_list_view_details = drawing_list_view_details
Client.drawing_list_views = drawing_list_views
Client.drawing_load_symbol_def = drawing_load_symbol_def
Client.drawing_regenerate = drawing_regenerate
Client.drawing_regenerate_sheet = drawing_regenerate_sheet
Client.drawing_rename_view = drawing_rename_view
Client.drawing_scale_sheet = drawing_scale_sheet
Client.drawing_scale_view = drawing_scale_view
Client.drawing_select_sheet = drawing_select_sheet
Client.drawing_set_cur_model = drawing_set_cur_model
Client.drawing_set_sheet_format = drawing_set_sheet_format
Client.drawing_set_view_loc = drawing_set_view_loc
Client.drawing_view_bound_box = drawing_view_bound_box


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
Client.familytable_add_inst = familytable_add_inst
Client.familytable_create_inst = familytable_create_inst
Client.familytable_delete_inst = familytable_delete_inst
Client.familytable_delete = familytable_delete
Client.familytable_exists = familytable_exists
Client.familytable_get_cell = familytable_get_cell
Client.familytable_get_header = familytable_get_header
Client.familytable_get_parents = familytable_get_parents
Client.familytable_get_row = familytable_get_row
Client.familytable_list = familytable_list
Client.familytable_list_tree = familytable_list_tree
Client.familytable_replace = familytable_replace
Client.familytable_set_cell = familytable_set_cell


# Feature
from creopyson.feature import delete as feature_delete
from creopyson.feature import delete_param as feature_delete_param
from creopyson.feature import list_ as feature_list
from creopyson.feature import list_params as feature_list_params
from creopyson.feature import list_group_features as \
    feature_list_group_features
from creopyson.feature import list_pattern_features as \
    feature_list_pattern_features
from creopyson.feature import param_exists as feature_param_exists
from creopyson.feature import rename as feature_rename
from creopyson.feature import resume as feature_resume
from creopyson.feature import set_param as feature_set_param
from creopyson.feature import suppress as feature_suppress
from creopyson.feature import user_select_csys as feature_user_select_csys
Client.feature_delete = feature_delete
Client.feature_delete_param = feature_delete_param
Client.feature_list = feature_list
Client.feature_list_params = feature_list_params
Client.feature_list_group_features = feature_list_group_features
Client.feature_list_pattern_features = feature_list_pattern_features
Client.feature_param_exists = feature_param_exists
Client.feature_rename = feature_rename
Client.feature_resume = feature_resume
Client.feature_set_param = feature_set_param
Client.feature_suppress = feature_suppress
Client.feature_user_select_csys = feature_user_select_csys


# File
from creopyson.file import assemble as file_assemble
from creopyson.file import backup as file_backup
from creopyson.file import close_window as file_close_window
from creopyson.file import display as file_display
from creopyson.file import delete_material as file_delete_material
from creopyson.file import erase as file_erase
from creopyson.file import erase_not_displayed as file_erase_not_displayed
from creopyson.file import exists as file_exists
from creopyson.file import get_active as file_get_active
from creopyson.file import get_cur_material as file_get_cur_material
from creopyson.file import get_cur_material_wildcard as file_get_cur_material_wildcard
from creopyson.file import get_fileinfo as file_get_fileinfo
from creopyson.file import get_length_units as file_get_length_units
from creopyson.file import get_mass_units as file_get_mass_units
from creopyson.file import get_transform as file_get_transform
from creopyson.file import has_instances as file_has_instances
from creopyson.file import is_active as file_is_active
from creopyson.file import list_instances as file_list_instances
from creopyson.file import list_materials as file_list_materials
from creopyson.file import list_materials_wildcard as file_list_materials_wildcard
from creopyson.file import list_ as file_list
from creopyson.file import list_simp_reps as file_list_simp_reps
from creopyson.file import load_material_file as file_load_material_file
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
from creopyson.file import set_cur_material as file_set_cur_material
from creopyson.file import set_length_units as file_set_length_units
from creopyson.file import set_mass_units as file_set_mass_units
Client.file_assemble = file_assemble
Client.file_backup = file_backup
Client.file_close_window = file_close_window
Client.file_display = file_display
Client.file_delete_material = file_delete_material
Client.file_erase = file_erase
Client.file_erase_not_displayed = file_erase_not_displayed
Client.file_exists = file_exists
Client.file_get_active = file_get_active
Client.file_get_cur_material = file_get_cur_material
Client.file_get_cur_material_wildcard = file_get_cur_material_wildcard
Client.file_get_fileinfo = file_get_fileinfo
Client.file_get_length_units = file_get_length_units
Client.file_get_mass_units = file_get_mass_units
Client.file_get_transform = file_get_transform
Client.file_has_instances = file_has_instances
Client.file_is_active = file_is_active
Client.file_list_instances = file_list_instances
Client.file_list_materials = file_list_materials
Client.file_list_materials_wildcard = file_list_materials_wildcard
Client.file_list = file_list
Client.file_list_simp_reps = file_list_simp_reps
Client.file_load_material_file = file_load_material_file
Client.file_massprops = file_massprops
Client.file_open_errors = file_open_errors
Client.file_open = file_open
Client.file_postregen_relations_get = file_postregen_relations_get
Client.file_postregen_relations_set = file_postregen_relations_set
Client.file_refresh = file_refresh
Client.file_regenerate = file_regenerate
Client.file_relations_get = file_relations_get
Client.file_relations_set = file_relations_set
Client.file_rename = file_rename
Client.file_repaint = file_repaint
Client.file_save = file_save
Client.file_set_cur_material = file_set_cur_material
Client.file_set_length_units = file_set_length_units
Client.file_set_mass_units = file_set_mass_units


# Geometry
from creopyson.geometry import bound_box as geometry_bound_box
from creopyson.geometry import get_edges as geometry_get_edges
from creopyson.geometry import get_surfaces as geometry_get_surfaces
Client.geometry_bound_box = geometry_bound_box
Client.geometry_get_edges = geometry_get_edges
Client.geometry_get_surfaces = geometry_get_surfaces


# Interface
from creopyson.interface import export_3dpdf as interface_export_3dpdf
from creopyson.interface import export_file as interface_export_file
from creopyson.interface import export_image as interface_export_image
from creopyson.interface import export_pdf as interface_export_pdf
from creopyson.interface import export_program as interface_export_program
from creopyson.interface import import_file as interface_import_file
from creopyson.interface import import_program as interface_import_program
from creopyson.interface import mapkey as interface_mapkey
from creopyson.interface import plot as interface_plot
Client.interface_export_3dpdf = interface_export_3dpdf
Client.interface_export_file = interface_export_file
Client.interface_export_image = interface_export_image
Client.interface_export_pdf = interface_export_pdf
Client.interface_export_program = interface_export_program
Client.interface_import_file = interface_import_file
Client.interface_import_program = interface_import_program
Client.interface_mapkey = interface_mapkey
Client.interface_plot = interface_plot


# Layer
from creopyson.layer import delete as layer_delete
from creopyson.layer import exists as layer_exists
from creopyson.layer import list_ as layer_list
from creopyson.layer import show as layer_show
Client.layer_delete = layer_delete
Client.layer_exists = layer_exists
Client.layer_list = layer_list
Client.layer_show = layer_show


# Note
from creopyson.note import copy as note_copy
from creopyson.note import delete as note_delete
from creopyson.note import exists as note_exists
from creopyson.note import get as note_get
from creopyson.note import list_ as note_list
from creopyson.note import set_ as note_set
Client.note_copy = note_copy
Client.note_delete = note_delete
Client.note_exists = note_exists
Client.note_get = note_get
Client.note_list = note_list
Client.note_set = note_set


# Parameter
from creopyson.parameter import copy as parameter_copy
from creopyson.parameter import delete as parameter_delete
from creopyson.parameter import exists as parameter_exists
from creopyson.parameter import list_ as parameter_list
from creopyson.parameter import set_ as parameter_set
from creopyson.parameter import set_designated as parameter_set_designated
Client.parameter_copy = parameter_copy
Client.parameter_delete = parameter_delete
Client.parameter_exists = parameter_exists
Client.parameter_list = parameter_list
Client.parameter_set = parameter_set
Client.parameter_set_designated = parameter_set_designated


# Server
from creopyson.server import pwd as server_pwd
Client.server_pwd = server_pwd


# View
from creopyson.view import activate as view_activate
from creopyson.view import list_exploded as view_list_exploded
from creopyson.view import list_ as view_list
from creopyson.view import save as view_save
Client.view_activate = view_activate
Client.view_list_exploded = view_list_exploded
Client.view_list = view_list
Client.view_save = view_save


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
Client.windchill_authorize = windchill_authorize
Client.windchill_clear_workspace = windchill_clear_workspace
Client.windchill_create_workspace = windchill_create_workspace
Client.windchill_delete_workspace = windchill_delete_workspace
Client.windchill_file_checked_out = windchill_file_checked_out
Client.windchill_get_workspace = windchill_get_workspace
Client.windchill_list_workspace_files = windchill_list_workspace_files
Client.windchill_list_workspaces = windchill_list_workspaces
Client.windchill_server_exists = windchill_server_exists
Client.windchill_set_server = windchill_set_server
Client.windchill_set_workspace = windchill_set_workspace
Client.windchill_workspace_exists = windchill_workspace_exists
