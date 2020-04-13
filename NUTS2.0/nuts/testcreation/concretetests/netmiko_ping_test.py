
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command

from nuts.testcreation.network_test_strategy import NetworkTestStrategyInterface


class NetmikoPingTest(NetworkTestStrategyInterface):
    expected = "Success rate is 100 percent (5/5)"

    def __init__(self, platform, hostname, username, password, destination):
        self.destination = destination
        self.nr = InitNornir(inventory={
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
        })

    def run_test(self):
        return self.nr.run(
            task=netmiko_send_command,
            command_string="ping " + str(self.destination)
        )

    def evaluate_result(self, result) -> bool:
        return self.expected in str(result)
