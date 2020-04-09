from time import sleep

import colorama
from colorama import Fore
from pyfiglet import Figlet
from tqdm import tqdm
from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from nuts.testhandling.evaluator import Evaluator
from nuts.testhandling.test_builder import TestBuilder
from nuts.testhandling.test_runner import TestRunner


class TestController:
    reporter = 0
    testRunner = TestRunner()
    evaluator = Evaluator()
    testBuilder = TestBuilder()

    def __init__(self):
        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Initializing Test Suite" + 24 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        self.testBuilder.create_test_suite()

        self.progress_bar("Progress", 0.01)

        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Run all Tests" + 34 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        print("This may take a few seconds")
        result = (self.testRunner.run_all_tests())
        print("Tests successful")
        self.progress_bar("Analyzing Results", 0.02)

        print(Fore.CYAN + "+" + 78 * "-" + "+")
        print(Fore.CYAN + "|" + 31 * " " + "Test Results" + 35 * " " + "|")
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        self.evaluator.compare(result)

    def progress_bar(self, description, time):
        for i in tqdm(range(100), desc=description, ncols=80,
                      bar_format="%s {l_bar}{bar}{r_bar} %s" % (Fore.CYAN, Fore.RESET)):
            sleep(time)


def main():
    colorama.init()
    f = Figlet(font='slant')
    print(f.renderText("NUTS 2.0"))
    controller = TestController()


if __name__ == '__main__':
    main()
