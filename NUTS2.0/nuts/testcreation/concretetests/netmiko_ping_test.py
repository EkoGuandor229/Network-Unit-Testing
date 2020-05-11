from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoPingTest(NetworkTestStrategyInterface):

    def __init__(self, test_definition):
        device_informations = test_definition.get_test_devices()
        self.hostname = device_informations.get_hostname()
        self.username = device_informations.get_username()
        self.password = device_informations.get_password()
        self.platform = device_informations.get_platform()
        self.expected = test_definition.get_expected_result()
        self.destination = device_informations.get_target()
        self.result = None

        self.nr = InitNornir(
            inventory={
                "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
                "options": {
                    "hosts": {
                        "host1": {
                            "platform": self.platform,
                            "hostname": self.hostname,
                            "username": self.username,
                            "password": self.password,
                        }
                    }
                }
            },
            logging={"enabled": False}
        )

    def run_test(self):
        return self.nr.run(
            task=netmiko_send_command,
            command_string=f"ping {self.destination}"
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
        return f"Ping {self.destination}"
