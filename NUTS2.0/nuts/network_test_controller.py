from time import sleep

import colorama
from colorama import Fore
from pyfiglet import Figlet
from tqdm import tqdm

from nuts.testhandling.evaluator import Evaluator
from nuts.testhandling.network_test_builder import TestBuilder
from nuts.testhandling.network_test_runner import TestRunner


class TestController:
    reporter = 0
    testRunner = TestRunner()
    evaluator = Evaluator()
    testBuilder = TestBuilder()

    def __init__(self):
        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Initializing Test Suite" + 24 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        self.progress_bar("Progress", 0.01)

        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Run all Tests" + 34 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        print("This may take a few seconds")
        self.testRunner.run_all_tests(self.testBuilder.tests)
        print("Tests successful")
        self.progress_bar("Analyzing Results", 0.02)

        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Test Results" + 35 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        self.evaluator.compare(self.testBuilder.tests)

    def progress_bar(self, description, time):
        for i in tqdm(range(100), desc=description, ncols=80,
                      bar_format="%s {l_bar}{bar}{r_bar} %s" % (Fore.CYAN, Fore.RESET)):
            sleep(time)


def run():
    colorama.init()
    f = Figlet(font='slant')
    print(f.renderText("NUTS 2.0"))
    controller = TestController()


if __name__ == "__main__":
    run()