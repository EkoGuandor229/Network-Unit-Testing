from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NoTestDefined(NetworkTestStrategyInterface):
    """
    The NoTestDefined class is a fallback class to be called, whenever a
    test definition contains a test which is not yet implemented.
    This guarantees, that a faulty specification does not crash the program,
    instead NUTS will complete and notify the user, that test was specified
    wrongly.
    """

    def __init__(self, test_definition):
        self.test_command = test_definition.get_command()
        self.failure_string = f"Test: {self.test_command} is not yet implemented"
        self.result = None

    def run_test(self):
        result = self.failure_string
        return result

    def evaluate_result(self):
        return False

    def print_result(self, result):
        print(result)

    def set_result(self, result):
        pass

    def get_result(self):
        return self.result

    def get_test_name(self):
        return f"Test with command: {self.test_command}"

    def get_expected_value(self):
        return "Some test implemented"
