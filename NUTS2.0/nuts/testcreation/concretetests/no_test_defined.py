from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NoTestDefined(NetworkTestStrategyInterface):

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