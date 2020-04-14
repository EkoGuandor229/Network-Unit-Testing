from nuts.connectionhandling.connection import Connection
from nuts.inventorymanagement.inventory import Inventory
from nuts.testcreation.network_test_bundle import TestBundle
from nuts.inventorymanagement.network_test_definition_loader import TestDefinitionLoader


class TestBuilder:
    testBundle = TestBundle()
    connection = Connection()
    inventory = Inventory()
    testDefinitionLoader = TestDefinitionLoader()
    testOrder = 0
    logger = 0
    testDefinitions = {}
    tests = []

    def __init__(self):
        self.testDefinitions = self.testDefinitionLoader.create_test_definition_object()

    def create_test_suite(self):
        for test in self.testDefinitions:
            test_device = self.testDefinitions[test].get_test_devices()
            device = self.inventory.devices[test_device]
            self.testDefinitions[test].set_test_devices(device)

    def define_test_order(self):
        self.testOrder = [1, 2, 3]

    def run_tests(self):
        self.tests = self.testBundle.create_test_bundle(self.testDefinitions)
        for test in self.tests:
            result = test.run_test()
            evaluation = test.evaluate_result((result["host1"][0]))
            print(evaluation)


def main():
    builder = TestBuilder()
    builder.create_test_suite()
    builder.run_tests()


if __name__ == '__main__':
    main()