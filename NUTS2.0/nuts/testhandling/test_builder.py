from nuts.connectionhandling.connection import Connection
from nuts.inventorymanagement.inventory import Inventory
from nuts.testcreation.test_bundle import TestBundle
from nuts.inventorymanagement.test_definition_loader import TestDefinitionLoader


class TestBuilder:
    testBundle = TestBundle()
    connection = Connection()
    inventory = Inventory()
    testDefinitionLoader = TestDefinitionLoader()
    testOrder = 0
    logger = 0
    testDefinitions = {}

    def __init__(self):
        self.inventory.create_inventory()
        self.testDefinitions = self.testDefinitionLoader.create_test_definition_object()

    def create_test_suite(self):
        for test in self.testDefinitions:
            test_devices = self.testDefinitions[test].get_test_devices()
            devices = []
            devices.append(self.inventory.devices[test_devices[0]])
            devices.append(self.inventory.devices[test_devices[1]])
            self.testDefinitions[test].set_test_devices(devices)

    def define_test_order(self):
        self.testOrder = [1, 2, 3]


def main():
    builder = TestBuilder()
    builder.create_test_suite()
    builder.testDefinitions["PingTest1"].print_test_definition()


if __name__ == '__main__':
    main()