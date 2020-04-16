
from nuts.testcreation.concretetests.netmiko_ping_test import NetmikoPingTest
from nuts.testcreation.network_test_factory import TestFactoryInterface


class TestStrategyFactory(TestFactoryInterface):

    def factory_method(self, type_of_test, *args):
        if str(type_of_test) == "Netmiko":
            return NetmikoPingTest(
                args[0],
                args[1],
                args[2],
                args[3],
                args[4]
            )
        else:
            print("Test not implemented")
