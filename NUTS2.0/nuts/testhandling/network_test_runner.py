class TestRunner:
    """
    The TestRunner-class executes the tests that are given to it by the
    test controller against a network
    """

    def run_all_tests(self, tests):
        for test in tests:
            test.set_result(test.run_test())

