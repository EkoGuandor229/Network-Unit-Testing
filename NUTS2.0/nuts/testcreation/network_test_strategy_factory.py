
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

    def factory_method(self, test_definition):
        """
        Creates concrete instances of tests based on the type of test specified
        in the test_definition

        Parameters
        ----------
        test_definition: collection, mandatory
            a definition of a single network test
        """
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
