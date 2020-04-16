from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
from nornir.plugins.connections.netmiko import Netmiko


class TestRunner:
    logger = 0

    def run_all_tests(self, tests):
        for test in tests:
            test.set_result(test.run_test())

