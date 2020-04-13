from nornir.plugins.functions.text import print_result

from nuts.testcreation.network_test_strategy_factory import TestStrategyFactory


class TestContext:
    factory_instance = TestStrategyFactory()
    tests = []
    tests.append(factory_instance.factory_method("Netmiko"))

    def run_all_tests(self):
        for test in self.tests:
            result = test.run_test()
            evaluation = test.evaluate_result((result["host1"][0]))
            print(evaluation)


def main():
    context = TestContext()
    context.run_all_tests()


if __name__ == '__main__':
    main()
