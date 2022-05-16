"""Creo testing."""
from .fixtures import mk_creoson_post_dict, mk_getactivefile
import creopyson


def test_bom_get_paths_ok(mk_creoson_post_dict, mk_getactivefile):
    """Test bom_get_paths ok."""
    c = creopyson.Client()
    result = c.bom_get_paths(
        file_="fakefile",
        paths=True,
        skeletons=True,
        top_level=True,
        get_transforms=True,
        exclude_inactive=True,
        get_simpreps=True,
    )
    assert isinstance(result, (dict))
    c = creopyson.Client()
    result = c.bom_get_paths()
    assert isinstance(result, (dict))
