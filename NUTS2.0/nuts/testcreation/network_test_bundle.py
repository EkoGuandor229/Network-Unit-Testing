from nuts.testcreation.network_test_context import TestContext
from nuts.testcreation.network_test_strategy_factory import TestStrategyFactory
from nuts.utilities.logger import Logger


class TestBundle:
    network_tests = []
    testContext = 0
    logger = 0
    testFactory = 0

    def __init__(self):
        self.testContext = TestContext
        self.logger = Logger
        self.testFactory = TestStrategyFactory()

    def create_test_bundle(self, test_definitions):
        for test_definition in test_definitions.values():
            test = self.testFactory.factory_method(
                test_definition.get_command(),
                test_definition.get_test_devices().get_platform(),
                test_definition.get_test_devices().get_hostname(),
                test_definition.get_test_devices().get_username(),
                test_definition.get_test_devices().get_password(),
                test_definition.get_target()
            )
            self.network_tests.append(test)
        return self.network_tests
