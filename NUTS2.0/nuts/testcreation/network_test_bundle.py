from nuts.testcreation.network_test_strategy_factory import TestStrategyFactory
from nuts.utilities.logger import Logger


class TestBundle:
    """
    The TestBundle-class orchestrates the instantiation of the concrete tests
    with a test factory. It implements the factory method pattern for the
    instantiation and the strategy pattern to choose a specific test for
    a given test definition.

    ...

    Attributes
    ----------
    network_tests
        A collection of instantiated tests, which are returned to the
        network test builder for further execution
    network_test_factory
        A reference to the TestFactory-class which is responsible to decide,
        which tests should be instantiated for a given test definition and
        and instantiates that conncrete test

    Methods
    -------
    create_test_bundle(test_definitions)
        Instantiates tests that are defined in the test definitions
    """

    def __init__(self):
        self.network_tests = []
        self.logger = Logger()
        self.testFactory = TestStrategyFactory()

    def create_test_bundle(self, test_definitions):
        """
        Fills the network_tests connection with instantiated tests for each
           test defined in the test definition

        Parameters
        ----------
        test_definitions: collection, mandatory
            A collection of defined network tests which should be executed
            according to the test definitions
        """
        for test_definition in test_definitions:
            test = self.testFactory.factory_method(test_definition)
            self.network_tests.append(test)
        return self.network_tests
