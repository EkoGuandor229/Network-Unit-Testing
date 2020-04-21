from tkinter import BooleanVar


class TestDefinition:
    """
    The TestDefinition-class specifies tests, that should be executed against
    a network

    ...

    Attributes
    ----------
    test_id
        Identifier of a test to differentiate between tests at runtime
    command
        The command specifies, what sort of test the system should execute
        e.g. 'ping', 'show ip int brief' etc.
    test_device
        Specifies the device, on which the tests should be executed
    target
        Specifies a target device for a network-test
    expected_result
        Defines a result which is expected as return value from the test
        e.g. a ping-command should either return successful, unsuccessful or
        with a specified percentage of success (five packets sent, 3 successful)
    connection
        Specifies the type of connection with witch Nornir will connect
    """
    test_id = None
    command = None
    test_device = None
    target = None
    expected_result = None
    connection = None
    is_executed = None

    def __init__(self, test_id, command, test_device, target, expected_result):
        self.test_id = test_id
        self.command = command
        self.test_device = test_device
        self.target = target
        self.expected_result = expected_result
        self.is_executed = BooleanVar()

    def print_test_definition(self):
        print(self.test_id, self.command, self.test_device, self.target, self.expected_result)

    def get_test_id(self):
        return self.test_id

    def get_command(self):
        return self.command

    def get_test_devices(self):
        return self.test_device

    def get_target(self):
        return self.target

    def get_expected_result(self):
        return self.expected_result

    def get_connection(self):
        return self.connection

    def get_is_executed(self):
        return self.is_executed

    def set_is_executed(self, is_executed):
        self.is_executed = is_executed

    def set_command(self, command):
        self.command = command

    def set_test_device(self, test_device):
        self.test_device = test_device

    def set_connection(self, connection):
        self.connection = connection