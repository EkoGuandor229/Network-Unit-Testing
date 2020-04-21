import abc


class TestFactoryInterface(metaclass=abc.ABCMeta):
    """
    Interface for  concrete factory implementation
    """

    @abc.abstractmethod
    def factory_method(self, test_definition):
        pass
