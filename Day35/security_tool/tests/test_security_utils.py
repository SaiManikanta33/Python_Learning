from security_utils import is_valid_port, classify_status_code


def test_valid_port():
    assert is_valid_port(443) is True


def test_invalid_port():
    assert is_valid_port(70000) is False


def test_success_status():
    assert classify_status_code(200) == "success"


def test_client_error_status():
    assert classify_status_code(404) == "client_error"


def test_server_error_status():
    assert classify_status_code(500) == "server_error"