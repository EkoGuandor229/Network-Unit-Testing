from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NapalmPingTest(NetworkTestStrategyInterface):
    expected = "none"
    command = "none"

    def __init__(self, command, expected):
        self.command = command
        self.expected = expected

    def run_test(self):
        print("Executing " + str(self.command) + " with expected value: " + str(self.expected) + " as napalm ping")