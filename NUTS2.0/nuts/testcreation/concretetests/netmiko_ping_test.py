from nuts.testcreation.test_strategy import NetworkTestStrategyInterface


class NetmikoPingTest(NetworkTestStrategyInterface):
    expected = "none"
    command = "none"

    def __init__(self, command, expected):
        self.command = command
        self.expected = expected

    def run_test(self):
        print("Executing " + str(self.command) + " with expected value: " + str(self.expected) + " as netmiko-command")
