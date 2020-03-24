class Reporter:
    evaluationResult = "All tests successful"
    fileHandler = "FileHandler"

    def print_results(self):
        print(self.evaluationResult)

    def save_results(self):
        print("Results saved to file with " + self.fileHandler)
