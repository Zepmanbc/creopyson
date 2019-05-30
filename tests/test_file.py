"""Feature testing."""
import creopyson
import pytest
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_creoson_post_list


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
        transform={"fake transform":122},
        constraints={"fake constraint":122},
        package_assembly=True,
        walk_children=True,
        assemble_to_root=True,
        suppress=True
    )
    assert isinstance(result, (dict))


def test_file_backup(mk_creoson_post_None):
    """Test backup."""
    c = creopyson.Client()
    result = c.file_backup(
        "target",
        file_="file"
    )
    assert result is None


def test_file_close_window(mk_creoson_post_None):
    """Test close_window."""
    c = creopyson.Client()
    result = c.file_close_window(file_="file")
    assert result is None


def test_file_display(mk_creoson_post_None):
    """Test display."""
    c = creopyson.Client()
    result = c.file_display("file", activate=True)
    assert result is None


def test_file_erase(mk_creoson_post_None):
    """Test erase."""
    c = creopyson.Client()
    result = c.file_erase(
        file_="file",
        erase_children=True
    )
    assert result is None
    result = c.file_erase(
        file_=["file", "other file"]
    )
    assert result is None


def test_file_erase_not_displayed(mk_creoson_post_None):
    """Test erase_not_displayed."""
    c = creopyson.Client()
    result = c.file_erase_not_displayed()
    assert result is None


def test_file_exists(mk_creoson_post_dict):
    """Test exists."""
    c = creopyson.Client()
    result = c.file_exists(file_="file")
    assert result is True


def test_file_get_active(mk_creoson_post_dict):
    """Test get_active."""
    c = creopyson.Client()
    result = c.file_get_active()
    assert isinstance(result, (dict))


def test_file_get_fileinfo(mk_creoson_post_dict):
    """Test get_fileinfo."""
    c = creopyson.Client()
    result = c.file_get_fileinfo(file_="file")
    assert isinstance(result, (dict))


def test_file_get_length_units(mk_creoson_post_dict):
    """Test get_length_units."""
    c = creopyson.Client()
    result = c.file_get_length_units(file_="file")
    assert isinstance(result, (str))


def test_file_get_mass_units(mk_creoson_post_dict):
    """Test get_mass_units."""
    c = creopyson.Client()
    result = c.file_get_mass_units(file_="file")
    assert isinstance(result, (str))


def test_file_get_transform(mk_creoson_post_dict):
    """Test get_transform."""
    c = creopyson.Client()
    result = c.file_get_transform(
        asm="asm",
        path="path",
        csys="csys"
    )
    assert isinstance(result, (dict))


def test_file_has_instances(mk_creoson_post_dict):
    """Test has_instances."""
    c = creopyson.Client()
    result = c.file_has_instances(file_="file")
    assert result is True


def test_file_is_active(mk_creoson_post_dict):
    """Test is_active."""
    c = creopyson.Client()
    result = c.file_is_active(file_="file")
    assert result is True


def test_file_list(mk_creoson_post_dict):
    """Test list."""
    c = creopyson.Client()
    result = c.file_list(file_="file")
    assert isinstance(result, (list))
    result = c.file_list(file_=["file", "other file"])
    assert isinstance(result, (list))


def test_file_list_instances(mk_creoson_post_dict):
    """Test list_instances."""
    c = creopyson.Client()
    result = c.file_list_instances(file_="file")
    assert isinstance(result, (dict))


def test_file_list_simp_reps(mk_creoson_post_dict):
    """Test list_simp_reps."""
    c = creopyson.Client()
    result = c.file_list_simp_reps(
        file_="file",
        rep="rep"
    )
    assert isinstance(result, (dict))


def test_file_massprops(mk_creoson_post_dict):
    """Test massprops."""
    c = creopyson.Client()
    result = c.file_massprops(file_="file")
    assert isinstance(result, (dict))


def test_file_open(mk_creoson_post_dict):
    """Test open."""
    c = creopyson.Client()
    result = c.file_open(
        file_="file",
        dirname="dirname",
        generic="generic",
        display=True,
        activate=True,
        new_window=True,
        regen_force=True
    )
    assert isinstance(result, (dict))
    result = c.file_open(
        file_=["file", "other file"],
    )
    assert isinstance(result, (dict))


def test_file_open_errors(mk_creoson_post_dict):
    """Test open_errors."""
    c = creopyson.Client()
    result = c.file_open_errors(file_="file")
    assert result is True


def test_file_postregen_relations_get(mk_creoson_post_dict):
    """Test postregen_relations_get."""
    c = creopyson.Client()
    result = c.file_postregen_relations_get(file_="file")
    assert isinstance(result, (list))


def test_file_postregen_relations_set(mk_creoson_post_None):
    """Test postregen_relations_set."""
    c = creopyson.Client()
    result = c.file_postregen_relations_set(
        file_="file",
        relations=["relation"]
    )
    assert result is None


def test_file_refresh(mk_creoson_post_None):
    """Test refresh."""
    c = creopyson.Client()
    result = c.file_refresh(file_="file")
    assert result is None


def test_file_regenerate(mk_creoson_post_None):
    """Test regenerate."""
    c = creopyson.Client()
    result = c.file_regenerate(
        file_="file",
        display=True
    )
    assert result is None
    result = c.file_regenerate(
        file_=["file", "other file"]
    )
    assert result is None


def test_file_relations_get(mk_creoson_post_dict):
    """Test relations_get."""
    c = creopyson.Client()
    result = c.file_relations_get(file_="file")
    assert isinstance(result, (list))


def test_file_relations_set(mk_creoson_post_None):
    """Test relations_set."""
    c = creopyson.Client()
    result = c.file_relations_set(
        file_="file",
        relations=["relation"]
    )
    assert result is None


def test_file_rename(mk_creoson_post_dict):
    """Test rename."""
    c = creopyson.Client()
    result = c.file_rename(
        "new_name",
        file_="file",
        onlysession=True
    )
    assert isinstance(result, (str))


def test_file_repaint(mk_creoson_post_None):
    """Test repaint."""
    c = creopyson.Client()
    result = c.file_repaint(file_="file")
    assert result is None


def test_file_save(mk_creoson_post_None):
    """Test save."""
    c = creopyson.Client()
    result = c.file_save("file")
    assert result is None
    result = c.file_save(["file", "other file"])
    assert result is None


def test_file_set_length_units(mk_creoson_post_None):
    """Test set_length_units."""
    c = creopyson.Client()
    result = c.file_set_length_units(
        "mm",
        file_="file",
        convert=True
    )
    assert result is None


def test_file_set_mass_units(mk_creoson_post_None):
    """Test set_mass_units."""
    c = creopyson.Client()
    result = c.file_set_mass_units(
        "g",
        file_="file",
        convert=True
    )
    assert result is None
