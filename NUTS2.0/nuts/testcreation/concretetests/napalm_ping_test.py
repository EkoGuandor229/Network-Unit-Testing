from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_ping

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NapalmPingTest(NetworkTestStrategyInterface):

    def __init__(self, test_definition):
        device_information = test_definition.get_test_devices()
        self.hostname = device_information.get_hostname()
        self.username = device_information.get_username()
        self.password = device_information.get_password()
        self.platform = device_information.get_platform()
        self.expected = test_definition.get_expected_result()
        self.destination = test_definition.get_target()
        self.loopback = device_information.get_loopback()
        self.test_name = test_definition.get_test_id()
        self.result = None

        if self.platform.lower() in "cisco_ios":
            self.platform = "IOS"
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
            task=napalm_ping,
            dest=self.destination, source=self.loopback
        )

    def evaluate_result(self) -> bool:
        return self.expected == self.result

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        result_collection = result["host1"][0].result["success"]
        packet_loss = result_collection["packet_loss"]
        if packet_loss == 0:
            self.result = "Success"
        else:
            self.result = "Failure"

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_name
