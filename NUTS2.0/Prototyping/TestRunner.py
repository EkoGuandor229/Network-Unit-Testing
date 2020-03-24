class TestRunner:
    logger = 0
    connection = 0
    testSuite = 0
    testResult = 0

    def run_all_tests(self):
        for test in self.testSuite:
            test.run()
