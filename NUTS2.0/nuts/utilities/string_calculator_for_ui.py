import colorama
from colorama import Fore
from pyfiglet import Figlet

# TODO: Delete this, when the project is done.
"""
Helper class that functions as a blueprint for the ui interface and 
lets the user calculate the amount of space left after a string gets printet
this helps to keep the length of a row at 80 characters
"""
def main():
    strCalc = StringCalc()
    print("What would you like to do?")
    print("1: Calculate length of a string...")
    print("2. Calculate length of characters to reach string length of 80")
    print("3: Create a line of output with the input String")
    print("4: Build an example gui")
    choice = int(input("Choose your option\n"))
    if choice == 1:
        strCalc.calculate_length_of_string()
    elif choice == 2:
        strCalc.calculate_length_to_80()
    elif choice == 3:
        strCalc.create_line_with_input()
    elif choice == 4:
        strCalc.build_sample_gui()
    else:
        print("Input was not correct")


class StringCalc(object):
    def calculate_length_of_string(self):
        text = input("Input String\n")
        print(len(text))

    def calculate_length_to_80(self):
        text = input("Input String\n")
        print(80 - len(text))

    def create_line_with_input(self):
        text = input("Input String\n")
        print("+" + 78 * "-" + "+")
        if len(text) > 78:
            print(text)
        elif len(text) % 2 == 0:
            print("|" + int((78 - len(text)) / 2) * " " + text + int((78 - len(text)) / 2) * " " + "|")
        else:
            print("|" + int((79 - len(text)) / 2) * " " + text + int((77 - len(text)) / 2) * " " + "|")
        print("+" + 78 * "-" + "+")

    def build_sample_gui(self):
        colorama.init()
        testPassed = 5
        testFailed = 2
        google = "google.com [172.217.168.68]"
        f = Figlet(font='slant')
        print(f.renderText("NUTS 2.0"))
        print(Fore.CYAN + "+" + 78 * "-" + "+")

        print("+" + 78 * "-" + "+" + Fore.RESET)
        print()
        print(Fore.CYAN + "Overview" + Fore.RESET)
        print(Fore.GREEN + "Test Passed: " + 66 * "." + str(testPassed) + Fore.RESET)
        print(Fore.RED + "Test Failed: " + + 66 * "." + str(testFailed) + Fore.RESET)
        print()
        print(Fore.CYAN + 80 * "-")
        print(Fore.GREEN + "Passed Tests")
        print(".")
        print("|-- Ping Tests")
        print("|   |-- Ping 192.0.2.229" + 50 * "." + "PASSED")
        print("|    -- Ping 192.0.2.23" + 51 * "." + "PASSED")
        print("|    -- Ping " + str(google) + 34 * "." + "PASSED")
        print("|-- Tracert Tests")
        print("|   |-- Tracert 192.0.2.229" + 47 * "." + "PASSED")
        print("|    -- Tracert hsr.ch [152.96.36.83]" + 37 * "." + "PASSED")
        print(Fore.CYAN + 80 * "-")
        print(Fore.RED + "Failed Tests")
        print(".")
        print("|-- Ping Tests")
        print("|   |-- Ping 192.0.2.42" + 50 * "." + "FAILED")
        print("|   |   |-- Expected: True")
        print("|   |   |-- Actual: False")
        print("|-- Tracert Tests")
        print("|   |-- Tracert 192.0.2.42" + 47 * "." + "FAILED")
        print("|   |   |-- Expected: 192.168.1.1")
        print("|   |    --           192.0.2.1")
        print("|   |    --           192.0.2.5")
        print("|   |    --           192.0.2.12")
        print("|   |    --           192.0.2.37")
        print("|   |    --           192.0.2.42")
        print("|   |   |-- Actual:   192.168.1.1")
        print("|   |    --           Destination net unreachable")
        print(Fore.CYAN + 80 * "-")
        print(Fore.RESET)


if __name__ == '__main__':
    main()
