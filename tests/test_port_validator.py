import pytest
from port_validator import validate_port

@pytest.mark.parametrize(
    "port_number, expected",
    [
        (80, True),
        (443,True),
        (65535,True),
    ]
)

def test_validate_port(port_number, expected):
    assert validate_port(port_number) == expected

@pytest.mark.parametrize(
    "port_number_raises",
    [
        0,
        65536,
        -1,
    ]
)

def test_port_value_error(port_number_raises):
    with pytest.raises(ValueError):
        validate_port(port_number_raises)
