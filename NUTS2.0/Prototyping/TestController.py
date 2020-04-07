from Prototyping.Evaluator import Evaluator
from Prototyping.TestBuilder import TestBuilder
from Prototyping.TestRunner import TestRunner


class TestController:
    reporter = 0
    testRunner = TestRunner()
    evaluator = Evaluator()
    testBuilder = TestBuilder()

    def __init__(self):
        self.testBuilder.create_test_suite()
        self.testRunner.run_all_tests()
        self.evaluator.compare()

def main():
    controller = TestController()


if __name__ == '__main__':
    main()
