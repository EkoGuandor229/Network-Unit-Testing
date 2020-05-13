from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NapalmShowArpTables(NetworkTestStrategyInterface):

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
            getters=["arp_table"]
        )

    def evaluate_result(self) -> bool:
        return self.expected == self.result

    def print_result(self, result):
        print(self.expected)
        print_result(result)

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = []
        result_collection = result["host1"][0].result["arp_table"]
        for i in range(0, len(result_collection)):
            del result_collection[i]["age"]
            self.result.append((result_collection[i]))

    def get_expected_value(self):
        return self.expected

    def get_test_name(self):
        return self.test_name

    def close_connection(self):
        self.nr.close_connections()
