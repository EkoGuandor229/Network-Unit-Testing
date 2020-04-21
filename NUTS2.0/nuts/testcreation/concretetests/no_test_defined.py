from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NoTestDefined(NetworkTestStrategyInterface):
    """
    The NoTestDefined class is a fallback class to be called, whenever a
    test definition contains a test which is not yet implemented.
    This guarantees, that a faulty specification does not crash the program,
    instead NUTS will complete and notify the user, that test was specified
    wrongly.
    """
    result = 0

    def __init__(self, test_command):
        self.test_command = test_command
        pass

    def run_test(self):
        result = ("Test: " + str(self.test_command) + " is not yet implemented")
        return result

    def evaluate_result(self, result):
        return result

    def print_result(self, result):
        print(result)

    def set_result(self, result):
        self.result = result

    def get_result(self):
        return self.result