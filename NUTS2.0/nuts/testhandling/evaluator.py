from nuts.utilities.logger import Logger


class Evaluator:
    """
    The Evaluator class compares the expected values for each test with the
    normalized return values of the test-executions.
    """
    def __init__(self):
        self.logger = Logger()

    def compare(self, tests):
        passed_tests = []
        failed_tests = []
        evaluation_results = {}

        for test in tests:
            actual_result = test.get_result()
            test_result = test.evaluate_result(actual_result)
            if test_result is True:
                passed_tests.append(test)
            else:
                failed_tests.append(test)

        evaluation_results["Passed Tests"] = passed_tests
        evaluation_results["Failed Tests"] = failed_tests
        return evaluation_results



