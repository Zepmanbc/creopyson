"""Objects Tests."""
import pytest
from creopyson.objects import jlpoint


def test_objects_jlpoint():
    """Test jlpoint."""
    result = jlpoint(1, 2, 3)
    assert result == {'x': 1.0, 'y': 2.0, 'z': 3.0}
    # Test fail
    with pytest.raises(Warning):
        jlpoint(1, "2", "trois")
