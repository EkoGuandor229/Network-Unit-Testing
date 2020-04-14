from nuts.testcreation.network_test_context import TestContext
from nuts.testcreation.network_test_strategy_factory import TestStrategyFactory
from nuts.utilities.logger import Logger


class TestBundle:
    tests = []
    testContext = 0
    logger = 0
    testFactory = 0

    def __init__(self):
        self.testContext = TestContext
        self.logger = Logger
        self.testFactory = TestStrategyFactory

    def create_test_bundle(self, test_definitions):
        for test_definition in test_definitions.values():
            self.tests.append(self.testFactory.factory_method(
                test_definition[1],
                test_definition[2].get_platform(),
                test_definition[2].get_hostname(),
                test_definition[2].get_username(),
                test_definition[2].get_password(),
                test_definition[3])
            )
        return self.tests
