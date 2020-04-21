from colorama import Fore


class Evaluator:
    """
    The Evaluator class compares the expected values for each test with the
    normalized return values of the test-executions.
    """
    logger = None
    evaluation_results = {}

    def compare(self, tests):
        passed_tests = []
        failed_tests = []

        for test in tests:
            actual_result = test.get_result()
            test_result = test.evaluate_result(actual_result)
            if test_result:
                passed_tests.append(test)
            else:
                failed_tests.append(test)

        self.evaluation_results["Passed Tests"] = passed_tests
        self.evaluation_results["Failed Tests"] = failed_tests
        return self.evaluation_results




