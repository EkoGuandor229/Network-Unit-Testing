from nuts.inventorymanagement.network_test_definition import TestDefinition


def test_test_definition_parameters():
    test_definition = TestDefinition("Test1", "Ping", "Router01", "127.0.0.1", "PingOk", "Connectivity")
    assert test_definition.get_test_id() == "Test1"
    assert test_definition.get_command() == "Ping"
    assert test_definition.get_test_devices() == "Router01"
    assert test_definition.get_target() == "127.0.0.1"
    assert test_definition.get_expected_result() == "PingOk"
    assert test_definition.get_test_group() == "Connectivity"

