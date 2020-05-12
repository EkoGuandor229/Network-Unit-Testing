import logging


class TestRunner:
    """
    The TestRunner-class executes the tests that are given to it by the
    test controller against a network

    ...

    Attributes
    ----------
    logger
        Instance of the logger class
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def run_all_tests(self, tests):
        """
        Starts the run Method for each test given
        """
        for test in tests:
            result = test.run_test()
            test.set_result(result)

