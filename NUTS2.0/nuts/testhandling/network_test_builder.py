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
        self.connect_device_objects()
        self.get_runnable_tests()
        self.define_test_order()

    def connect_device_objects(self):
        for test in self.testDefinitions:
            test_device = self.testDefinitions[test].get_test_devices()
            device = self.inventory.devices[test_device]
            self.testDefinitions[test].set_test_device(device)

    def define_test_order(self):
        self.testOrder = [1, 2, 3]

    def get_runnable_tests(self):
        self.tests = self.testBundle.create_test_bundle(self.testDefinitions)
