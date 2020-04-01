from Prototyping.Connection import Connection
from Prototyping.Inventory import Inventory
from Prototyping.TestBundle import TestBundle
from Prototyping.TestDefinitionLoader import TestDefinitionLoader


class TestBuilder:
    testBundle = TestBundle()
    connection = Connection()
    inventory = Inventory()
    testDefinitionLoader = TestDefinitionLoader()
    testOrder = 0
    logger = 0
    testDefinitions = 0

    def __init__(self):
        self.testDefinitions = self.testDefinitionLoader.create_test_definition_object()

    def create_test_suite(self):
        testSuite = str(self.testBundle)
        return testSuite

    def define_test_order(self):
        self.testOrder = [1, 2, 3]
