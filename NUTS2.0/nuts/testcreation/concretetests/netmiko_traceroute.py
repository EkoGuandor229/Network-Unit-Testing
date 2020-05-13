from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoTraceroute(NetworkTestStrategyInterface):

    def __init__(self, test_definition):
        device_information = test_definition.get_test_devices()
        self.platform = device_information.get_platform()
        self.hostname = device_information.get_hostname()
        self.username = device_information.get_username()
        self.password = device_information.get_password()
        self.destination = test_definition.get_target()
        self.expected = test_definition.get_expected_result()
        self.test_name = test_definition.get_test_id()
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
            command_string=f"traceroute {self.destination}"
        )

    def evaluate_result(self) -> bool:
        if len(self.result) != len(self.expected):
            return False

        i = 0
        for line in self.result:
            array = line.split()
            if self.expected[i] != array[1]:
                return False
            i += 1

        return True

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = []
        result_collection = str(result["host1"][0])
        array = result_collection.splitlines()
        for line in array[3:]:
            self.result.append(line)

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_name

    def close_connection(self):
        self.nr.close_connections()
