import abc


class NetworkTestStrategyInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run_test(self):
        pass

    @abc.abstractmethod
    def evaluate_result(self, result):
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
