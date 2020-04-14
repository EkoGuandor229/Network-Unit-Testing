from nuts.utilities.file_handler import FileHandler
from nuts.inventorymanagement.test_definition import TestDefinition


class TestDefinitionLoader:
    testDefinitions = {}
    fileHandler = FileHandler()

    def create_test_definition_object(self):
        test_definition_yaml = self.fileHandler.read_file(r"../resources/inventory/TestDefinitions/testDefinitions.yaml")
        try:
            for test_definition in test_definition_yaml:
                devices = test_definition[2].split(',')
                self.testDefinitions[test_definition[0]] = TestDefinition(test_definition[0], test_definition[1], devices, test_definition[3], test_definition[4])
            return self.testDefinitions
        except ValueError:
            print("There are Values missing or in the wrong Format")


def main():
    loader = TestDefinitionLoader()
    loader.create_test_definition_object()
    loader.testDefinitions["PingR1Lo0"].print_test_definition()


if __name__ == '__main__':
    main()
