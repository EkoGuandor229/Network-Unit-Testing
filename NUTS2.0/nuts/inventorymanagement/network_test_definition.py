class TestDefinition:
    testId = 0
    command = 0
    testDevice = 0
    target = 0
    expectedResult = 0

    def __init__(self, testId, command, test_device, target, expected_result):
        self.testId = testId
        self.command = command
        self.testDevice = test_device
        self.target = target
        self.expectedResult = expected_result

    def print_test_definition(self):
        print(self.testId, self.command, self.testDevice, self.target, self.expectedResult)

    def get_command(self):
        return self.command

    def get_test_devices(self):
        return self.testDevice

    def get_target(self):
        return self.target

    def get_expected_result(self):
        return self.expectedResult

    def set_command(self, command):
        self.command = command

    def set_test_device(self, test_device):
        self.testDevice = test_device
