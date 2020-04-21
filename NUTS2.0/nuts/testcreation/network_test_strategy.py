import abc


class NetworkTestStrategyInterface(metaclass=abc.ABCMeta):
    """
    Interface for concrete network test class implementation
    """

    @abc.abstractmethod
    def run_test(self):
        """
        The run_test method executes a test specified in the concrete implementation
        of the network test
        """
        pass

    @abc.abstractmethod
    def evaluate_result(self, result):
        """
        This method evaluates the return value of an executed test with the
        expected result of a concrete implementation of a test
        """
        pass

    @abc.abstractmethod
    def print_result(self, result):
        pass

    @abc.abstractmethod
    def set_result(self, result):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass
