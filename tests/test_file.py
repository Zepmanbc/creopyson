"""Feature testing."""
import creopyson
import pytest
from .fixtures import (
    mk_creoson_post_dict,
    mk_creoson_post_None,
    mk_creoson_post_list,
    mk_getactivefile,
)


def test_file_assemble(mk_creoson_post_dict):
    """Test assemble."""
    c = creopyson.Client()
    result = c.file_assemble(
        "file",
        dirname="dirname",
        generic="generic",
        into_asm="target",
        path="path",
        ref_model="model",
        transform={"fake transform": 122},
        constraints={"fake constraint": 122},
        package_assembly=True,
        walk_children=True,
        assemble_to_root=True,
        suppress=True,
    )
    assert isinstance(result, (dict))


def test_file_backup(mk_creoson_post_None, mk_getactivefile):
    """Test backup."""
    c = creopyson.Client()
    result = c.file_backup("target", file_="file")
    assert result is None
    result = c.file_backup("target")
    assert result is None


def test_file_close_window(mk_creoson_post_None, mk_getactivefile):
    """Test close_window."""
    c = creopyson.Client()
    result = c.file_close_window(file_="file")
    assert result is None
    result = c.file_close_window()
    assert result is None


def test_file_display(mk_creoson_post_None):
    """Test display."""
    c = creopyson.Client()
    result = c.file_display("file", activate=True)
    assert result is None


def test_file_delete_material(mk_creoson_post_None, mk_getactivefile):
    """Test delete_material."""
    c = creopyson.Client()
    result = c.file_delete_material("brass", file_="file")
    assert result is None
    result = c.file_delete_material("brass")
    assert result is None


def test_file_erase(mk_creoson_post_None, mk_getactivefile):
    """Test erase."""
    c = creopyson.Client()
    result = c.file_erase(file_="file", erase_children=True)
    assert result is None
    result = c.file_erase(file_=["file", "other file"])
    assert result is None
    result = c.file_erase()
    assert result is None


def test_file_erase_not_displayed(mk_creoson_post_None):
    """Test erase_not_displayed."""
    c = creopyson.Client()
    result = c.file_erase_not_displayed()
    assert result is None


def test_file_exists(mk_creoson_post_dict):
    """Test exists."""
    c = creopyson.Client()
    result = c.file_exists("file")
    assert result is True


def test_file_get_accuracy(mk_creoson_post_dict, mk_getactivefile):
    """Test get_accuracy."""
    c = creopyson.Client()
    result = c.file_get_accuracy()
    assert isinstance(result, (dict))
    result = c.file_get_accuracy(file_="file")
    assert isinstance(result, (dict))


def test_file_get_active(mk_creoson_post_dict):
    """Test get_active."""
    c = creopyson.Client()
    result = c.file_get_active()
    assert isinstance(result, (dict))


def test_file_get_cur_material(mk_creoson_post_dict, mk_getactivefile):
    """Test get_cur_material."""
    c = creopyson.Client()
    result = c.file_get_cur_material(file_="file")
    assert isinstance(result, (str))
    result = c.file_get_cur_material()
    assert isinstance(result, (str))


def test_file_get_cur_material_wildcard(mk_creoson_post_dict, mk_getactivefile):
    """Test get_cur_material_wildcard."""
    c = creopyson.Client()
    result = c.file_get_cur_material_wildcard(
        file_="file", include_non_matching_parts=True
    )
    assert isinstance(result, (list))
    result = c.file_get_cur_material_wildcard()
    assert isinstance(result, (list))


def test_file_get_fileinfo(mk_creoson_post_dict, mk_getactivefile):
    """Test get_fileinfo."""
    c = creopyson.Client()
    result = c.file_get_fileinfo(file_="file")
    assert isinstance(result, (dict))
    result = c.file_get_fileinfo()
    assert isinstance(result, (dict))


def test_file_get_length_units(mk_creoson_post_dict, mk_getactivefile):
    """Test get_length_units."""
    c = creopyson.Client()
    result = c.file_get_length_units(file_="file")
    assert isinstance(result, (str))
    result = c.file_get_length_units()
    assert isinstance(result, (str))


def test_file_get_mass_units(mk_creoson_post_dict, mk_getactivefile):
    """Test get_mass_units."""
    c = creopyson.Client()
    result = c.file_get_mass_units(file_="file")
    assert isinstance(result, (str))
    result = c.file_get_mass_units()
    assert isinstance(result, (str))


def test_file_get_transform(mk_creoson_post_dict):
    """Test get_transform."""
    c = creopyson.Client()
    result = c.file_get_transform(asm="asm", path="path", csys="csys")
    assert isinstance(result, (dict))


def test_file_has_instances(mk_creoson_post_dict, mk_getactivefile):
    """Test has_instances."""
    c = creopyson.Client()
    result = c.file_has_instances(file_="file")
    assert result is True
    result = c.file_has_instances()
    assert result is True


def test_file_is_active(mk_creoson_post_dict, mk_getactivefile):
    """Test is_active."""
    c = creopyson.Client()
    result = c.file_is_active("file")
    assert result is True


def test_file_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.file_list(file_="file")
    assert isinstance(result, (list))
    result = c.file_list(file_=["file", "other file"])
    assert isinstance(result, (list))
    result = c.file_list()
    assert isinstance(result, (list))


def test_file_list_instances(mk_creoson_post_dict, mk_getactivefile):
    """Test list_instances."""
    c = creopyson.Client()
    result = c.file_list_instances(file_="file")
    assert isinstance(result, (dict))
    result = c.file_list_instances()
    assert isinstance(result, (dict))


def test_file_list_materials(mk_creoson_post_dict, mk_getactivefile):
    """Test list_materials."""
    c = creopyson.Client()
    result = c.file_list_materials(file_="file", material="wood*")
    assert isinstance(result, (list))
    result = c.file_list_materials()
    assert isinstance(result, (list))


def test_file_list_materials_wildcard(mk_creoson_post_dict, mk_getactivefile):
    """Test list_materials."""
    c = creopyson.Client()
    result = c.file_list_materials_wildcard(
        file_="file", material="wood*", include_non_matching_parts=True
    )
    assert isinstance(result, (list))
    result = c.file_list_materials_wildcard()
    assert isinstance(result, (list))


def test_file_list_simp_reps(mk_creoson_post_dict, mk_getactivefile):
    """Test list_simp_reps."""
    c = creopyson.Client()
    result = c.file_list_simp_reps(file_="file", rep="rep")
    assert isinstance(result, (dict))
    result = c.file_list_simp_reps()
    assert isinstance(result, (dict))


def test_load_material_file(mk_creoson_post_dict, mk_getactivefile):
    """Test load_material_file"""
    c = creopyson.Client()
    result = c.file_load_material_file("material", file_="file", dirname="dirname")
    assert isinstance(result, (list))
    result = c.file_load_material_file("material")
    assert isinstance(result, (list))


def test_file_massprops(mk_creoson_post_dict, mk_getactivefile):
    """Test massprops."""
    c = creopyson.Client()
    result = c.file_massprops(file_="file")
    assert isinstance(result, (dict))
    result = c.file_massprops()
    assert isinstance(result, (dict))


def test_file_open(mk_creoson_post_dict, mk_getactivefile):
    """Test open."""
    c = creopyson.Client()
    result = c.file_open(
        "file",
        dirname="dirname",
        generic="generic",
        display=True,
        activate=True,
        new_window=True,
        regen_force=True,
    )
    assert isinstance(result, (dict))
    result = c.file_open(["file", "other file"],)
    assert isinstance(result, (dict))


def test_file_open_errors(mk_creoson_post_dict, mk_getactivefile):
    """Test open_errors."""
    c = creopyson.Client()
    result = c.file_open_errors(file_="file")
    assert result is True
    result = c.file_open_errors()
    assert result is True


def test_file_postregen_relations_get(mk_creoson_post_dict, mk_getactivefile):
    """Test postregen_relations_get."""
    c = creopyson.Client()
    result = c.file_postregen_relations_get(file_="file")
    assert isinstance(result, (list))
    result = c.file_postregen_relations_get()
    assert isinstance(result, (list))


def test_file_postregen_relations_set(mk_creoson_post_None, mk_getactivefile):
    """Test postregen_relations_set."""
    c = creopyson.Client()
    result = c.file_postregen_relations_set(file_="file", relations=["relation"])
    assert result is None
    result = c.file_postregen_relations_set()
    assert result is None


def test_file_refresh(mk_creoson_post_None, mk_getactivefile):
    """Test refresh."""
    c = creopyson.Client()
    result = c.file_refresh(file_="file")
    assert result is None
    result = c.file_refresh()
    assert result is None


def test_file_regenerate(mk_creoson_post_None, mk_getactivefile):
    """Test regenerate."""
    c = creopyson.Client()
    result = c.file_regenerate(file_="file", display=True)
    assert result is None
    result = c.file_regenerate(file_=["file", "other file"])
    assert result is None
    result = c.file_regenerate()
    assert result is None


def test_file_relations_get(mk_creoson_post_dict, mk_getactivefile):
    """Test relations_get."""
    c = creopyson.Client()
    result = c.file_relations_get(file_="file")
    assert isinstance(result, (list))
    result = c.file_relations_get()
    assert isinstance(result, (list))


def test_file_relations_set(mk_creoson_post_None, mk_getactivefile):
    """Test relations_set."""
    c = creopyson.Client()
    result = c.file_relations_set(file_="file", relations=["relation"])
    assert result is None
    result = c.file_relations_set()
    assert result is None


def test_file_rename(mk_creoson_post_dict, mk_getactivefile):
    """Test rename."""
    c = creopyson.Client()
    result = c.file_rename("new_name", file_="file", onlysession=True)
    assert isinstance(result, (str))
    result = c.file_rename("new_name")
    assert isinstance(result, (str))


def test_file_repaint(mk_creoson_post_None, mk_getactivefile):
    """Test repaint."""
    c = creopyson.Client()
    result = c.file_repaint(file_="file")
    assert result is None
    result = c.file_repaint()
    assert result is None


def test_file_save(mk_creoson_post_None, mk_getactivefile):
    """Test save."""
    c = creopyson.Client()
    result = c.file_save(file_="file")
    assert result is None
    result = c.file_save(file_=["file", "other file"])
    assert result is None
    result = c.file_save()
    assert result is None


def test_set_cur_material(mk_creoson_post_dict, mk_getactivefile):
    """Test set_cur_material."""
    c = creopyson.Client()
    result = c.file_set_cur_material("wood", file_="*.prt")
    assert isinstance(result, (list))
    result = c.file_set_cur_material("wood")
    assert isinstance(result, (list))


def test_file_set_length_units(mk_creoson_post_None, mk_getactivefile):
    """Test set_length_units."""
    c = creopyson.Client()
    result = c.file_set_length_units("mm", file_="file", convert=True)
    assert result is None
    result = c.file_set_length_units("mm")
    assert result is None
    result = c.file_set_length_units("mm", file_=["file1", "file2"])
    assert result is None
    result = c.file_set_length_units("mm")
    assert result is None


def test_file_set_mass_units(mk_creoson_post_None, mk_getactivefile):
    """Test set_mass_units."""
    c = creopyson.Client()
    result = c.file_set_mass_units("g", file_="file", convert=True)
    assert result is None
    result = c.file_set_mass_units("g", file_=["file1", "file2"])
    assert result is None
    result = c.file_set_mass_units("g")
    assert result is None
