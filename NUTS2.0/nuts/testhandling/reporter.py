import logging

from colorama import Fore

from nuts.utilities.file_handler import FileHandler


class Reporter:
    """
    The Reporter-class is responsible to print the test results to the
    console and write a logfile with the test information.

    ...

    Attributes
    ----------
    logger
        Instance of the Logger Class
    file_handler
        Instane of the FileHandler Class
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.file_handler = FileHandler()

    def print_results(self, results):
        """
        Categorizes Tests in Passedand Failed and starts the matching method
        """
        passed = results["Passed Tests"]
        failed = results["Failed Tests"]

        if len(passed) > 0:
            self.print_passed_results(passed)
        else:
            print("No tests passed")
        print(80*"-")

        if len(failed) > 0:
            self.print_failed_results(failed)
        else:
            print("No tests failed")

    def save_results(self, results):
        """
        Saves the Results in a file
        """
        print("Saving Results")
        self.file_handler.write_new_run()
        self.file_handler.write_passed_results(results["Passed Tests"])
        self.file_handler.write_failed_results(results["Failed Tests"])

    def print_passed_results(self, passed_results):
        """
        Shows the Results of the Passed tests in the console
        """
        print(Fore.GREEN + "Passed Tests")
        for test_result in passed_results:
            print(Fore.GREEN + f"|   |-- Test: {test_result.get_test_name()} has PASSED")

    def print_failed_results(self, failed_results):
        """
        Shows the Results of the failed tests in the console
        """
        print(Fore.RED + "Failed Tests")
        for test_result in failed_results:
            print(Fore.RED + f"|   |-- Test: {test_result.get_test_name()} has FAILED")
            print(Fore.RED + f"|   |   |-- Expected: {test_result.get_expected_value()}")
            print(Fore.RED + f"|   |   |-- Actual:   {test_result.get_result()}")
            print(Fore.RED + "|   |")

