import logging

from nuts.utilities.progress_bar_handler import ProgressBarHandler


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
        self.progress_bar = ProgressBarHandler()

    def run_all_tests(self, test_bundle):
        self.progress_bar.initiate_progress_bar(len(test_bundle), "Execute tests")
        for test in test_bundle:
            result = test.run_test()
            test.close_connection()
            self.progress_bar.update_progress_bar(1)
            test.set_result(result)
        self.progress_bar.clear_progress_bar()
