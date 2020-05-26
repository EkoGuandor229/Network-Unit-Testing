import argparse

from nuts.testhandling.evaluator import Evaluator
from nuts.testhandling.network_test_builder import TestBuilder
from nuts.testhandling.network_test_runner import TestRunner
from nuts.testhandling.reporter import Reporter
from nuts.utilities.ui_handler import UIHandler


class TestController:
    """
    The TestController-class is the central part of the NUTS2.0 program

    It controls the flow of the creation, execution and evaluation of
    the network-unit tests.

    ...

    Attributes
    ----------
    network_test_runner
        reference to the TestRunner-class that is responsible for executing
        the network tests against a specified network
    evaluator
        reference to the Evaluator class that is responsible for evaluating
        the results of the executed tests
    network_test_builder
        reference to the TestBuilder-class that is responsible for creating
        the tests as they are specified in the test definition
    reporter
        reference to the Reporter-class that is responsible for printing
        the evaluated test-results and writing the test-log

    Methods
    -------
    logic()
        runs the program logic
    """

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-r", "-runalltests",
                            help="executes all tests without ui-prompt",
                            action="store_true")
        args = parser.parse_args()

        self.ui_handler = UIHandler()
        self.network_test_builder = TestBuilder(args)
        self.network_test_runner = TestRunner()
        self.evaluator = Evaluator()
        self.reporter = Reporter()

    def logic(self):
        """
        Creates a test-bundle from the test-definition with the test_builder,
        executes the tests with the test_runner, evaluates the test-results
        with the evaluator and finally prints the evaluated results on the
        console and into a log-file.
        """

        test_bundle = self.network_test_builder.get_network_tests()
        self.ui_handler.create_border_box("Run all tests")
        self.network_test_runner.run_all_tests(test_bundle)
        self.ui_handler.create_border_box("Test results")
        evaluated_results = self.evaluator.compare(test_bundle)
        self.reporter.print_results(evaluated_results)
        self.reporter.save_results(evaluated_results)

    def get_skip_ui(self):
        return self.skip_ui


def run():
    controller = TestController()
    controller.logic()


if __name__ == "__main__":
    run()
