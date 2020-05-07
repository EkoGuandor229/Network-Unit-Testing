from nuts.testcreation.concretetests.napalm_get_device_interfaces import NapalmShowInterfaces
from nuts.testcreation.concretetests.napalm_ping_test import NapalmPingTest
from nuts.testcreation.concretetests.netmiko_get_interfaces import NetmikoShowInterfaces
from nuts.testcreation.concretetests.netmiko_ping_test import NetmikoPingTest
from nuts.testcreation.concretetests.no_test_defined import NoTestDefined
from nuts.testcreation.network_test_factory import TestFactoryInterface


class TestStrategyFactory(TestFactoryInterface):
    """
    Concrete implementation of the factory method pattern for the creation
    of network tests. The factory decides, which concrete test should be
    instantiated based on the type of the test and returns an instance of that
    test.

    ...
    Methods:
    --------
    factory_method(test_definition)
        Decides, which test to instantiate and returns an instance of the
        concrete test or a NoTestDefined instance
    """

    def __init__(self):
        self.test_map = {
            "Ping": {
                "Napalm": NapalmPingTest,
                "Netmiko": NetmikoPingTest
            },
            "Show Interfaces": {
                "Napalm": NapalmShowInterfaces,
                "Netmiko": NetmikoShowInterfaces
            }
            # Add more Tests as "Testcommand: {connection_dictionary}
        }

    def factory_method(self, test_definition):
        """
        Creates concrete instances of tests based on the type of test specified
        in the test_definition

        Parameters
        ----------
        test_definition: collection, mandatory
            a definition of a single network test
        """
        test_to_implement = NoTestDefined
        test_command = test_definition.get_command()
        connection_types = test_definition.get_connection()
        for connection_option in connection_types:
            test_to_implement = self.test_map[test_command][connection_option]
            break

        return test_to_implement(
            test_definition.get_test_devices().get_platform(),
            test_definition.get_test_devices().get_hostname(),
            test_definition.get_test_devices().get_username(),
            test_definition.get_test_devices().get_password(),
            test_definition.get_target(),
            test_definition.get_expected_result()
        )
