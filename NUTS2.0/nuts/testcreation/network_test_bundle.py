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
        for definition in test_definitions:
            self.tests.append(self.testFactory.factory_method(definition))
        return self.tests
