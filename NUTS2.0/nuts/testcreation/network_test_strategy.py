import abc


class NetworkTestStrategyInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run_test(self):
        pass
