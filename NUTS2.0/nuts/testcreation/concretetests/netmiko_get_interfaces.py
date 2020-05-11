from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoShowInterfaces(NetworkTestStrategyInterface):

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
            command_string="show ip interface brief"
        )

    def evaluate_result(self) -> bool:
        return self.result == self.expected

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = {}
        result_collection = str(result["host1"][0])
        array = result_collection.split()
        for i in range(6, len(array), 6):
            if array[i+4] == "up":
                self.result.update({array[i]: True})
            else:
                self.result.update({array[i]: False})

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_name
