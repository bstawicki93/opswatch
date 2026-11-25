import pytest
from status_resolver import resolve_status

@pytest.mark.parametrize(
    "status_code, expected",
    [
        (200, "UP"),
        (503, "DOWN"),
        (None, "UNKNOWN"),
        (299, "UP"),
        (199, "DOWN"),
        (300,"DOWN"),
    ]
)

def test_resolve_status(status_code, expected):
    assert resolve_status(status_code) == expected

def test_status_invalid_type():
    with pytest.raises(TypeError):
        resolve_status("200")