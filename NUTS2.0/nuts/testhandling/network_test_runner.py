import logging


class TestRunner:
    """
    The TestRunner-class executes the tests that are given to it by the
    test controller against a network
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run_all_tests(self, tests):
        for test in tests:
            result = test.run_test()
            test.set_result(result)

