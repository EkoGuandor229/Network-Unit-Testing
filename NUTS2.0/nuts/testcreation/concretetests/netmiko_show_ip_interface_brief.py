from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoShowIpInterfaceBrief(NetworkTestStrategyInterface):

    def __init__(self, test_definition):
        device_information = test_definition.get_test_devices()
        self.platform = device_information.get_platform()
        self.hostname = device_information.get_hostname()
        self.username = device_information.get_username()
        self.password = device_information.get_password()
        self.expected = test_definition.get_expected_result()
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
            command_string="show ip int brief"
        )

    def evaluate_result(self, result) -> bool:
        return self.expected in str(result["host1"][0])

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return f"show ip interface brief of device: {self.hostname}"
