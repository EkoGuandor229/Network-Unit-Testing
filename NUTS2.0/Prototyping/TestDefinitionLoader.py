from Prototyping.FileHandler import FileHandler
from Prototyping.TestDefinition import TestDefinition


class TestDefinitionLoader:
    testDefinitions = {}
    fileHandler = FileHandler()

    def create_test_definition_object(self):
        test_definition_yaml = self.fileHandler.read_test_definition_file()
        for test_definition in test_definition_yaml:
            devices = test_definition[2].split(',')
            self.testDefinitions[test_definition[0]] = TestDefinition(test_definition[0], test_definition[1], devices, test_definition[3])
        return self.testDefinitions


def main():
    loader = TestDefinitionLoader()
    loader.create_test_definition_object()
    print(loader.testDefinitions["PingTest1"].print_test_definition())


if __name__ == '__main__':
    main()