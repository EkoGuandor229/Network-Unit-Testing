import abc


class TestFactoryInterface(abc.ABCMeta):

    @abc.abstractmethod
    def factory_method(self, type_of_test):
        pass
