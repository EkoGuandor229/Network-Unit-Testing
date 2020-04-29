from colorama import Fore

from nuts.utilities.file_handler import FileHandler
from nuts.utilities.logger import Logger


class Reporter:
    """
    The Reporter-class is responsible to print the test results to the
    console and write a logfile with the test information.
    """
    def __init__(self):
        self.logger = Logger()
        self.file_handler = FileHandler()

    def print_results(self, results):
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

    def save_results(self):
        print(f"Results saved to file with {self.file_handler}")

    def print_passed_results(self, passed_results):
        print(Fore.GREEN + "Passed Tests")
        print(Fore.GREEN + ".")
        print(Fore.GREEN + "|-- Netmiko Pingtest")
        for test_result in passed_results:
            print(Fore.GREEN + f"|   |-- Test: {test_result.get_test_name()} has PASSED")

    def print_failed_results(self, failed_results):
        print(Fore.RED + "Failed Tests")
        print(Fore.RED + ".")
        print(Fore.RED + "|-- Netmiko Pingtest")
        for test_result in failed_results:
            print(Fore.RED + f"|   |-- Test: {test_result.get_test_name()} has FAILED")
            print(Fore.RED + f"|   |   |-- Expected: {test_result.get_expected_value()}")
            print(Fore.RED + f"|   |   |-- Actual: {test_result.get_result()}")
            print(Fore.RED + "|   |")


