from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NapalmShowInterfaces(NetworkTestStrategyInterface):

    def __init__(self, test_definition):
        device_information = test_definition.get_test_devices()
        self.hostname = device_information.get_hostname()
        self.username = device_information.get_username()
        self.password = device_information.get_password()
        self.expected = test_definition.get_expected_result()
        self.platform = device_information.get_platform()
        self.test_name = test_definition.get_test_id()
        self.result = None
        if self.platform in "cisco_ios":
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
                            "password": self.password
                        }
                    }
                }
            },
            logging={"enabled": False}
        )

    def run_test(self):
        return self.nr.run(
            task=napalm_get,
            getters=["interfaces"]

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
        result_collection = result["host1"][0].result["interfaces"]
        for key in result_collection.keys():
            self.result.update({key: result_collection[key]["is_up"]})

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_name
