"""Creo testing."""
from .fixtures import mk_creoson_post_dict
import creopyson


def test_bom_get_paths_ok(mk_creoson_post_dict):
    """Test bom_get_paths ok."""
    c = creopyson.Client()
    result = c.bom_get_paths(
        file_="",
        paths=True,
        skeletons=True,
        top_level=True,
        get_transforms=True,
        exclude_inactive=True
    )
    assert isinstance(result, (dict))
