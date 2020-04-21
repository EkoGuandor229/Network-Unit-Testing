from colorama import Fore


class Reporter:
    """
    The Reporter-class is responsible to print the test results to the
    console and write a logfile with the test information.
    """
    evaluationResult = "All tests successful"
    fileHandler = "FileHandler"

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
        print("Results saved to file with " + self.fileHandler)

    def print_passed_results(self, passed_results):
        print(Fore.GREEN + "Passed Tests")
        print(Fore.GREEN + ".")
        print(Fore.GREEN + "|-- Show Ip Int Brief")
        for test_result in passed_results:
            print(Fore.GREEN + "|   |-- Device: " + str() + 50 * "." + "PASSED")

    def print_failed_results(self, failed_results):
        print(Fore.RED + "Failed Tests")
        print(Fore.RED + ".")
        print(Fore.RED + "|-- Show Ip Int Brief")
        for device in failed_results:
            print(Fore.RED + "|   |-- Device: " + str(device) + 50 * "." + "FAILED")
            print(Fore.RED + "|   |   |-- Expected: \n" + str(5))
            print(Fore.RED + "|   |   |-- Actual: \n" + str(229))
            print(Fore.RED + "|   |")


