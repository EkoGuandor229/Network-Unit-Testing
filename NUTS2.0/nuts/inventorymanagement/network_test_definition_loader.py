from nuts.utilities.file_handler import FileHandler
from nuts.inventorymanagement.network_test_definition import TestDefinition


class TestDefinitionLoader:
    """
    The TestDefinitionLoader is a helper-class, that loads the definitions of
    the tests to be executed from a test-definition file in the .yaml format

    ...

    Attributes
    ----------
    test_definitions: collection
        The test definitions specify the tests that should be executed against
        a network system. They are loaded from one or multiple .yaml files
    file_handler
        Reference to the FileHandler-class that is responsible for reading and
        writing in the directory
    """

    def __init__(self):
        self.test_definitions = {}
        self.file_handler = FileHandler()

    def create_test_definition_object(self):
        """
        Loads test definitions from the file system specified in the
        definition_location and instantiates NetworkTestDefinition classes
        """
        definition_location = r"./resources/inventory/TestDefinitions/testDefinitions.yaml"
        test_definition_yaml = self.file_handler.read_file(definition_location)
        try:
            for test_definition in test_definition_yaml:
                self.test_definitions[test_definition[0]] = TestDefinition(
                    test_definition[0],
                    test_definition[1],
                    test_definition[2],
                    test_definition[3],
                    test_definition[4]
                )
        except ValueError:
            print("There are Values missing or in the wrong Format")
        else:
            return self.test_definitions
