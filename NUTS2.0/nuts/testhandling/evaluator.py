import logging


class Evaluator:
    """
    The Evaluator class compares the expected values for each test with the
    normalized return values of the test-executions.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def compare(self, tests):
        passed_tests = []
        failed_tests = []
        evaluation_results = {}

        for test in tests:
            test_result = test.evaluate_result()
            if test_result is True:
                passed_tests.append(test)
            else:
                failed_tests.append(test)

        evaluation_results["Passed Tests"] = passed_tests
        evaluation_results["Failed Tests"] = failed_tests
        return evaluation_results




