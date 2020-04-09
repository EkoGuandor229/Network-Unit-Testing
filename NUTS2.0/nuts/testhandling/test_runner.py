from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir.plugins.connections.netmiko import Netmiko


class TestRunner:
    logger = 0
    connection = 0
    testSuite = []
    testResult = 0

    def run_all_tests(self):
        nr = InitNornir(config_file="../resources/config.yaml")
        result = nr.run(
            task=netmiko_send_command,
            command_string="show ip int brief"
        )
        return result


def main():
    runner = TestRunner()
    runner.run_all_tests()


if __name__ == '__main__':
    main()
