from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoShowArpTables(NetworkTestStrategyInterface):

    def __init__(self, test_definition):
        device_information = test_definition.get_test_devices()
        self.platform = device_information.get_platform()
        self.hostname = device_information.get_hostname()
        self.username = device_information.get_username()
        self.password = device_information.get_password()
        self.expected = test_definition.get_expected_result()
        self.test_name = test_definition.get_test_id()
        self.result = None

        self.nr = InitNornir(
            inventory={
                "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
                "options": {
                    "hosts": {
                        "host1": {
                            "platform": str(self.platform),
                            "hostname": str(self.hostname),
                            "username": str(self.username),
                            "password": str(self.password),
                        }
                    }
                }
            },
            logging={"enabled": False}
        )

    def run_test(self):
        return self.nr.run(
            task=netmiko_send_command,
            command_string="show arp"
        )

    def evaluate_result(self) -> bool:
        return self.result == self.expected

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = []
        array = result["host1"][0].result.split()
        for i in range(8, len(array), 6):
            arp_dict = {
                "interface": array[i + 5],
                "mac": self.parse_mac(array[i + 3]),
                "ip": array[i + 1]
            }
            self.result.append(arp_dict)

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_name

    def parse_mac(self, param):
        return f"{param[0:2]}:{param[2:4]}:{param[5:7]}:{param[7:9]}:{param[10:12]}:{param[12:14]}".upper()

    def close_connection(self):
        self.nr.close_connections()