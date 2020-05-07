from nuts.connectionhandling.connection import Connection
from nuts.inventorymanagement.inventory import Inventory
from nuts.testcreation.network_test_bundle import TestBundle
from nuts.inventorymanagement.network_test_definition_loader import TestDefinitionLoader
from nuts.testhandling.network_test_order import TestOrder


class TestBuilder:
    """
    This class is responsible for the creation of the test-cases from
    predefined test-definitions and a prepared device-inventory.

    ...

    Attributes
    ----------
    network_test_bundle
        reference to the TestBundle-class that is responsible for the
        instantiation of the concrete test-classes from the test-definitions
    connection
        reference to the Connection-class that is responsible for the selection
        of a connection type based on the device type and the possible
        connections for a single device
    inventory
        reference to the inventory-class that is responsible for the creation
        of an inventory with specifications of the different devices in a
        network and the connections between them
    network_test_definition_loader
        reference to the TestDefinitionLoader-class that is responsible for
        loading the network test definitions from a testdefinitions-file
    network_test_definitions
        collection of testdefinitions that gets first passed to the connection
        to determine, which connection the tests should use and is then
        passed to the network_test_bundle to instantiate the concrete tests
    network_tests
        collection of concrete tests that are returned to the
        network_test_controller to be executed against a network

    Methods
    ------
    get_test_definitions()
        loads test definitions from the test_definition_loader
    connect_device_objects()
        connects devices from the inventory with the test definitions
    get_runnable_tests()
        calls the network_test_bundle class to instantiate concrete tests
        according to the test definitions
    """

    def __init__(self):
        self.inventory = Inventory()
        self.connection = Connection()
        self.network_test_definition_loader = TestDefinitionLoader()
        self.network_test_bundle = TestBundle()
        self.network_test_order = TestOrder()
        self.network_test_definitions = {}
        self.network_tests = []

        self.get_test_definitions()
        self.connect_device_objects()
        self.connection.define_connection(self.network_test_definitions)
        self.network_test_order.define_test_order(self.network_test_definitions)
        self.get_runnable_tests()

    def get_test_definitions(self):
        """
        Loads test definitions from the network_test_definition_loader into
        the network_test_definitions collection
        """
        loader = self.network_test_definition_loader
        definitions = loader.create_test_definition_object()
        self.network_test_definitions = definitions

    def connect_device_objects(self):
        """
        Maps devices defined in the network_test_definitions collection to
        specified devices from the inventory
        """
        for test in self.network_test_definitions:
            test_device = self.network_test_definitions[test].get_test_devices()
            device = self.inventory.devices[test_device]
            self.network_test_definitions[test].set_test_device(device)

    def get_runnable_tests(self):
        """
        Gets concrete tests for the tests specified in the
        network_test_definitions collection from the network_test_bundle class
        """
        test_definitions = self.network_test_order.ordered_test_definitions
        test_bundle = self.network_test_bundle.create_test_bundle(test_definitions)
        self.network_tests = test_bundle
