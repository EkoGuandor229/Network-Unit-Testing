import abc


class TestFactoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def factory_method(self, test_definition):
        pass
