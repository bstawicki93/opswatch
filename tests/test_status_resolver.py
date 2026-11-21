from status_resolver import resolve_status

def test_status_200():
    assert resolve_status(200) == "UP"

def test_status_503():
    assert resolve_status(503) == "DOWN"

def test_status_none():
    assert resolve_status(None) == "UNKNOWN"

def test_status_299():
    assert resolve_status(299) == "UP"
