class TestDefinition:
    testId = 0
    command = 0
    testDevices = []
    expectedResult = 0

    def __init__(self, testId, command, testDevices, expectedResult):
        self.testId = testId
        self.command = command
        self.testDevices = testDevices
        self.expectedResult = expectedResult

    def print_test_definition(self):
        print(self.testId, self.command, self.testDevices, self.expectedResult)