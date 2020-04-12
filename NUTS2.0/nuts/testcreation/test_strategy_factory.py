from nuts.testcreation.concretetests.napalm_ping_test import NapalmPingTest
from nuts.testcreation.concretetests.netmiko_ping_test import NetmikoPingTest
from nuts.testcreation.network_test_factory import TestFactoryInterface


class TestStrategyFactory(TestFactoryInterface):
    def factory_method(self, type_of_test):
        if type_of_test == "Netmiko":
            return NetmikoPingTest("ping", True)
        elif type_of_test == "Napalm":
            return NapalmPingTest("ping", True)
