class TestBuilder:
    testBundle = 0
    connection = 0
    inventory = 0
    testDefinitionLoader = 0
    testOrder = 0
    logger = 0
    testDefinitions = 0

    def create_test_suite(self):
        testSuite = str(self.testBundle)
        return testSuite

    def define_test_order(self):
        self.testOrder = [1, 2, 3]
