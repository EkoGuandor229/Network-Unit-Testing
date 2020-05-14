import colorama
from colorama import Fore
from pyfiglet import Figlet


class UIHandler:
    def __init__(self):
        colorama.init()
        f = Figlet(font='slant')
        print(Fore.GREEN + f.renderText("NUTS 2.0"))
        self.start_program()

    def start_program(self):
        self.create_border_box("Initializing test suite")

    def create_border_box(self, text: str):
        print(Fore.CYAN + "+" + 98 * "-" + "+")
        print(Fore.CYAN + "| " + text.upper() + (97-len(text)) * " " + "|")
        print(Fore.CYAN + "+" + 98 * "-" + "+")
