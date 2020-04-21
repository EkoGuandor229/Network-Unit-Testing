class Reporter:
    """
    The Reporter-class is responsible to print the test results to the
    console and write a logfile with the test information.
    """
    evaluationResult = "All tests successful"
    fileHandler = "FileHandler"

    def print_results(self):
        print(self.evaluationResult)

    def save_results(self):
        print("Results saved to file with " + self.fileHandler)


"""
    def compare_gui(self, result):
        passed = 0
        failed = 0
        passed_tests = []
        failed_tests = []
        failed_tests_expectations = []
        failed_tests_actual = []
        for key in result.keys():
            # expected = (result[key][0])
            expected = "Expected Result Mockstring"
            if result[key][0] == expected:
                passed += 1
                passed_tests.append(key)

            else:
                failed += 1
                failed_tests.append(key)
                failed_tests_expectations.append(expected)
                failed_tests_actual.append(result[key][0])

        print(Fore.CYAN + "Overview")
        print(Fore.GREEN + "Tests passed:" + 66 * "." + str(passed))
        print(Fore.RED + "Tests failed: " + 65 * "." + str(failed))
        print(Fore.CYAN + 80 * "-")

        if len(passed_tests) > 0:
            print(Fore.GREEN + "Passed Tests")
            print(Fore.GREEN + ".")
            print(Fore.GREEN + "|-- Show Ip Int Brief")
            for device in passed_tests:
                print(Fore.GREEN + "|   |-- Device: " + str(device) + 50 * "." + "PASSED")

        if len(failed_tests) > 0:
            print(Fore.RED + "Failed Tests")
            print(Fore.RED + ".")
            print(Fore.RED + "|-- Show Ip Int Brief")
            index = 0
            for device in failed_tests:
                print(Fore.RED + "|   |-- Device: " + str(device) + 50 * "." + "FAILED")
                print(Fore.RED + "|   |   |-- Expected: \n" + str(failed_tests_expectations[index]))
                print(Fore.RED + "|   |   |-- Actual: \n" + str(failed_tests_actual[index]))
                print(Fore.RED + "|   |")
                index += 1

        print(Fore.CYAN + 80 * "-")
"""
