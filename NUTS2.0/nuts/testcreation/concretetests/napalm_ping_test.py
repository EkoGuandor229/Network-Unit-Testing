from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_ping

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NapalmPingTest(NetworkTestStrategyInterface):

    def __init__(self, platform, hostname, username, password, destination, expected):
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
            task=napalm_ping,
            dest=self.destination
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