from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


class TestRunner:
    logger = 0
    connection = 0
    testSuite = []
    testResult = 0

    def run_all_tests(self):
        commands = "show ip int brief"
        nr = InitNornir(config_file="Configurations/config.yaml")
        print(nr.inventory.hosts)
        result = nr.run(
            task=netmiko_send_command,
            command_string=commands
        )

        print_result(result)


def main():
    runner = TestRunner()
    runner.run_all_tests()


if __name__ == '__main__':
    main()
