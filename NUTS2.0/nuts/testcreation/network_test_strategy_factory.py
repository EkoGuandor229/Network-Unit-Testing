
from nuts.testcreation.concretetests.netmiko_ping_test import NetmikoPingTest
from nuts.testcreation.network_test_factory import TestFactoryInterface


class TestStrategyFactory(TestFactoryInterface):

    def factory_method(self, type_of_test):
        if type_of_test == "Netmiko":
            return NetmikoPingTest(
                "cisco_ios",
                "10.20.0.31",
                "cisco",
                "cisco",
                "172.16.255.1"
            )
        else:
            print("Test not implemented")
