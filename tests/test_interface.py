"""Interface testing."""
import pytest
import creopyson
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_getactivefile


def test_interface_export_3dpdf(mk_creoson_post_dict, mk_getactivefile):
    """Test export_3dpdf."""
    c = creopyson.Client()
    result = c.interface_export_3dpdf(
        file_="file",
        filename="filename",
        dirname="dirname",
        height=12.3,
        width=12.3,
        dpi=200,
        use_drawing_settings=True,
        sheet_range="current",
    )
    assert isinstance(result, (dict))
    result = c.interface_export_3dpdf()
    assert isinstance(result, (dict))


def test_interface_export_file(mk_creoson_post_dict, mk_getactivefile):
    """Test export_file."""
    c = creopyson.Client()
    result = c.interface_export_file(
        "STEP",
        file_="file",
        filename="filename",
        dirname="dirname",
        geom_flags="default",
        advanced=True,
    )
    assert isinstance(result, (dict))
    result = c.interface_export_file("STEP")
    assert isinstance(result, (dict))


def test_interface_export_image(mk_creoson_post_dict, mk_getactivefile):
    """Test export_image."""
    c = creopyson.Client()
    result = c.interface_export_image(
        "JPEG",
        file_="file",
        filename="filename",
        height=9.2,
        width=12.3,
        dpi=200,
        depth=12,
    )
    assert isinstance(result, (dict))
    result = c.interface_export_image("JPEG")
    assert isinstance(result, (dict))


def test_interface_export_pdf(mk_creoson_post_dict, mk_getactivefile):
    """Test export_pdf."""
    c = creopyson.Client()
    result = c.interface_export_pdf(
        file_="file",
        filename="filename",
        dirname="dirname",
        height=12.3,
        width=12.3,
        dpi=200,
        use_drawing_settings=True,
        sheet_range="current",
    )
    assert isinstance(result, (dict))
    result = c.interface_export_pdf()
    assert isinstance(result, (dict))


def test_interface_export_program(mk_creoson_post_dict, mk_getactivefile):
    """Test export_program."""
    c = creopyson.Client()
    result = c.interface_export_program(file_="file")
    assert isinstance(result, (dict))
    result = c.interface_export_program()
    assert isinstance(result, (dict))


def test_import_file(mk_creoson_post_dict):
    """Test import_file."""
    c = creopyson.Client()
    result = c.interface_import_file(
        "filename.stp",
        "STEP",
        dirname="directory/of/filename/",
        new_name="my_imported_file",
        new_model_type="prt",
    )
    assert isinstance(result, (str))


def test_import_file_tryAllExtensions(mk_creoson_post_dict):
    """Test import_file."""
    c = creopyson.Client()
    result = c.interface_import_file("filename.stp")
    assert isinstance(result, (str))
    result = c.interface_import_file("filename.igs.1")
    assert isinstance(result, (str))
    result = c.interface_import_file("filename.neu.59")
    assert isinstance(result, (str))
    result = c.interface_import_file("filename.pvz")
    assert isinstance(result, (str))


def test_import_file_Needfile_type(mk_creoson_post_dict):
    """Test import_file."""
    c = creopyson.Client()
    with pytest.raises(TypeError):
        c.interface_import_file("filename.fake_ext.12")


def test_interface_import_program(mk_creoson_post_dict, mk_getactivefile):
    """Test import_program."""
    c = creopyson.Client()
    result = c.interface_import_program(
        file_="file", filename="filename", dirname="dirname"
    )
    assert isinstance(result, (str))
    result = c.interface_import_program()
    assert isinstance(result, (str))


def test_interface_mapkey(mk_creoson_post_None):
    """Test mapkey."""
    c = creopyson.Client()
    result = c.interface_mapkey("script", delay=12)
    assert result is None


def test_interface_plot(mk_creoson_post_dict, mk_getactivefile):
    """Test plot."""
    c = creopyson.Client()
    result = c.interface_plot(file_="file", dirname="dirname", driver="JPEG")
    assert isinstance(result, (dict))
    result = c.interface_plot()
    assert isinstance(result, (dict))
