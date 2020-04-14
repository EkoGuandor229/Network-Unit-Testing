class TestDefinition:
    testId = 0
    command = 0
    testDevices = []
    target = 0
    expectedResult = 0

    def __init__(self, testId, command, testDevices, target, expectedResult):
        self.testId = testId
        self.command = command
        self.testDevices = testDevices
        self.target = target
        self.expectedResult = expectedResult

    def print_test_definition(self):
        print(self.testId, self.command, self.testDevices, self.target, self.expectedResult)

    def get_test_devices(self):
        return self.testDevices

    def set_test_devices(self, test_devices):
        self.testDevices = test_devices
