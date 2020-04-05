class Evaluator:
    testRunnerResult = 0
    testExpectation = 0
    logger = 0
    evaluationResult = 0

    def compare(self):
        print(self.testRunnerResult == self.testExpectation)
