"""Feature testing."""
import creopyson
import pytest
from .fixtures import mk_creoson_post_dict, mk_creoson_post_None, mk_creoson_post_list, mk_getactivefile, mk_getactivefile


def test_feature_delete(mk_creoson_post_None, mk_getactivefile):
    """Test delete."""
    c = creopyson.Client()
    result = c.feature_delete(
        file_="file",
        name="name",
        status="ACTIVE",
        type_="type",
        clip=True
    )
    assert result is None
    result = c.feature_delete(
        name=["name1", "name2"]
    )
    assert result is None


def test_feature_delete_param(mk_creoson_post_None, mk_getactivefile):
    """Test delete_param."""
    c = creopyson.Client()
    result = c.feature_delete_param(
        file_="file",
        name="name",
        param="param"
    )
    assert result is None
    result = c.feature_delete_param()
    assert result is None


def test_feature_list(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.feature_list(
        file_="file",
        name="name",
        type_="type",
        no_datum=True,
        inc_unnamed=True,
        no_comp=True,
        param="param",
        value="param",
        encoded=True
    )
    assert isinstance(result, (list))
    result = c.feature_list(
        param=["param", "other param"],
    )
    assert isinstance(result, (list))


def test_feature_list_params(mk_creoson_post_dict, mk_getactivefile):
    """Test list."""
    c = creopyson.Client()
    result = c.feature_list_params(
        file_="file",
        name="name",
        type_="type",
        no_datum=True,
        no_comp=True,
        param="param",
        value="param",
        encoded=True,
    )
    assert isinstance(result, (list))
    result = c.feature_list_params(
        param=["param", "other param"],
        name=12,
    )
    assert isinstance(result, (list))


def test_feature_list_group_features(mk_creoson_post_dict, mk_getactivefile):
    """Test list_group_features."""
    c = creopyson.Client()
    result = c.feature_list_group_features(
        "group_name",
        file_="file",
        type_="type",
    )
    assert isinstance(result, (list))
    result = c.feature_list_group_features("group_name")
    assert isinstance(result, (list))


def test_feature_list_pattern_features(mk_creoson_post_dict, mk_getactivefile):
    """Test list_group_features."""
    c = creopyson.Client()
    result = c.feature_list_pattern_features(
        "pattern_name",
        file_="file",
        type_="type",
    )
    assert isinstance(result, (list))
    result = c.feature_list_pattern_features("pattern_name")
    assert isinstance(result, (list))


def test_feature_param_exists(mk_creoson_post_dict, mk_getactivefile):
    """Test param_exists."""
    c = creopyson.Client()
    result = c.feature_param_exists(
        file_="file",
        param="param"
    )
    assert result is True
    result = c.feature_param_exists(
        param=["param", "other param"]
    )
    assert result is True


def test_feature_rename(mk_creoson_post_None, mk_getactivefile):
    """Test rename."""
    c = creopyson.Client()
    result = c.feature_rename(
        "oldname", "new_name",
        file_="file"
    )
    assert result is None
    c = creopyson.Client()
    result = c.feature_rename("oldname", "new_name")
    assert result is None
    result = c.feature_rename(
        1, "new_name",
        file_="file"
    )
    with pytest.raises(TypeError):
        c.feature_rename(
            ["list"], "new_name",
            file_="file"
        )


def test_feature_resume(mk_creoson_post_None, mk_getactivefile):
    """Test resume."""
    c = creopyson.Client()
    result = c.feature_resume(
        file_="file",
        name="name",
        status="ACTIVE",
        type_="type",
        with_children=True
    )
    assert result is None
    result = c.feature_resume(
        name=["name", "other name"],
    )
    assert result is None


def test_feature_set_param(mk_creoson_post_None, mk_getactivefile):
    """Test set_param."""
    c = creopyson.Client()
    result = c.feature_set_param(
        "param",
        file_="file",
        name="name",
        type_="STRING",
        value=12,
        encoded=True,
        designate=True,
        no_create=True
    )
    assert result is None
    result = c.feature_set_param("param")
    assert result is None


def test_feature_suppress(mk_creoson_post_None, mk_getactivefile):
    """Test suppress."""
    c = creopyson.Client()
    result = c.feature_suppress(
        file_="file",
        name="name",
        status="ACTIVE",
        type_="type",
        clip=False,
        with_children=False
    )
    assert result is None
    result = c.feature_suppress(
        name=["name", "other name"],
    )
    assert result is None


def test_feature_user_select_csys(mk_creoson_post_list, mk_getactivefile):
    """Test user_select_csys."""
    c = creopyson.Client()
    result = c.feature_user_select_csys(
        file_="file",
        max_=12
    )
    assert isinstance(result, (list))
    result = c.feature_user_select_csys()
    assert isinstance(result, (list))
