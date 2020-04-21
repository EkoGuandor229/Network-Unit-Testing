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
