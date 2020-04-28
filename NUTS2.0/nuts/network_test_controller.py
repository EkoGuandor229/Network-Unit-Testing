from time import sleep

import colorama
from colorama import Fore
from pyfiglet import Figlet
from tqdm import tqdm

from nuts.testhandling.evaluator import Evaluator
from nuts.testhandling.network_test_builder import TestBuilder
from nuts.testhandling.network_test_runner import TestRunner
from nuts.testhandling.reporter import Reporter


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
        self.network_test_runner = TestRunner()
        self.evaluator = Evaluator()
        self.network_test_builder = TestBuilder()
        self.reporter = Reporter()

    def logic(self):
        """
        Creates a test-bundle from the test-definition with the test_builder,
        executes the tests with the test_runner, evaluates the test-results
        with the evaluator and finally prints the evaluated results on the
        console and into a log-file.
        """
        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "+{:-^78}+".format(""))
        print(Fore.CYAN + "|" + 31 * " " + "Initializing Test Suite" + 24 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        self.progress_bar("Progress", 0.01)
        test_bundle = self.network_test_builder.network_tests

        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Run all Tests" + 34 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        print("This may take a few seconds")
        self.network_test_runner.run_all_tests(test_bundle)
        print("Test execution successful")
        self.progress_bar("Analyzing Results", 0.02)

        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Test Results" + 35 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        evaluated_results = self.evaluator.compare(test_bundle)
        self.reporter.print_results(evaluated_results)

    def progress_bar(self, description, time):
        for i in tqdm(range(100), desc=description, ncols=80,
                      bar_format="%s {l_bar}{bar}{r_bar} %s" % (Fore.CYAN, Fore.RESET)):
            sleep(time)


def run():
    colorama.init()
    f = Figlet(font='slant')
    print(f.renderText("NUTS 2.0"))
    controller = TestController()
    controller.logic()


if __name__ == "__main__":
    run()
