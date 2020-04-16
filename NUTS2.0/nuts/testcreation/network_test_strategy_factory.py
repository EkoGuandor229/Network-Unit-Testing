
from nuts.testcreation.concretetests.netmiko_ping_test import NetmikoPingTest
from nuts.testcreation.concretetests.no_test_defined import NoTestDefined
from nuts.testcreation.network_test_factory import TestFactoryInterface


class TestStrategyFactory(TestFactoryInterface):

    def factory_method(self, test_definition):
        type_of_test = test_definition.get_command()
        if str(type_of_test) == "Netmiko":
            return NetmikoPingTest(
                test_definition.get_test_devices().get_platform(),
                test_definition.get_test_devices().get_hostname(),
                test_definition.get_test_devices().get_username(),
                test_definition.get_test_devices().get_password(),
                test_definition.get_target()
            )
        else:
            return NoTestDefined(type_of_test)
