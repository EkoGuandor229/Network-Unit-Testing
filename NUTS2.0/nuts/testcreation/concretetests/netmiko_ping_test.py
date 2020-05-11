from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoPingTest(NetworkTestStrategyInterface):

    def __init__(self, test_id, platform, hostname, username, password, destination, expected):
        self.test_id = test_id
        self.expected = expected
        self.result = None
        self.destination = destination
        self.nr = InitNornir(
            inventory={
                "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
                "options": {
                    "hosts": {
                        "host1": {
                            "platform": str(platform),
                            "hostname": str(hostname),
                            "username": str(username),
                            "password": str(password),
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

    def evaluate_result(self) -> bool:
        return self.expected == self.result

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        for host_name, res_data in result.items():
            mapped_result = res_data[0].result
        if "Success rate is 100 percent (5/5)" in mapped_result:
            self.result = "Success"
        else:
            self.result = "Failure"

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_id
