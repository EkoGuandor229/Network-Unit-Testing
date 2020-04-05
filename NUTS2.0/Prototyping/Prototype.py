from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command
from colorama import Fore, Style


def main():
    nr = InitNornir(config_file="Configurations/config.yaml")
    print(Fore.YELLOW + "*" * 5 + " INITIALIZING PING TEST " + "*" * 37 + Style.RESET_ALL)
    print("\n")
    target = "www.google.com"
    result = nr.run(netmiko_send_command, command_string="ping " + target)
    for key in result.keys():
        response = result[key].result
        if not "!!!" in response:
            print(Fore.CYAN + "-" * 40 + Style.RESET_ALL)
            print(Fore.RED + "Alert: " + Style.RESET_ALL + key + " cannot ping " + target)
            print(Fore.CYAN + "-" * 40 + Style.RESET_ALL)
    print("\n")
    print("*" * 5 + Fore.GREEN + " TEST COMPLETE " + Style.RESET_ALL + "*" * 46)
    print_result(result)



if __name__ == '__main__':
    main()
